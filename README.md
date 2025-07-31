# MCP arXiv Server

A FastMCP-based backend service for searching, organizing, and managing arXiv research papers. This project provides a simple interface to search for academic papers, store their metadata, and retrieve them by topic or paper ID.

## What is this project?
This server provides programmatic access to arXiv papers through a set of MCP-compatible tools. It allows you to:
- Search for papers on any topic
- Temporarily store paper metadata (note: data may be lost on server restart)
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
- **Temporary Storage**: Note that on Render.com's free tier, stored data may be lost when the server restarts

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
