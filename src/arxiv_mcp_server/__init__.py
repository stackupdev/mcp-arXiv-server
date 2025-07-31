"""
Arxiv MCP Server initialization
"""

from . import server
import asyncio
import sys


def main():
    """Main entry point for the package (MCP stdio server)."""
    asyncio.run(server.main())


def main_sse():
    """Main entry point for SSE-enabled HTTP server."""
    try:
        from . import sse_server
    except ImportError as e:
        print(f"Error: SSE server dependencies not available: {e}")
        print("Please install FastAPI dependencies: pip install fastapi uvicorn sse-starlette")
        sys.exit(1)
    
    # Parse command line arguments for host and port
    host = "0.0.0.0"
    port = 8000
    
    if len(sys.argv) > 1:
        try:
            if "--host" in sys.argv:
                host_idx = sys.argv.index("--host") + 1
                if host_idx < len(sys.argv):
                    host = sys.argv[host_idx]
            if "--port" in sys.argv:
                port_idx = sys.argv.index("--port") + 1
                if port_idx < len(sys.argv):
                    port = int(sys.argv[port_idx])
        except (ValueError, IndexError):
            print("Usage: arxiv-mcp-server-sse [--host HOST] [--port PORT]")
            sys.exit(1)
    
    sse_server.run_sse_server(host, port)


__all__ = ["main", "main_sse", "server"]
