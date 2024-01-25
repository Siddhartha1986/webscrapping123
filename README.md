

# Amazon Product Scraper ( webscrapping123 )

## Overview
This Python script is designed to scrape product information from Amazon search results. It targets a specific product category (currently set to 'phones'), extracts key details such as product names, ratings, rating counts, prices, and product URLs, and saves this information into an Excel file. This script can be particularly useful for data analysis, price tracking, or market research purposes.

## Features
- Scrapes product details from Amazon search results.
- Extracts product name, rating, rating count, price, and URL.
- Saves data in a structured Excel file.
- Easy to modify for different search queries.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Libraries: `requests`, `bs4` (BeautifulSoup), `pandas`

You can install these libraries using pip:
```bash
pip install requests beautifulsoup4 pandas
```

## Usage
1. **Setting the Search Query**: Modify the `search_query` variable in the script to search for different products. For example, replace `'phone'` with `'laptop'` to scrape data for laptops.

2. **Running the Script**: Execute the script in your Python environment. The script will scrape data from the first 4 pages of Amazon search results for the given query.

3. **Output File**: After successful execution, the script generates an Excel file named after the search query (e.g., `phone.xlsx`). This file contains the scraped product information.

## Code Structure
- The script uses `requests` to send HTTP requests to Amazon.
- `BeautifulSoup` from `bs4` is employed for parsing HTML content.
- `pandas` is used for creating and exporting a DataFrame.
- The script includes a `sleep` function to mimic human browsing and avoid being blocked by Amazon.

## Note
- Web scraping should be done responsibly and in accordance with the website's terms of service.
- Ensure you have the legal right to scrape and use the data you collect.

## Contribution
Feel free to fork this repository and contribute to its improvement. Whether it's adding new features, improving the existing code, or fixing bugs, your contributions are welcome!

## License
[MIT License](LICENSE)
