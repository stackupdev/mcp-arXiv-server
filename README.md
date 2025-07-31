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

- **`main.py`**: Application entry point
  - Handles server startup and shutdown
  - Provides user-friendly messages and error handling
  - Imports and runs the FastMCP server from `research_server.py`

- **`research_server.py`**: Server implementation using FastMCP framework
  - Defines all MCP tools, resources, and prompts
  - Handles arXiv API integration
  - Manages local file storage
  - Exports the `mcp` server instance for use by `main.py`

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
   python main.py
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

## How to Use the MCP Server

This is an MCP (Model Context Protocol) server that provides tools, resources, and prompts to AI assistants like Claude. Here's how it works:

### 1. Start the Server
```bash
python main.py
```
The server will start on `http://localhost:8001` and be ready to receive MCP requests.

### 2. Connect an MCP Client
The server exposes its functionality through the MCP protocol. AI assistants or MCP clients can connect to use the tools.

### 3. Available Functionality

#### **MCP Tools** (called by AI assistants)
- `search_papers(topic, max_results)` - Search and store papers on a topic
- `extract_info(paper_id)` - Get details about a specific paper

#### **MCP Resources** (accessed via URI)
- `papers://folders` - Browse all available topic folders
- `papers://machine_learning` - View all papers in the "machine learning" topic
- `papers://quantum_computing` - View all papers in the "quantum computing" topic

#### **MCP Prompts** (generate research instructions)
- `generate_search_prompt(topic, num_papers)` - Create structured research prompts

### 4. Example Workflow
1. **Search**: AI assistant calls `search_papers("quantum computing", 10)`
2. **Store**: Papers are automatically saved to `papers/quantum_computing/papers_info.json`
3. **Browse**: Access `papers://quantum_computing` resource to view all papers
4. **Retrieve**: Use `extract_info("2301.12345")` to get specific paper details

### 5. Data Storage
- Papers are organized in topic-based directories under `papers/`
- Each topic has a `papers_info.json` file with metadata
- Data persists between server restarts

## Integration with AI Assistants

This MCP server is designed to work with AI assistants that support the Model Context Protocol. When connected:

- **Tools**: The AI can search for papers and retrieve information
- **Resources**: The AI can browse your saved research topics and papers
- **Prompts**: The AI can generate structured research workflows

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
