FROM python:3.11.4-slim

# Install system dependencies for Node.js and poetry
RUN apt-get update && apt-get install -y nodejs npm
RUN pip install poetry
RUN poetry config virtualenvs.create false --local

WORKDIR /usr/src/app
# Copy the rest of the codebase
COPY . .

# Debugging: Print the contents of pyproject.toml
RUN cat pyproject.toml

# Debugging: Print the Poetry configuration
RUN poetry config --list

# Copy only the files needed for dependency installation
RUN poetry install

# Debugging: Print the installed packages
RUN pip freeze

# Set the working directory for the React application
WORKDIR /usr/src/app/ui
RUN npm install
RUN npm run build

# Set the working directory back to the main application
WORKDIR /usr/src/app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["tail", "-f", "/dev/null"]
