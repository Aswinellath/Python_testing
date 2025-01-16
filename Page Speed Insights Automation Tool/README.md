# Page Speed Insights Automation

## Overview
This tool automates the process of fetching Google PageSpeed Insights metrics for all pages of a given website. Instead of manually entering each URL, the script crawls the website, extracts all links, and then fetches speed insights for each page. The results are stored in an Excel sheet.

## Features
- Crawls the given website URL to find all internal pages
- Fetches Google PageSpeed Insights metrics for each page
- Saves the data into an Excel file for easy analysis

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.8+
- Google PageSpeed Insights API Key
- Required Python libraries:
  - `requests`
  - `pandas`
  - `beautifulsoup4`
  - `openpyxl`

## Installation

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/pagespeed-insights-automation.git
   cd pagespeed-insights-automation
```

2. **Create a virtual environment** (Recommended)
```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Set up your API Key**
   - Get a Google PageSpeed Insights API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Create a `.env` file and add:
     ```
     API_KEY=your_api_key_here
     ```

## Usage
Run the script with the main website URL:
```bash
   python main.py --url https://example.com
```

This will:
1. Crawl the website to find all internal links.
2. Fetch PageSpeed Insights data for each URL.
3. Store the results in an Excel file (`pagespeed_results.xlsx`).

## Future Improvements
- Support for multi-threading to speed up the scanning process
- Option to fetch mobile and desktop scores separately
- Generate visual reports for performance trends
- Web-based UI for easier access

## Contributing
Feel free to submit issues or contribute to the project via pull requests.

## License
MIT License

