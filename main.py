#!/usr/bin/env python3
"""
MCP arXiv Server - Entry Point

A FastMCP-based research server for searching and managing arXiv papers.
"""

import sys
from research_server import mcp


def main():
    """Main entry point for the MCP arXiv server."""
    try:
        print("Starting MCP arXiv Server...")
        print("Server will be available at http://localhost:8001")
        print("Press Ctrl+C to stop the server")
        
        # Run the FastMCP server with SSE transport
        mcp.run(transport='sse')
        
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
