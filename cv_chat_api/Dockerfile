FROM ubuntu:22.04
# Install uv
RUN apt-get update
RUN apt-get install -y curl ca-certificates
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
RUN uv python install 3.14
# Set working directory
WORKDIR /app
# Copy requirements file
COPY pyproject.toml uv.lock /app/
# Install dependencies
RUN uv sync
COPY . /app/
# Expose port
EXPOSE 8000
# Start the FastAPI server
CMD ["ls"]
CMD ["uv", "run", "python", "main.py"]
