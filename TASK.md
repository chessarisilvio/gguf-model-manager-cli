# GGUF Model Manager CLI

**ID**: 202606071200-02
**Categoria**: progetto
**Difficoltà**: Facile
**Stima**: 1-2gg
**Approvata**: 2026-06-07T12:00:00
**Directory**: /media/rust/hd-linux/home/rust/Scrivania/Hub/lavoro-tech/gguf-model-manager-cli

## Descrizione

Tool CLI Python (gguf-manager) per gestione locale modelli GGUF: download da HuggingFace con verifica SHA256, catalogo JSON con metadata (quant, ctx, VRAM stimata), confronto side-by-side, pulizia duplicati. Pubblicato su PyPI. README professionale con benchmark P40. Lead generation per consulting.

## Piano sotto-task (5 fasi)

- **[1] Creazione struttura progetto**: Crea la cartella /media/rust/hd-linux/home/rust/Scrivania/Hub/lavoro-tech/gguf-model-manager-cli, inizializza un reposit
- **[2] Scaffold del pacchetto Python**: Genera pyproject.toml, src/gguf_manager/__init__.py e src/gguf_manager/cli.py con entry‑point console_script 'gguf-manag
- **[3] Funzione download con verifica SHA256**: Implementa in src/gguf_manager/download.py la funzione download_hf(model_id, filename, sha256) che usa huggingface_hub p
- **[4] Gestione catalogo e pulizia duplicati**: Crea src/gguf_manager/catalog.py per leggere/scrivere catalogo JSON (metadata: quant, ctx, vram_est), aggiungere entry, 
- **[5] Documentazione finale e aggiornamento vault**: Scrivi README.md completo (installazione, uso, benchmark teorico su P40, guida al testing manuale) e aggiorna il vault d
