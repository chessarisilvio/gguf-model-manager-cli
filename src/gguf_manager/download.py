"""Download utilities for GGUF Model Manager."""

import hashlib
import os
from typing import Optional

from huggingface_hub import hf_hub_download


def download_hf(model_id: str, filename: str, sha256: Optional[str] = None) -> str:
    """Download a file from Hugging Face Hub with optional SHA256 verification.

    Args:
        model_id: The model repository ID (e.g., "TheBloke/Llama-2-7B-GGUF").
        filename: The name of the file to download (e.g., "model.gguf").
        sha256: Expected SHA256 hash of the file (hex string). If provided,
                the downloaded file's hash is verified against this value.

    Returns:
        The local path to the downloaded file.

    Raises:
        ValueError: If sha256 is provided and does not match the computed hash.
        Exception: Propagates any exception from huggingface_hub.hf_hub_download.
    """
    # Download the file (will cache locally)
    downloaded_path = hf_hub_download(
        repo_id=model_id,
        filename=filename,
        # We don't specify a local_dir to use the default cache.
        # The function returns the path to the cached file.
    )

    # If SHA256 verification is requested
    if sha256 is not None:
        # Compute SHA256 of the downloaded file
        sha256_hash = hashlib.sha256()
        with open(downloaded_path, "rb") as f:
            # Read in chunks to handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        computed_hash = sha256_hash.hexdigest()

        if computed_hash != sha256:
            # Remove the mismatched file from cache? We'll leave it to the user.
            raise ValueError(
                f"SHA256 mismatch for file {filename} from {model_id}. "
                f"Expected: {sha256}, Got: {computed_hash}"
            )

    return downloaded_path