import requests
import pandas as pd

# Set your API key and test URLs
API_KEY = "AIzaSyCwzJiO6yXzHbfJQQoTz8_ODdViS2gtBmc"  # Replace with your actual API Key
URLS = ["https://ktxglobal.com/", "https://ktxglobal.com/organisers.php"]  # Add more URLs as needed
EXCEL_FILE = "pagespeed_metrics.xlsx"

def fetch_pagespeed_metrics(url):
    """Fetch PageSpeed Insights data for a given URL."""
    endpoint = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
    params = {
        "url": url,
        "key": API_KEY,
        "strategy": "mobile"  # Change to "desktop" if needed
    }
    
    response = requests.get(endpoint, params=params)
    data = response.json()
    
    # Extract key metrics (Modify based on your needs)
    lighthouse_result = data.get("lighthouseResult", {}).get("categories", {})
    
    return {
        "URL": url,
        "Performance Score": lighthouse_result.get("performance", {}).get("score", None),
        "First Contentful Paint (s)": data["lighthouseResult"]["audits"]["first-contentful-paint"]["numericValue"] / 1000,
        "Largest Contentful Paint (s)": data["lighthouseResult"]["audits"]["largest-contentful-paint"]["numericValue"] / 1000,
        "Total Blocking Time (ms)": data["lighthouseResult"]["audits"]["total-blocking-time"]["numericValue"],
        "Cumulative Layout Shift": data["lighthouseResult"]["audits"]["cumulative-layout-shift"]["numericValue"],
        "Speed Index (s)": data["lighthouseResult"]["audits"]["speed-index"]["numericValue"] / 1000,
    }

# Fetch data for all URLs
results = [fetch_pagespeed_metrics(url) for url in URLS]

# Convert to DataFrame and save to Excel
df = pd.DataFrame(results)
df.to_excel(EXCEL_FILE, index=False)

print(f"PageSpeed Insights metrics saved to {EXCEL_FILE}")
