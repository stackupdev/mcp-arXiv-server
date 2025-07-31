# MCP arXiv Server

A FastMCP-based research server providing arXiv paper search, topic-based paper management, and real-time SSE/REST API endpoints. Implements MCP tools to search, organize, and retrieve academic papers by topic, expose research data via HTTP/SSE, and support integration with agents and web clients.

## Overview

This project provides a Model Context Protocol (MCP) server that interfaces with arXiv to search, organize, and manage academic papers. Built with FastMCP and running on port 8001, it offers both programmatic access through MCP tools and real-time updates via Server-Sent Events (SSE).

## Features

- **arXiv Paper Search**: Search for academic papers by topic with customizable result limits
- **Topic-based Organization**: Automatically organize papers into topic-specific directories
- **Paper Metadata Storage**: Store and retrieve paper information in JSON format
- **MCP Protocol Support**: Expose functionality through standardized MCP tools
- **Real-time Updates**: SSE transport for live data streaming
- **Docker Support**: Containerized deployment for easy scaling

## Architecture

### Key Files
- `research_server.py`: Main FastMCP server implementation with all MCP tools and SSE support
- `main.py`: Simple entry point (prints hello message, not used for server startup)
- `Dockerfile`: Container configuration for deployment
- `pyproject.toml`: Project metadata and dependencies

### Data Storage
Papers are organized in a `papers/` directory structure:
```
papers/
└── {topic_name}/
    └── papers_info.json
```

## MCP Tools

The server exposes the following MCP tools:

### `search_papers(topic: str, max_results: int = 10) -> List[str]`
Search arXiv for papers on a specific topic and store their metadata.
- **topic**: Research topic to search for
- **max_results**: Maximum number of results (default: 10)
- **Returns**: List of paper IDs found

### `extract_info(paper_id: str) -> str`
Retrieve information about a specific paper by its arXiv ID.
- **paper_id**: The arXiv paper ID to look up
- **Returns**: JSON string with paper details or error message

### `get_available_folders() -> str`
List all available topic folders in the papers directory.
- **Returns**: Markdown-formatted list of available topics

### `get_topic_papers(topic: str) -> str`
Get detailed information about all papers for a specific topic.
- **topic**: The research topic to retrieve papers for
- **Returns**: Formatted markdown with paper details

### `generate_search_prompt(topic: str, num_papers: int = 10) -> str`
Generate a structured prompt for AI assistance with paper research.
- **topic**: The research topic
- **num_papers**: Number of papers to include in prompt (default: 10)
- **Returns**: Formatted prompt text for AI/LLM use

## Installation & Setup

### Requirements
- Python 3.10+
- Dependencies: `arxiv>=2.2.0`, `mcp>=1.7.1`

### Local Development
1. Clone the repository:
   ```bash
   git clone <repository-url>
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

The server will start on `http://localhost:8001` with SSE transport enabled.

### Docker Deployment

Build and run using Docker:

```bash
# Build the image
docker build -t mcp-arxiv-server .

# Run the container
docker run -p 8001:8001 mcp-arxiv-server
```

The Dockerfile uses:
- Python 3.11 slim base image
- UV package manager for fast dependency installation
- Exposes port 8001
- Runs `research_server.py` as the main command

## Usage

### MCP Client Integration
Connect your MCP-compatible client to `http://localhost:8001` to access the available tools.

### Direct API Access
The server runs with SSE transport, enabling real-time communication and event streaming.

## Data Persistence

- Paper metadata is stored locally in JSON files organized by topic
- Data persists between server restarts when running locally
- In containerized environments, consider mounting a volume for the `papers/` directory to maintain persistence

## Limitations

- Only metadata is stored, not full PDF downloads
- arXiv API rate limits may apply for excessive queries
- Local file storage (consider external database for production use)

## License

This project is licensed under the terms specified in the [LICENSE](LICENSE) file.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.
