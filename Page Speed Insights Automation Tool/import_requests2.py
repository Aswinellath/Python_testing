import requests
import pandas as pd
from openpyxl import Workbook

# Define API key and base URL
API_KEY = "AIzaSyCwzJiO6yXzHbfJQQoTz8_Osdfsdfsdf2gtBmc"
BASE_URL = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

# List of URLs to analyze
URLS = [
    "https://samuhikpahal.org/",
    "https://samuhikpahal.org/organization-development/",
]

# Function to fetch PageSpeed Insights data
def get_pagespeed_data(url, strategy="mobile"):
    params = {
        "url": url,
        "key": API_KEY,
        "strategy": strategy,
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    # Extract required metrics
    try:
        performance_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
        lcp = data["lighthouseResult"]["audits"]["largest-contentful-paint"]["displayValue"]
        fcp = data["lighthouseResult"]["audits"]["first-contentful-paint"]["displayValue"]
        report_url = f"https://pagespeed.web.dev/analysis/{url.replace('https://', '').replace('/', '-')}"
    except KeyError:
        performance_score, lcp, fcp, report_url = None, None, None, None
    
    return performance_score, lcp, fcp, report_url

# Prepare data storage
results = []

# Fetch metrics for each URL
for url in URLS:
    mob_score, mob_lcp, mob_fcp, report_url = get_pagespeed_data(url, "mobile")
    desk_score, desk_lcp, desk_fcp, _ = get_pagespeed_data(url, "desktop")
    
    results.append([
        url, report_url, mob_score, mob_lcp, mob_fcp, desk_score, desk_lcp, desk_fcp
    ])

# Create DataFrame
columns = [
    "Page Url", "PageSpeed test report url", "Performance score (Mob)", "LCP(Mob)", "FCP(Mob)",
    "Performance score (Desk)", "LCP(Desk)", "FCP(Desk)"
]
df = pd.DataFrame(results, columns=columns)

# Save to Excel
EXCEL_FILE = "KTX_speed_test_output2.xlsx"
df.to_excel(EXCEL_FILE, index=False, engine='openpyxl')

print(f"Excel file '{EXCEL_FILE}' has been generated successfully.")
