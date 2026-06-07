import argparse
import sys
from .catalog import add_entry, list_entries, clean_duplicates, compare_entries

def main():
    parser = argparse.ArgumentParser(
        prog="gguf-manager",
        description="A CLI tool for managing GGUF models"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Catalog subcommand
    catalog_parser = subparsers.add_parser("catalog", help="Manage model catalog")
    catalog_subparsers = catalog_parser.add_subparsers(dest="catalog_command", help="Catalog commands")

    # catalog add
    add_parser = catalog_subparsers.add_parser("add", help="Add a model to the catalog")
    add_parser.add_argument("model_path", help="Path to the GGUF model file")
    add_parser.add_argument("--quant", required=True, help="Quantization type (e.g., Q4_K_M)")
    add_parser.add_argument("--ctx", type=int, required=True, help="Context size")
    add_parser.add_argument("--vram-est", type=int, required=True, help="Estimated VRAM usage in MB")

    # catalog list
    catalog_subparsers.add_parser("list", help="List all models in the catalog")

    # catalog clean
    catalog_subparsers.add_parser("clean", help="Remove duplicate entries from the catalog")

    # TODO: Implement other commands (list, info, download) in later phases

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(0)
    elif args.command == "catalog":
        if args.catalog_command == "add":
            add_entry(args.model_path, args.quant, args.ctx, args.vram_est)
            print(f"Added/updated model: {args.model_path}")
        elif args.catalog_command == "list":
            entries = list_entries()
            if not entries:
                print("Catalog is empty.")
            else:
                print(f"{'Path':<80} {'Quant':<10} {'Ctx':<8} {'VRAM Est (MB)':<15}")
                print("-" * 120)
                for entry in entries:
                    print(f"{entry['path']:<80} {entry['quant']:<10} {entry['ctx']:<8} {entry['vram_est']:<15}")
        elif args.catalog_command == "clean":
            removed = clean_duplicates()
            if removed > 0:
                print(f"Removed {removed} duplicate entry(ies) from the catalog.")
            else:
                print("No duplicates found in the catalog.")
        else:
            catalog_parser.print_help()
            sys.exit(1)
    else:
        print(f"Command '{args.command}' is not yet implemented.")
        sys.exit(1)

if __name__ == "__main__":
    main()