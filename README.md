
# GitHub Commit Analyzer

The GitHub Commit Analyzer is a Python script designed to fetch and analyze commit messages from a specified GitHub repository. It categorizes commit messages according to conventional commit types and outputs the results in both console and CSV format.

## Features

- Fetches commits directly from GitHub using the GitHub API.
- Analyzes commit messages to classify them based on conventional commit types.
- Outputs the analysis results to the console and a CSV file.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6 or higher
- `requests` library
- `python-dotenv` library for managing environment variables

You will also need a GitHub token with appropriate permissions to access repository data. This token should be stored in an `.env` file for security.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install Required Python Libraries:**

   You can install the required libraries using pip:

   ```bash
   pip install requests python-dotenv
   ```

3. **Set Up Environment Variables:**

   Create a `.env` file in the root directory of the project and add your GitHub token:

   ```plaintext
   GITHUB_TOKEN=your_github_token_here
   ```

## Configuration

Open the script and modify the following lines in the `REPOSITORY_OWNER` and `REPOSITORY_NAME` constants to point to the repository you wish to analyze:

```python
REPOSITORY_OWNER = "<repository-owner-username>"
REPOSITORY_NAME = "<repository-name>"
```

## Usage

To run the script, use the following command from the root of your project directory:

```bash
python commit_analyzer.py
```

The script will fetch commit data from the specified repository, analyze it, and print the results to the console. It will also save the results to a CSV file named `commit_types.csv` in the root directory.

## Output

The script outputs the count of each type of commit found in the analyzed commits, both on the console and in the CSV file with columns "Commit Type" and "Count".
