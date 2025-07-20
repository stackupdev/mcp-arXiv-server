# MCP arXiv Server

A FastMCP-based backend service for searching, organizing, and managing arXiv research papers. This project provides a simple interface to search for academic papers, store their metadata, and retrieve them by topic or paper ID.

## What is this project?
This server provides programmatic access to arXiv papers through a set of MCP-compatible tools. It allows you to:
- Search for papers on any topic
- Store paper metadata locally
- Retrieve papers by topic or ID
- Generate structured search prompts for AI assistance

## How does it work?
- Built with **Python 3.10+** for reliability and modern features
- Uses the official **arxiv** Python package for searching arXiv
- **FastMCP** provides the MCP protocol and web interface
- Dependencies are managed with `pyproject.toml` and locked with `uv.lock`
- Paper metadata is stored in JSON files organized by topic

## Main Features
- **Paper Search**: Search arXiv for papers by topic with customizable result limits
- **Metadata Management**: Automatically store and organize paper metadata by topic
- **Topic-based Organization**: Easily browse papers by their research topics
- **MCP Integration**: Exposes tools through the Model Context Protocol
- **Simple Storage**: Uses JSON files for easy inspection and backup

## Available MCP Tools

The server exposes the following tools through the MCP protocol:

### `search_papers(topic: str, max_results: int = 5) -> List[str]`
Search arXiv for papers on a specific topic and store their metadata.
- `topic`: The research topic to search for
- `max_results`: Maximum number of results to return (default: 5)
- Returns: List of paper IDs found in the search

### `extract_info(paper_id: str) -> str`
Retrieve information about a specific paper by its ID.
- `paper_id`: The arXiv paper ID to look up
- Returns: JSON string with paper details or error message

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

## Getting Started

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/stackupdev/mcp-arXiv-server.git
   cd mcp-arXiv-server
   ```

2. Install dependencies using `uv` (recommended):
   ```bash
   uv pip install -e .
   ```
   Or using pip:
   ```bash
   pip install -e .
   ```

### Running the Server

Start the server with:
```bash
python research_server.py
```

The server will start on port 8001 by default. You can now connect to it using any MCP-compatible client.

## Managing Dependencies

Dependencies are managed using `pyproject.toml` and `uv.lock`:

- To add a new dependency:
  ```bash
  uv pip install <package>
  uv pip compile --output-file=uv.lock
  ```

- To update all dependencies:
  ```bash
  uv pip install --upgrade -e .
  uv pip compile --upgrade --output-file=uv.lock
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
