import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional

CATALOG_FILE = Path.home() / ".gguf_manager_catalog.json"


def load_catalog() -> List[Dict[str, Any]]:
    """Load the catalog from the JSON file."""
    if not CATALOG_FILE.exists():
        return []
    try:
        with open(CATALOG_FILE, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (json.JSONDecodeError, IOError):
        return []


def save_catalog(catalog: List[Dict[str, Any]]) -> None:
    """Save the catalog to the JSON file."""
    with open(CATALOG_FILE, 'w') as f:
        json.dump(catalog, f, indent=2)


def add_entry(model_path: str, quant: str, ctx: int, vram_est: int) -> None:
    """Add a model entry to the catalog if it doesn't already exist."""
    catalog = load_catalog()
    # Normalize the path
    model_path = os.path.abspath(model_path)
    # Check if entry with same path already exists
    for entry in catalog:
        if entry.get('path') == model_path:
            # Update existing entry
            entry.update({
                'quant': quant,
                'ctx': ctx,
                'vram_est': vram_est
            })
            save_catalog(catalog)
            return
    # Add new entry
    catalog.append({
        'path': model_path,
        'quant': quant,
        'ctx': ctx,
        'vram_est': vram_est
    })
    save_catalog(catalog)


def list_entries() -> List[Dict[str, Any]]:
    """Return all catalog entries."""
    return load_catalog()


def clean_duplicates() -> int:
    """Remove duplicate entries (by path) and return number of removed entries."""
    catalog = load_catalog()
    seen = set()
    unique = []
    removed = 0
    for entry in catalog:
        path = entry.get('path')
        if path in seen:
            removed += 1
        else:
            seen.add(path)
            unique.append(entry)
    if removed > 0:
        save_catalog(unique)
    return removed


def compare_entries(entry1: Dict[str, Any], entry2: Dict[str, Any]) -> Dict[str, Any]:
    """Compare two entries side-by-side and return a dict of differences."""
    all_keys = set(entry1.keys()) | set(entry2.keys())
    comparison = {}
    for key in all_keys:
        val1 = entry1.get(key)
        val2 = entry2.get(key)
        if val1 != val2:
            comparison[key] = {'entry1': val1, 'entry2': val2}
    return comparison