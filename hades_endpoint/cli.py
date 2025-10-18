"""CLI entry point for HADES Endpoint Security."""

import sys
from horizon_core.logging import setup_logging, get_logger


def main():
    """Main entry point for the HADES CLI."""
    setup_logging(level="INFO")
    logger = get_logger(__name__)
    logger.info("HADES Endpoint Security CLI started")
    
    if len(sys.argv) < 2:
        print("Usage: hades <command>")
        print("Available commands:")
        print("  scan - Run endpoint security scan")
        return 0
    
    command = sys.argv[1]
    
    if command == "scan":
        from hades_endpoint.endpoint_scanner import EndpointScanner
        scanner = EndpointScanner()
        scanner.run_scan()
    else:
        print(f"Unknown command: {command}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
