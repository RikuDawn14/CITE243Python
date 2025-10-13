# Given the URL of a web page, will find every <a> link.

"""
===========================================================
Description:
    This program takes a URL and finds every <a> link on the page.
    It tests whether each linked URL results in a "404 Not Found" 
    or other error status codes.
Usage:
    Run the script using Python 3.13.7 Ensure requests and 
    beautifulsoup4 are installed:
    pip install requests beautifulsoup4
===========================================================
"""

# Take user input for URL.
# Verify URL is valid.
# Find every <a> link on page.
# Test pages.
# Return any links that are broken.

import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from typing import List, Tuple

def validate_url(url: str) -> bool:
    """Validate that the URL has a proper scheme and netloc."""
    parsed = urlparse(url)
    return bool(parsed.scheme in ('http', 'https') and parsed.netloc)

def fetch_page(url: str) -> Tuple[bool, str, requests.Response]:
    """Fetch the page and return success status, message, and response."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return True, "Success", response
    except requests.exceptions.Timeout:
        return False, "Request timed out", None
    except requests.exceptions.ConnectionError:
        return False, "Could not connect to server", None
    except requests.exceptions.HTTPError as e:
        return False, f"HTTP error: {e}", None
    except Exception as e:
        return False, f"Unexpected error: {e}", None

def check_link(full_url: str) -> Tuple[str, int, str]:
    """
    Check if a link is broken.
    Returns: (url, status_code, status_message)
    """
    try:
        head = requests.head(full_url, allow_redirects=True, timeout=10)
        # Some servers don't respond to HEAD, try GET if HEAD fails
        if head.status_code == 405 or head.status_code >= 500:
            head = requests.get(full_url, allow_redirects=True, timeout=10, stream=True)
        return full_url, head.status_code, "OK" if head.status_code < 400 else "Broken"
    except requests.exceptions.Timeout:
        return full_url, 0, "Timeout"
    except requests.exceptions.ConnectionError:
        return full_url, 0, "Connection Error"
    except requests.exceptions.TooManyRedirects:
        return full_url, 0, "Too Many Redirects"
    except Exception as e:
        return full_url, 0, f"Error: {str(e)[:50]}"

def extract_links(url: str, html: str) -> List[str]:
    """Extract all valid HTTP(S) links from the HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a', href=True)
    
    valid_links = []
    for link in links:
        href = link['href']
        full_url = urljoin(url, href)
        
        # Skip non-HTTP(S) links
        parsed = urlparse(full_url)
        if parsed.scheme in ('http', 'https'):
            valid_links.append(full_url)
    
    return valid_links

def main():
    """Main program loop."""
    print("=" * 60)
    print("Link Verification Tool".center(60))
    print("=" * 60)
    print("\nThis tool checks all links on a web page for broken URLs.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    while True:
        url = input("Please enter a URL to check:\n => ").strip()
        
        # Allow user to exit
        if url.lower() in ('quit', 'exit', 'q'):
            print("\nGoodbye!")
            break
        
        # Validate URL format
        if not validate_url(url):
            print("Invalid URL. Please include http:// or https://\n")
            continue
        
        print(f"\nFetching page: {url}")
        success, message, response = fetch_page(url)
        
        if not success:
            print(f"Failed to fetch page: {message}\n")
            continue
        
        # Extract links
        links = extract_links(url, response.text)
        unique_links = list(set(links))  # Remove duplicates
        
        print(f"Found {len(links)} total links ({len(unique_links)} unique)")
        print(f"Checking for broken links...\n")
        time.sleep(0.5)
        
        # Check each link
        broken_links = []
        working_links = []
        
        for i, link in enumerate(unique_links, 1):
            print(f"Checking {i}/{len(unique_links)}: {link[:60]}...", end='\r')
            
            full_url, status_code, status = check_link(link)
            
            if status_code >= 400 or status_code == 0:
                broken_links.append((full_url, status_code, status))
            else:
                working_links.append(full_url)
        
        # Clear the progress line
        print(" " * 80, end='\r')
        
        # Display results
        print("\n" + "=" * 60)
        print("RESULTS".center(60))
        print("=" * 60)
        print(f"Working links: {len(working_links)}")
        print(f"Broken links: {len(broken_links)}")
        
        if broken_links:
            print("\nBroken Links Found:")
            print("-" * 60)
            for url, code, status in broken_links:
                if code > 0:
                    print(f"[{code}] {url}")
                else:
                    print(f"[{status}] {url}")
        else:
            print("\nAll links are working!")
        
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main()