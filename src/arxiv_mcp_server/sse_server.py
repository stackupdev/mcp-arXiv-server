"""
SSE-enabled HTTP server for arXiv MCP Server
==========================================

This module implements an HTTP server with Server-Sent Events (SSE) support
for real-time communication with the arXiv MCP server.
"""

import asyncio
import json
import logging
from typing import Dict, Any, List, AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sse_starlette.sse import EventSourceResponse
import uvicorn

from .config import Settings
from .tools import handle_search, handle_download, handle_list_papers, handle_read_paper
from .tools import search_tool, download_tool, list_tool, read_tool
from .prompts.handlers import list_prompts as handler_list_prompts
from .prompts.handlers import get_prompt as handler_get_prompt
import mcp.types as types

settings = Settings()
logger = logging.getLogger("arxiv-mcp-sse-server")
logger.setLevel(logging.INFO)

# Global event queue for SSE
event_queue: asyncio.Queue = asyncio.Queue()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan."""
    logger.info("Starting arXiv MCP SSE Server")
    yield
    logger.info("Shutting down arXiv MCP SSE Server")


# Create FastAPI app with SSE support
app = FastAPI(
    title="arXiv MCP Server with SSE",
    description="A flexible arXiv search and analysis service with Server-Sent Events support",
    version=settings.APP_VERSION,
    lifespan=lifespan
)

# Add CORS middleware for web clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def send_sse_event(event_type: str, data: Dict[str, Any]):
    """Send an event to all SSE clients."""
    event_data = {
        "type": event_type,
        "data": data,
        "timestamp": asyncio.get_event_loop().time()
    }
    await event_queue.put(event_data)


async def event_stream() -> AsyncGenerator[str, None]:
    """Generate SSE events for clients."""
    while True:
        try:
            # Wait for events with timeout to send keep-alive
            event = await asyncio.wait_for(event_queue.get(), timeout=30.0)
            yield f"data: {json.dumps(event)}\n\n"
        except asyncio.TimeoutError:
            # Send keep-alive ping
            yield "data: {\"type\": \"ping\", \"timestamp\": " + str(asyncio.get_event_loop().time()) + "}\n\n"
        except Exception as e:
            logger.error(f"Error in event stream: {e}")
            yield f"data: {{\"type\": \"error\", \"message\": \"{str(e)}\"}}\n\n"


@app.get("/events")
async def stream_events(request: Request):
    """SSE endpoint for real-time events."""
    return EventSourceResponse(event_stream())


@app.get("/")
async def root():
    """Root endpoint with server information."""
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "description": "arXiv MCP Server with SSE support",
        "endpoints": {
            "events": "/events",
            "tools": "/tools",
            "prompts": "/prompts",
            "search": "/search",
            "download": "/download",
            "list": "/list",
            "read": "/read"
        }
    }


@app.get("/tools")
async def list_tools():
    """List available arXiv research tools."""
    tools = [search_tool, download_tool, list_tool, read_tool]
    return {"tools": [tool.model_dump() for tool in tools]}


@app.get("/prompts")
async def list_prompts():
    """List available prompts."""
    prompts = await handler_list_prompts()
    return {"prompts": [prompt.model_dump() for prompt in prompts]}


@app.get("/prompts/{prompt_name}")
async def get_prompt(prompt_name: str, arguments: Dict[str, str] = None):
    """Get a specific prompt with arguments."""
    try:
        result = await handler_get_prompt(prompt_name, arguments)
        return {"prompt": result.model_dump()}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post("/search")
async def search_papers(request: Dict[str, Any]):
    """Search for arXiv papers with SSE notifications."""
    try:
        # Send start event
        await send_sse_event("search_started", {"query": request.get("query", "")})
        
        # Perform search
        result = await handle_search(request)
        
        # Send completion event
        await send_sse_event("search_completed", {
            "query": request.get("query", ""),
            "results_count": len(result)
        })
        
        return {"results": [r.model_dump() for r in result]}
    except Exception as e:
        await send_sse_event("search_error", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/download")
async def download_paper(request: Dict[str, Any]):
    """Download a paper with SSE notifications."""
    try:
        # Send start event
        await send_sse_event("download_started", {"paper_id": request.get("paper_id", "")})
        
        # Perform download
        result = await handle_download(request)
        
        # Send completion event
        await send_sse_event("download_completed", {"paper_id": request.get("paper_id", "")})
        
        return {"result": [r.model_dump() for r in result]}
    except Exception as e:
        await send_sse_event("download_error", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/list")
async def list_papers(request: Dict[str, Any]):
    """List papers with SSE notifications."""
    try:
        # Send start event
        await send_sse_event("list_started", {})
        
        # Perform listing
        result = await handle_list_papers(request)
        
        # Send completion event
        await send_sse_event("list_completed", {"papers_count": len(result)})
        
        return {"papers": [r.model_dump() for r in result]}
    except Exception as e:
        await send_sse_event("list_error", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/read")
async def read_paper(request: Dict[str, Any]):
    """Read paper content with SSE notifications."""
    try:
        # Send start event
        await send_sse_event("read_started", {"paper_id": request.get("paper_id", "")})
        
        # Perform reading
        result = await handle_read_paper(request)
        
        # Send completion event
        await send_sse_event("read_completed", {"paper_id": request.get("paper_id", "")})
        
        return {"content": [r.model_dump() for r in result]}
    except Exception as e:
        await send_sse_event("read_error", {"error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/tools/{tool_name}")
async def call_tool(tool_name: str, arguments: Dict[str, Any]):
    """Generic tool calling endpoint with SSE notifications."""
    try:
        # Send start event
        await send_sse_event("tool_started", {"tool": tool_name, "arguments": arguments})
        
        # Call the appropriate tool
        if tool_name == "search_papers":
            result = await handle_search(arguments)
        elif tool_name == "download_paper":
            result = await handle_download(arguments)
        elif tool_name == "list_papers":
            result = await handle_list_papers(arguments)
        elif tool_name == "read_paper":
            result = await handle_read_paper(arguments)
        else:
            raise HTTPException(status_code=404, detail=f"Unknown tool: {tool_name}")
        
        # Send completion event
        await send_sse_event("tool_completed", {"tool": tool_name})
        
        return {"result": [r.model_dump() for r in result]}
    except Exception as e:
        await send_sse_event("tool_error", {"tool": tool_name, "error": str(e)})
        raise HTTPException(status_code=500, detail=str(e))


def run_sse_server(host: str = None, port: int = None):
    """Run the SSE-enabled HTTP server."""
    host = host or settings.HOST
    port = port or settings.PORT
    
    logger.info(f"Starting arXiv MCP SSE Server on {host}:{port}")
    uvicorn.run(
        "arxiv_mcp_server.sse_server:app",
        host=host,
        port=port,
        reload=False,
        log_level="info"
    )


if __name__ == "__main__":
    run_sse_server()
