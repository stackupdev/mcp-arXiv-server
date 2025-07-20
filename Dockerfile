FROM python:3.11-slim
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv pip install --system .
COPY research_server.py .
EXPOSE 8001
CMD ["uvicorn", "research_server:app", "--host", "0.0.0.0", "--port", "8001"]