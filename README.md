# CrewAI Project

This project is a crash course from Tyler AI on how to the use of CrewAI to create an AI agent that provides information about various topics.

## Prerequisites

- Python 3.9 or higher (tested with Python 3.12.9)
- pip (Python package installer)
- make (for using the Makefile)

## Installation

1. Clone this repository:
```bash
git clone <your-repository-url>
cd crew-ai-course
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up your OpenAI API key:
   - Get your API key from [OpenAI's platform](https://platform.openai.com/api-keys)
   - Replace the API key in `main.py` with your own key

## Running the Project

1. Make sure your virtual environment is activated:
```bash
source venv/bin/activate
```

2. Run the main script:
```bash
python main.py
```

The script will:
- Initialize an information agent
- Create a task about the blue-ringed octopus
- Execute the task and display the results

## Code Quality Tools

### Using the Makefile

This project includes a Makefile to simplify code quality tasks:

```bash
# Install dependencies including linting tools
make install

# Format code with Black
make format

# Lint code with Flake8
make lint

# Fix code with Autopep8
make fix

# Run all code quality tools
make quality

# Clean up Python cache files
make clean

# Show help
make help
```

### Code Quality Configuration

This project includes configuration files for code quality tools:

- `.flake8`: Configuration for Flake8 linting
  - Sets maximum line length to 120 characters
  - Excludes common directories like `__pycache__`, `venv`, etc.
  - Ignores specific error codes that are less critical
  - Sets maximum complexity to 10
  - Configures per-file ignores for tests and `__init__.py` files

### Manual Formatting and Linting

If you prefer to run the tools manually:

1. **Black** - The uncompromising code formatter:
```bash
# Format a single file
black main.py

# Format all Python files in the project
black .
```

2. **Flake8** - A wrapper around PyFlakes, pycodestyle, and McCabe:
```bash
# Check code style
flake8 main.py

# Check all Python files
flake8 .
```

3. **Autopep8** - A tool that automatically formats Python code to conform to the PEP 8 style guide:
```bash
# Format a single file
autopep8 --in-place --aggressive --aggressive main.py

# Format all Python files
autopep8 --in-place --aggressive --aggressive .
```

## Monitoring System Resources

### GPU Monitoring

To monitor GPU usage in real-time while running the project, open a separate terminal and run:
```bash
watch -n 1 nvidia-smi
```

This command will:
- Display GPU usage statistics
- Update every 1 second
- Show memory usage, power consumption, and running processes

### CPU Monitoring

To monitor CPU usage in real-time, open a separate terminal and run:
```bash
top
```

For a more user-friendly interface, you can use:
```bash
htop
```

These commands will:
- Display CPU usage statistics
- Show memory usage
- List running processes
- Update in real-time

## Project Structure

- `main.py`: Main script containing the CrewAI implementation
- `.vscode/settings.json`: VS Code/Cursor configuration for Python development
- `Makefile`: Contains commands for code quality tools
- `.flake8`: Configuration for Flake8 linting

## Note

Make sure to keep your API key secure and never commit it to version control. 
Consider using environment variables or a `.env` file for better security. 