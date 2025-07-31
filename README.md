# MCP arXiv Server

A FastAPI-based research backend for searching, organizing, and managing arXiv research papers. Provides both HTTP/SSE (Server-Sent Events) and MCP protocol interfaces for real-time, programmatic access to academic papers. Includes Docker support for easy deployment.

---

## Project Overview

This project exposes a modern, agent-ready server for interacting with arXiv:
- **arXiv Paper Search**: Find and organize academic papers by topic.
- **Topic-based Paper Management**: Store and retrieve paper metadata in structured folders.
- **Real-time API**: Access search results and paper data via REST or SSE endpoints.
- **MCP Protocol Integration**: Use with agents and tools supporting the Model Context Protocol.

---

## Features
- **Search arXiv** by research topic with customizable result limits.
- **Store & Organize** paper metadata by topic (JSON format).
- **Retrieve** papers by topic or paper ID.
- **List available topics** and papers per topic.
- **Generate prompts** for AI/LLM research assistance.
- **Real-time updates** via SSE event stream (`/events`).
- **CORS support** for web clients.
- **Dockerized** for reproducible deployment.

---

## Architecture & Key Files
- `research_server.py`: Main FastAPI-based server. Implements all endpoints, SSE, and MCP tools.
- `main.py`: Simple entry point (prints a hello message; not used for server startup).
- `Dockerfile`: Containerizes the server for production use.
- `pyproject.toml`: Project metadata and dependencies.

---

## HTTP & SSE Endpoints

- `POST /search` — Search for papers by topic.
- `GET /list` — List all available topic folders.
- `GET /read` — Retrieve paper info by ID.
- `GET /topic/{topic}` — Get all papers for a topic.
- `GET /events` — Real-time SSE event stream for updates.

---

## MCP Tools

- `search_papers(topic: str, max_results: int = 10) -> List[str]`  
  Search arXiv for papers and store their metadata by topic.

- `extract_info(paper_id: str) -> str`  
  Retrieve metadata for a specific paper by arXiv ID.

- `get_available_folders() -> List[str]`  
  List all topic folders (research areas).

- `get_topic_papers(topic: str) -> List[dict]`  
  Get paper metadata for a given topic.

- `generate_search_prompt(topic: str, num_papers: int = 10) -> str`  
  Generate a prompt for LLMs to find and discuss papers on a topic.

---

## Setup & Installation

### Requirements
- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- Docker (optional, for containerized deployment)

### Local Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mcp-arXiv-server.git
   cd mcp-arXiv-server
   ```
2. Install dependencies:
   ```bash
   pip install uv
   uv pip install --system .
   ```
3. Run the server:
   ```bash
   uv run research_server.py
   ```
   The server will start on `http://localhost:8001` by default.

### Docker Deployment
1. Build and run the Docker container:
   ```bash
   docker build -t mcp-arxiv-server .
   docker run -p 8001:8001 mcp-arxiv-server
   ```
2. Access the API at `http://localhost:8001`.

---

## Usage Examples

### Search for Papers (HTTP)
```bash
curl -X POST http://localhost:8001/search -H "Content-Type: application/json" -d '{"topic": "quantum computing", "max_results": 5}'
```

### Receive Real-time Updates (SSE)
Connect to `http://localhost:8001/events` with an SSE-capable client.

### Use with MCP-compatible Agents
Configure your agent to connect to the MCP server at `http://localhost:8001`.

---

## Limitations & Notes
- **Temporary Storage**: Paper metadata is stored locally in JSON files. Data may be lost if the server or container is restarted.
- **No full-text downloads**: Only metadata is stored, not full PDFs.
- **arXiv API rate limits** may apply for excessive queries.

---

## Credits
- Built with [FastAPI](https://fastapi.tiangolo.com/), [arxiv](https://github.com/lukasschwab/arxiv.py), and [MCP](https://github.com/stackupdev/mcp).
- Dockerized for reproducibility.

## License
MIT License. See `LICENSE` file for details.

## Contributions
Pull requests and issues are welcome!

### `get_available_folders() -> str`
List all available topic folders containing saved papers.
- Returns: Markdown-formatted list of topics

### `get_topic_papers(topic: str) -> str`
Get detailed information about all papers for a specific topic.
- `topic`: The research topic to retrieve papers for
- Returns: Formatted markdown with paper details

### `generate_search_prompt(topic: str, num_papers: int = 5) -> str`
Generate a structured prompt for searching and analyzing papers.
- `topic`: The research topic
- `num_papers`: Number of papers to include in the prompt (default: 5)
- Returns: Formatted prompt text

## Project Structure

```
.
├── README.md          # This documentation file
├── pyproject.toml     # Project metadata and dependencies
├── research_server.py # Main server implementation
├── uv.lock            # Locked dependency versions
└── papers/            # Directory for storing paper metadata
    └── {topic}/       # Each topic gets its own directory
        └── papers_info.json  # Paper metadata for the topic
```

## Deployment on Render.com

### Prerequisites
- A GitHub account with access to the repository
- A Render.com account (free tier available)

### Deployment Steps

1. **Push your code to GitHub**
   - Make sure your code is pushed to a GitHub repository
   - Include all necessary files: `research_server.py`, `pyproject.toml`, and `uv.lock`

2. **Create a new Web Service on Render.com**
   - Log in to your Render.com dashboard
   - Click "New" and select "Web Service"
   - Connect your GitHub account if you haven't already
   - Select the repository containing this project

3. **Configure the Web Service**
   - **Name**: Choose a name for your service
   - **Region**: Select the region closest to your users
   - **Branch**: Select the branch to deploy (usually `main` or `master`)
   - **Build Command**: `pip install -e .`
   - **Start Command**: `python research_server.py`
   - **Environment Variables**: No additional variables needed by default
   - **Plan**: Select the free plan to start

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application
   - The deployment process typically takes 2 5 minutes

5. **Access Your Service**
   - Once deployed, your MCP server will be available at: `https://your-service-name.onrender.com`
   - The server exposes the MCP protocol on the root endpoint

> **Important Note on Storage**: The free tier of Render.com uses ephemeral storage. This means any paper metadata stored will be lost when the server restarts. For persistent storage, consider upgrading to a paid plan with persistent storage or modifying the code to use an external database service.

## Managing Dependencies

## Development Notes

### Local Development
For development and testing, you can run the server locally where file storage will persist between restarts:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mcp-arXiv-server.git
   cd mcp-arXiv-server
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   ```

3. Run the server:
   ```bash
   python research_server.py
   ```

### Dependency Management
Dependencies are managed using `pyproject.toml` and `uv.lock`:

1. **Add a new dependency**:
   ```bash
   uv pip install <package>
   uv pip compile --output-file=uv.lock
   git add pyproject.toml uv.lock
   git commit -m "Add <package> dependency"
   git push
   ```
   Render will automatically detect the changes and redeploy your service.

2. **Update dependencies**:
   ```bash
   uv pip install --upgrade -e .
   uv pip compile --upgrade --output-file=uv.lock
   git add pyproject.toml uv.lock
   git commit -m "Update dependencies"
   git push
   ```
   Again, Render will handle the deployment automatically.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
