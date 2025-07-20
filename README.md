# Welcome to the MCP arXiv Server!

This is an easy-to-use online tool that helps you search for and manage research papers from arXiv. You can use it to find papers on any topic and keep track of what you discover.

## What does this project do?
- Lets you search arXiv for interesting research papers
- Helps you organize and retrieve paper information
- Works with tools that use the "MCP" protocol
- Shows a simple welcome page when you visit the website

## How do I use it?
You can run this project on [Render.com](https://render.com/), a service that makes it simple to put your project online.

### Steps to get started:
1. **Put your project on GitHub.**
   - If you haven't already, upload your code to a GitHub repository.

2. **Set up on Render.com:**
   - Go to the Render.com website and log in.
   - Click "New Web Service" and connect your GitHub account.
   - Choose your project repository.
   - You don't need to change any build settings—Render will use the included Dockerfile.
   - Make sure the port is set to `8001`.
   - Click "Create Web Service" and wait for your site to go live!

3. **Visit your new site:**
   - Once it's ready, go to the link Render.com gives you (it will look like `https://your-app-name.onrender.com/`).
   - The homepage will greet you and tell you about the project.
   - The special `/sse` page is for connecting with other tools (you don't need to use this unless you know what MCP is).

## Need help?
If you have any questions or need help, check with the person who shared this project or look at the code for more details.

## Files in this project
- `research_server.py`: The main code for the server
- `pyproject.toml`, `uv.lock`: These help manage which packages the project needs
- `README.md`: This file!

## License
MIT (or add your own license)
## License
MIT (or specify your license)
