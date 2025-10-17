# 📊 GitHub Repository Analyzer

A Python command-line tool designed to fetch data from the GitHub API and generate simple statistical summaries for any public repository.

## ✨ Features
* **Commit Analysis:** Calculate total commits and commits per contributor.
* **Language Breakdown:** Determine the percentage usage of all programming languages in the repository.
* **Command-Line Interface:** Easy execution by passing the owner and repository name as arguments.

## 🛠️ Setup

1.  **Clone the repository:**
    ```bash
    git clone [Your-Repo-URL]
    cd github-analyzer
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Run the script using the repository owner's username and the repository name:

```bash
python main.py <owner_username> <repository_name>