import requests

GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}"

def fetch_data(owner, repo, endpoint="commits"):
    """
    Fetches data from a specific GitHub API endpoint (e.g., commits, contributors).
    
    Args:
        owner (str): The repository owner (username).
        repo (str): The repository name.
        endpoint (str): The specific API endpoint (e.g., 'commits', 'contributors').
        
    Returns:
        list or None: A list of data objects, or None on failure.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"
    
    # You might need to use a Personal Access Token (PAT) 
    # for higher rate limits, but we'll omit that for simplicity here.
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {endpoint} data for {owner}/{repo}: {e}")
        return None

def fetch_languages(owner, repo):
    """Fetches language usage for the repository."""
    url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json() # Returns a dictionary of {language: bytes_of_code}
    except requests.exceptions.RequestException as e:
        print(f"Error fetching language data: {e}")
        return None