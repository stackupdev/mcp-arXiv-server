# Welcome to the MCP arXiv Server!

This project helps you search for and organize research papers from arXiv with just a few clicks. It’s designed to be simple, friendly, and easy to use online.

## What does this site do?
- Lets you search for research papers on any topic from arXiv.
- Saves and organizes the papers you find, so you can look them up later.
- Shows a friendly homepage when you visit the main website.
- Works with special tools that use the "MCP" protocol for advanced users.

## How do I use it?
You can put this project online using [Render.com](https://render.com/):
1. Upload your code to GitHub.
2. On Render.com, create a new "Web Service" and connect your GitHub.
3. Render.com will set everything up for you—just make sure the port is set to `8001`.
4. When it’s ready, visit your new website link (like `https://your-app-name.onrender.com/`).

## What will I see?
- **Homepage (`/`)**: A welcome page that explains what the project does.
- **/sse**: A special page for connecting with other tools (you can ignore this unless you know you need it).

## What happens when I search for papers?
When you use the search feature (through the MCP protocol or connected tools), the server will:
- Look up the latest papers from arXiv on your chosen topic
- Save the results so you can find them again later
- Let you view info about each paper, like title, authors, summary, and download link

## Project files
- `research_server.py`: The main code that runs the server
- `pyproject.toml` and `uv.lock`: These keep track of which packages are needed
- `README.md`: This guide

## Need help?
If you’re stuck or have questions, ask the person who shared this project with you, or check the code for more details.

---

Enjoy exploring research papers with MCP arXiv Server!
## License
MIT (or specify your license)
