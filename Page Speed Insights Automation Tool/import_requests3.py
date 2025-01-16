import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# PageSpeed API Key
API_KEY = "AIzaSyCwzJiO6yXzHbfJQQoTz8_ODdViS2gtBmc"

# Function to extract internal links
def get_internal_links(base_url):
    internal_links = set()
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for link in soup.find_all("a", href=True):
            url = link["href"]
            if url.startswith("/") or base_url in url:
                full_url = url if url.startswith("http") else base_url + url
                internal_links.add(full_url)
                
    except Exception as e:
        print(f"Error fetching links: {e}")
    
    return list(internal_links)

# Function to get PageSpeed Insights data
def get_pagespeed_metrics(url):
    api_url = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key={API_KEY}"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100  # Convert to percentage
        return score
    except Exception as e:
        print(f"Error fetching PageSpeed data for {url}: {e}")
        return None

# Main function
def main():
    base_url = input("https://ktxglobal.com/")
    links = get_internal_links(base_url)
    
    print(f"Found {len(links)} pages to test.")
    
    results = []
    for link in links:
        print(f"Testing {link}...")
        score = get_pagespeed_metrics(link)
        results.append({"URL": link, "Performance Score": score})
        time.sleep(2)  # To prevent API rate limits
    
    # Save to Excel
    df = pd.DataFrame(results)
    df.to_excel("PageSpeed_Results.xlsx", index=False)
    print("Results saved to PageSpeed_Results.xlsx")

if __name__ == "__main__":
    main()
