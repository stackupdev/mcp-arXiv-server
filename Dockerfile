FROM python:3.11-slim
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv pip install --system .
COPY main.py research_server.py ./
EXPOSE 8001
CMD ["python", "main.py"]