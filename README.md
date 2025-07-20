# MCP arXiv Server

A backend service for searching and managing arXiv research paper information, designed for easy deployment and integration. This project is suitable for both developers and users who want a reliable way to interact with arXiv data programmatically or via web endpoints.

## What is this project?
This server lets you search for research papers on arXiv, organize results by topic, and access them through modern web APIs. It supports real-time updates via Server-Sent Events (SSE) and is compatible with the Model Context Protocol (MCP) for advanced integrations.

## How does it work?
- **Built with Python 3.11+** for reliability and modern features.
- **FastAPI** handles web/API routes (like the homepage and docs).
- **FastMCP** provides the MCP protocol and SSE endpoint for real-time communication.
- **Dependencies** are managed with `pyproject.toml` and locked for reproducibility with `uv.lock`.
- **Dockerfile** makes deployment on platforms like Render.com simple and consistent.

## Main Features
- Search arXiv for papers by topic (using the official arxiv Python package)
- Save and retrieve paper metadata in organized folders
- Real-time updates and communication via `/sse` endpoint
- Clear, friendly homepage at `/` for info and documentation
- Exposes MCP-compatible tools for automation or integration

## API Endpoints (What can you call?)
- `GET /` — Homepage with project info (HTML)
- `GET /sse` — Real-time SSE endpoint for MCP clients
- **MCP Tools (auto-exposed as API calls):**
  - `search_papers(topic: str, max_results: int = 5)` — Search and store papers
  - `extract_info(paper_id: str)` — Get info for a specific paper
  - `get_available_folders()` — List all topic folders
  - `get_topic_papers(topic: str)` — Get all papers for a topic
  - `generate_search_prompt(topic: str, num_papers: int = 5)` — Generate a search prompt for AI tools

## Project Structure (What's in the repo?)
```
.
├── Dockerfile         # Container build instructions
├── LICENSE            # Project license (MIT)
├── README.md          # This documentation file
├── main.py            # Simple test script
├── pyproject.toml     # Dependency definitions
├── research_server.py # Main server code
├── uv.lock            # Locked dependency versions
```

## How to Deploy (on Render.com)
1. **Push your code to GitHub** (include Dockerfile and all lock files).
2. **Create a new Web Service on Render.com:**
   - Select your GitHub repo
   - Render will auto-detect the Dockerfile
   - Set the environment port to `8001`
   - Click Deploy
3. **Access your service:**
   - Homepage: `https://<your-app-name>.onrender.com/`
   - SSE endpoint: `https://<your-app-name>.onrender.com/sse`

## Managing Dependencies
- All dependencies are listed in `pyproject.toml` and locked in `uv.lock`.
- To add or update dependencies, use `uv pip install ...` and regenerate `uv.lock`.
- FastAPI and FastMCP are required for the API and SSE functionality.

## License
This project is licensed under the [MIT License](./LICENSE) © 2025 The C Foundation.
