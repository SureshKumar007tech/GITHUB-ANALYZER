import sys
from analyzer.github_api import fetch_data, fetch_languages
from analyzer.data_processor import summarize_commits, summarize_languages

def display_summary(summary):
    """Prints the analyzed data to the console."""
    print("\n==============================")
    print(f" TOTAL COMMITS: {summary['total_commits']}")
    print("==============================")
    
    print("\n--- COMMIT AUTHORS ---")
    for author, count in summary['authors_by_commits'].items():
        print(f"{author:<20}: {count} commits")

def display_languages(languages):
    """Prints the language usage percentages."""
    print("\n--- LANGUAGE BREAKDOWN ---")
    if not languages:
        print("No language data found.")
        return
        
    for lang, percent in languages.items():
        # Display percentage rounded to two decimal places
        print(f"{lang:<15}: {percent:.2f}%")
    print("--------------------------")

def run_analysis(owner, repo):
    """Fetches and processes all data for the given repository."""
    print(f"🔍 Starting analysis for GitHub repository: {owner}/{repo}")
    
    # 1. Fetch Commit Data
    raw_commits = fetch_data(owner, repo, endpoint="commits")
    if raw_commits:
        commit_summary = summarize_commits(raw_commits)
        display_summary(commit_summary)
    else:
        print("Could not retrieve commit data.")
        
    # 2. Fetch Language Data
    raw_languages = fetch_languages(owner, repo)
    if raw_languages:
        language_summary = summarize_languages(raw_languages)
        display_languages(language_summary)
    else:
        print("Could not retrieve language data.")
        
    print("\n✅ Analysis complete.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <owner_username> <repository_name>")
        print("Example: python main.py google python-requests")
        sys.exit(1)
        
    OWNER = sys.argv[1]
    REPO = sys.argv[2]
    
    run_analysis(OWNER, REPO)