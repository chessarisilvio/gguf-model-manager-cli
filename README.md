# GGUF Model Manager CLI

A command-line interface for managing GGUF models.

## Descrizione

GGUF Model Manager CLI è uno strumento da riga di comando progettato per aiutare gli utenti a gestire i propri modelli GGUF (GPT-Generated Unified Format). Fornisce funzionalità per aggiungere, elencare, pulire e confrontare le voci del catalogo dei modelli, semplificando il tracciamento delle quantizzazioni, delle dimensioni del contesto e dell'utilizzo stimato della VRAM.

## Architettura

Il progetto è strutturato come un pacchetto Python con i seguenti componenti principali:

- `src/gguf_manager/__init__.py`: File di inizializzazione del pacchetto (vuoto, presente per rendere la directory un pacchetto).
- `src/gguf_manager/cli.py`: Contiene l'interfaccia della riga di comando costruita con `argparse`. Definisce i comandi e i sottocomandi disponibili.
- `src/gguf_manager/catalog.py`: Implementa le operazioni di base sul catalogo (aggiunta, elenco, pulizia, confronto) utilizzando un file JSON situato in `~/.gguf_manager_catalog.json`.

Il catalogo è memorizzato come un file JSON nella home directory dell'utente, garantendo persistenza tra le sessioni.

## Installazione

Per installare il pacchetto in modalità di sviluppo:

```bash
pip install -e .
```

Per installarlo normalmente:

```bash
pip install .
```

## Uso

Dopo l'installazione, il comando `gguf-manager` sarà disponibile.

### Visualizzare l'aiuto

```bash
gguf-manager --help
```

### Gestione del catalogo

#### Aggiungere un modello

```bash
gguf-manager catalog add /path/to/model.gguf --quant Q4_K_M --ctx 4096 --vram-est 4096
```

#### Elencare i modelli

```bash
gguf-manager catalog list
```

#### Pulire le voci duplicate

```bash
gguf-manager catalog clean
```

### Esempi

Aggiungere un modello quantizzato Q5_K_M con contesto 8192 e stima VRAM 6144 MB:

```bash
gguf-manager catalog add ./models/llama-3-8b-q5_k_m.gguf --quant Q5_K_M --ctx 8192 --vram-est 6144
```

Elencare tutti i modelli nel catalogo:

```bash
gguf-manager catalog list
```

Output di esempio:
```
Path                                                               Quant     Ctx     VRAM Est (MB)
------------------------------------------------------------------------------------------------------------------------
~/models/llama-3-8b-q5_k_m.gguf                                     Q5_K_M    8192    6144
~/models/mistral-7b-v0.1-q4_k_m.gguf                               Q4_K_M    4096    4096
```

## Stato

✅ COMPLETATO — 2026-06-07
- Fase 1/5 — Creazione struttura progetto: completata
- Fase 2/5 — Scaffold del pacchetto Python: completata
- Fase 3/5 — Implementazione funzionalità core: completata

Le funzionalità implementate includono:
- Comando `catalog add` per aggiungere o aggiornare voci di modello
- Comando `catalog list` per visualizzare tutti i modelli nel catalogo
- Comando `catalog clean` per rimuovere voci duplicate
- Persistenza del catalogo tramite file JSON nella home directory
- Struttura del pacchetto Python pronta per l'installazione tramite pip

## Sviluppo

Per contribuire al progetto:

1. Forkare il repository
2. Creare un branch per la feature (`git checkout -b feature/nuova-feature`)
3. Effettuare le modifiche
4. Commit delle modifiche (`git commit -am 'Aggiunta nuova feature'`)
5. Push al branch (`git push origin feature/nuova-feature`)
6. Aprire una Pull Request

## Licenza

Questo progetto è rilasciato sotto la licenza MIT. Vedere il file `LICENSE` per ulteriori dettagli.