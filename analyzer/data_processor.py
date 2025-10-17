from collections import defaultdict
import datetime
# Optional: import pandas as pd
# Optional: import matplotlib.pyplot as plt

def summarize_commits(commits_data):
    """
    Processes raw commit data to get commit count by author and date.
    
    Args:
        commits_data (list): List of commit objects from the GitHub API.
        
    Returns:
        dict: Summary including total commits, commits per author, etc.
    """
    if not commits_data:
        return {"total_commits": 0, "authors": {}}

    authors = defaultdict(int)
    
    for commit in commits_data:
        author_info = commit.get('author')
        if author_info:
            author_login = author_info.get('login', 'Unknown')
        else:
            # Fallback for commits without a GitHub account link
            author_login = commit['commit']['author']['name']
            
        authors[author_login] += 1
    
    # Sort authors by commit count
    sorted_authors = dict(sorted(authors.items(), key=lambda item: item[1], reverse=True))

    return {
        "total_commits": len(commits_data),
        "authors_by_commits": sorted_authors,
        # Add more features here, e.g., commits over time, first/last commit date
    }

def summarize_languages(languages_data):
    """
    Converts language byte data into percentages.
    
    Args:
        languages_data (dict): Dictionary of {language: bytes_of_code}.
        
    Returns:
        dict: Dictionary of {language: percentage}.
    """
    if not languages_data:
        return {}
        
    total_bytes = sum(languages_data.values())
    
    # Calculate percentage for each language
    percentages = {
        lang: (bytes_val / total_bytes) * 100
        for lang, bytes_val in languages_data.items()
    }
    
    # Sort by percentage
    return dict(sorted(percentages.items(), key=lambda item: item[1], reverse=True))

# In a full project, you'd add functions here for visualization (if using matplotlib)