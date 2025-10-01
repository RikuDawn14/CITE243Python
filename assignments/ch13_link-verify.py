# Given the URL of a web page, will find every <a> link.
"""
===========================================================
Program Name: ch13 link verify
Author: Matthew Balthaser
Date: 2025-09-28
Description:
    This program converts given the URL of a web page, will find every <a> link on the page.
    It is designed to test whether the linked URL results in a “404 Not Found” status code.
    
Usage:
    Run the script using Python 3.13.7. Ensure all dependencies
    are installed before execution.

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

### Start of program ###
print("=" * 60)
print("Link Verification".center(60))
print("=" * 60)

while True:
    
    url = input("\nPlease enter a URL to check.\n => ").strip()
    

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as exc:
        print(f'There was a problem: {exc}')
    
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a', href=True)

    print(f"Found {len(links)} links. Checking for broken ones...")
    time.sleep(1)

    broken_links = []

    for link in links:
        href = link['href']
        full_url = urljoin(url, href)

        # Skip links like mailto:, javascript:, etc.
        parsed = urlparse(full_url)
        if parsed.scheme not in ('http', 'https'):
            continue

        try:
            head = requests.head(full_url, allow_redirects=True, timeout=10)
            if head.status_code == 404:
                broken_links.append(full_url)
                print(f"Broken link: {full_url}")
        except requests.RequestException:
            broken_links.append(full_url)
            print(f"Could not reach: {full_url}")

    print(f"\nDone. Found {len(broken_links)} broken link(s).")