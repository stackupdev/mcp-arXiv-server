# MCP arXiv Server

A FastMCP-based research server for searching, organizing, and managing arXiv academic papers. This project provides a comprehensive interface to search for papers, store their metadata locally, and retrieve them through various methods.

## What is this project?
This server provides programmatic access to arXiv papers through a set of MCP-compatible tools, resources, and prompts. It allows you to:
- Search for papers on any research topic
- Store paper metadata locally in organized JSON files
- Retrieve papers by topic or individual paper ID
- Browse available topics and papers through MCP resources
- Generate structured research prompts for AI assistance

## How does it work?
- Built with **Python 3.10+** for modern language features
- Uses the official **arxiv** Python package for arXiv API integration
- **FastMCP** framework provides MCP protocol support with SSE transport
- Paper metadata is stored in local JSON files organized by topic directories
- Runs on port 8001 by default with SSE (Server-Sent Events) transport

## Main Features
- **Paper Search**: Search arXiv for papers by topic with configurable result limits
- **Local Storage**: Persistent storage of paper metadata in organized JSON files
- **Topic Organization**: Automatic organization of papers by research topics
- **MCP Tools**: Complete set of tools for paper search and retrieval
- **MCP Resources**: Dynamic resources for browsing topics and papers
- **MCP Prompts**: Pre-built prompts for research assistance
- **SSE Transport**: Real-time communication through Server-Sent Events

## Available MCP Components

### MCP Tools

#### `search_papers(topic: str, max_results: int = 10) -> List[str]`
Search arXiv for papers on a specific topic and store their metadata locally.
- `topic`: The research topic to search for
- `max_results`: Maximum number of results to return (default: 10)
- Returns: List of paper IDs found in the search
- **Storage**: Creates topic-specific directories and saves metadata to `papers_info.json`

#### `extract_info(paper_id: str) -> str`
Retrieve detailed information about a specific paper by its arXiv ID.
- `paper_id`: The arXiv paper ID to look up
- Returns: JSON string with complete paper details or error message if not found
- **Search**: Searches across all topic directories to find the paper

### MCP Resources

#### `papers://folders`
Dynamic resource that lists all available topic folders.
- Returns: Markdown-formatted list of all topics with saved papers
- **Usage**: Provides an overview of all research areas with stored papers

#### `papers://{topic}`
Dynamic resource for accessing papers within a specific topic.
- `topic`: The research topic to retrieve papers for
- Returns: Detailed markdown with all papers in the topic including titles, authors, summaries, and PDF links
- **Format**: Comprehensive paper listings with metadata and abstracts

### MCP Prompts

#### `generate_search_prompt(topic: str, num_papers: int = 10) -> str`
Generate a structured research prompt for AI-assisted paper analysis.
- `topic`: The research topic for the prompt
- `num_papers`: Number of papers to include in the search (default: 10)
- Returns: Comprehensive prompt for systematic paper research and analysis
- **Features**: Includes instructions for search, analysis, and synthesis

## Project Structure

```
.
├── README.md          # This documentation file
├── pyproject.toml     # Project metadata and dependencies
├── main.py            # Simple entry point (placeholder)
├── research_server.py # Main FastMCP server implementation
└── papers/            # Directory for storing paper metadata (created at runtime)
    └── {topic}/       # Each topic gets its own directory
        └── papers_info.json  # Paper metadata for the topic
```

### Key Files

- **`research_server.py`**: Main server implementation using FastMCP framework
  - Defines all MCP tools, resources, and prompts
  - Handles arXiv API integration
  - Manages local file storage
  - Runs on port 8001 with SSE transport

- **`main.py`**: Simple placeholder entry point
  - Currently contains basic "Hello" message
  - Can be extended for additional functionality

- **`pyproject.toml`**: Project configuration
  - Minimal dependencies: `arxiv>=2.2.0` and `mcp>=1.7.1`
  - Python 3.10+ requirement
  - Project metadata and build configuration

## Installation and Setup

### Prerequisites
- Python 3.10 or higher
- pip package manager

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mcp-arXiv-server.git
   cd mcp-arXiv-server
   ```

2. **Install dependencies**:
   ```bash
   pip install -e .
   ```

3. **Run the server**:
   ```bash
   python research_server.py
   ```

   The server will start on `http://localhost:8001` with SSE transport enabled.

### Dependencies

The project has minimal dependencies as defined in `pyproject.toml`:

- **`arxiv>=2.2.0`**: Official arXiv API client for paper search and retrieval
- **`mcp>=1.7.1`**: Model Context Protocol framework for tool integration

### Storage

- **Local Storage**: Paper metadata is stored in local JSON files under the `papers/` directory
- **Organization**: Each research topic gets its own subdirectory
- **Persistence**: Data persists between server restarts when running locally
- **Format**: Structured JSON with paper titles, authors, summaries, PDF URLs, and publication dates

## Usage Examples

### Searching for Papers
```python
# Search for machine learning papers
result = search_papers("machine learning", max_results=5)
# Returns: ['2301.12345', '2302.67890', ...]
```

### Retrieving Paper Information
```python
# Get details for a specific paper
info = extract_info("2301.12345")
# Returns: JSON string with paper metadata
```

### Browsing Topics
```python
# List all available topics
folders = get_available_folders()
# Returns: Markdown list of topic directories

# Get all papers in a topic
papers = get_topic_papers("machine_learning")
# Returns: Detailed markdown with all papers in the topic
```

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
