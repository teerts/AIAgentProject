# AI Coding Agent
This agent uses Google's Gemini AI model to understand natural language requests and perform file operations, code execution, and project management tasks.

## Features

- **File Management**: List, read, and write files in your project directory
- **Code Execution**: Run Python scripts with optional arguments
- **Natural Language Interface**: Describe what you want in plain English
- **Autonomous Operation**: The agent plans and executes multiple steps to complete complex tasks
- **Safety**: All operations are contained within the specified working directory -- VERY IMPORTANT. 

## Prerequisites

- Python 3.7 or higher
- Google Gemini API key
- Required Python packages (see Installation)

## Installation

1. Clone or download this project
2. Install required dependencies:
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. Ensure you have a `calculator` directory in your project root (or modify the `working_directory` variable in `main.py`)

## Usage

### Basic Usage

```bash
python3 main.py "Your request here"
```

### Verbose Mode

To see detailed information about function calls and token usage:

```bash
python3 main.py "Your request here" --verbose
```

### Example Commands

Here are some example requests you can make:

```bash
# File operations
python3 main.py "List all files in the calculator directory"

# Code execution
python3 main.py "Execute test.py with arguments '--verbose'"

# Code modification
python3 main.py "Add error handling to the divide function in calculator.py"

# Complex tasks
python3 main.py "Build a command-line calculator that can handle basic arithmetic operations"

```

## Available Functions

The AI agent can perform the following operations:

### File Operations
- **List Files**: View directory contents and file information
- **Read Files**: Get the content of specific files
- **Write Files**: Create new files or overwrite existing ones

### Code Execution
- **Run Python**: Execute Python scripts with optional command-line arguments

## How It Works

1. **Natural Language Processing**: The agent processes your request using Google's Gemini model
2. **Function Planning**: It creates a plan of which functions to call and in what order
3. **Execution**: The agent executes the planned functions step by step
4. **Iteration**: It can make up to 20 function calls to complete complex tasks
5. **Response**: Finally, it provides a summary of what was accomplished

## Configuration

### Working Directory
By default, the agent operates in the `./calculator` directory. You can change this by modifying the `working_directory` variable in `main.py`:

```python
working_directory = "./your_project_directory"
```

### Model Selection
The agent uses `gemini-2.0-flash-001` by default. You can change this by modifying the `model` variable in `main.py`.

## Safety Features

- All file operations are restricted to the specified working directory
- Function calls are validated before execution
- Error handling prevents crashes from invalid operations
- Maximum iteration limit prevents infinite loops

## Troubleshooting

### Common Issues

**"Unknown function" error**: This indicates an internal error with function registration. Check that all function modules are properly imported.

**API Key errors**: Ensure your `GEMINI_API_KEY` is correctly set in your `.env` file.

**Permission errors**: Make sure the script has read/write permissions for the working directory.

