"""CLI entry point for HADES Endpoint Security."""

import sys
from hades_endpoint.log_utils import setup_logging


def main():
    """Main entry point for the HADES CLI."""
    logger = setup_logging()
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
