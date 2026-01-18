FROM ubuntu:22.04
# Install uv
RUN apt-get update
RUN apt-get install -y curl ca-certificates
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
# Set working directory
WORKDIR /app
# Copy requirements file
COPY pyproject.toml uv.lock /app/
# Install dependencies
RUN uv install --no-dev
# Copy application code
COPY . /app
# Expose port
EXPOSE 80000
# Start the application
CMD ["uv", "run", "main:app"]