# MCP arXiv Server

## Overview
MCP arXiv Server is a backend service for searching, storing, and managing arXiv research paper metadata. It exposes a set of API endpoints compatible with the Model Context Protocol (MCP) and provides real-time communication via Server-Sent Events (SSE). The server is designed for deployment on Render.com as a containerized web service.

## Architecture
- **Language:** Python 3.11+
- **Frameworks:** FastAPI (for HTTP routes), FastMCP (for MCP protocol/SSE)
- **Dependency Management:** [uv](https://github.com/astral-sh/uv) with `pyproject.toml` and `uv.lock`
- **Containerization:** Dockerfile provided for reproducible builds

## Features
- Search arXiv for papers by topic (using the `arxiv` Python package)
- Store and retrieve paper metadata in topic-based directories
- Expose MCP-compatible tools for integration with MCP clients
- Real-time updates and communication via `/sse` endpoint (SSE transport)
- FastAPI-powered homepage at `/` for project info and documentation

## API Endpoints
- `GET /` — HTML homepage with project info
- `GET /sse` — SSE endpoint for MCP protocol clients
- **MCP Tools (auto-exposed):**
  - `search_papers(topic: str, max_results: int = 5) -> List[str]`
  - `extract_info(paper_id: str)`
  - `get_available_folders()`
  - `get_topic_papers(topic: str)`
  - `generate_search_prompt(topic: str, num_papers: int = 5)`

## File Structure
```
.
├── Dockerfile
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
├── research_server.py
├── uv.lock
```
- `research_server.py`: Main application entry point, defines FastAPI app and MCP tools
- `pyproject.toml`/`uv.lock`: Dependency definitions and locking
- `Dockerfile`: Build instructions for container deployment
- `main.py`: Simple script for testing environment
- `LICENSE`: [MIT License](./LICENSE)

## Deployment (Render.com)
1. **Push to GitHub:** Ensure your repository contains all project files, including Dockerfile and lock files.
2. **Create Render.com Web Service:**
   - Select your GitHub repo
   - Render will detect and use the Dockerfile automatically
   - Set the environment port to `8001`
   - Deploy
3. **Access:**
   - Homepage: `https://<your-app-name>.onrender.com/`
   - SSE endpoint: `https://<your-app-name>.onrender.com/sse`

## Dependency Management
- All Python dependencies are listed in `pyproject.toml` and locked in `uv.lock`.
- To update dependencies, use `uv pip install ...` and regenerate `uv.lock`.
- FastAPI and FastMCP are required for API and protocol functionality.

## License
This project is licensed under the [MIT License](./LICENSE) (c) 2025 The C Foundation.
