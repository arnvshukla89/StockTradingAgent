FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock* /app/

# Install Poetry
RUN pip install poetry

# Install dependencies
RUN poetry install --no-root --no-dev

# Copy the source code
COPY src/ /app/src/

# Expose the port for the FastAPI application
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "src/trading_agent/api.main:app", "--host", "0.0.0.0", "--port", "8000"]