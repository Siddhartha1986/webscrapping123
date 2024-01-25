import requests                  # Importing requests to send HTTP requests.
from bs4 import BeautifulSoup    # BeautifulSoup for parsing HTML and XML documents.
import pandas as pd              # Pandas for data manipulation and analysis.
from time import sleep           # Sleep to pause the execution for a given amount of time.

# Headers to mimic a browser visit and potentially avoid being blocked as a bot.
headers = {
 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
 'Accept-Language': 'en-US, en;q=0.5'
}

# Search query setup and base URL formation for Amazon search.
search_query = 'phone'.replace(' ','+')
base_url = f'https://www.amazon.com/s?k={search_query}'

items = []  # List to store scraped data.

# Looping through the first 4 pages of search results.
for i in range(1, 5):
    print(f'processing page {i}...{base_url}&page={i}')
    # Sending HTTP GET request to each search result page.
    response = requests.get(base_url + '&page={0}'.format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')  # Parsing the page content.
    
    # Finding all product items on the page.
    results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    
    # Iterating over each product item.
    for result in results:
        product_name = result.h2.text  # Extracting product name.

        try:
            # Extracting product rating and rating count.
            rating = result.find('i', {'class': 'a-icon'}).text
            rating_count = result.find_all('span', {'aria-label': True})[1].text
        except AttributeError:
            continue  # Skip if rating or rating count not found.

        try:
            # Extracting product price and URL.
            price1 = result.find('span', {'class': 'a-price-whole'}).text
            price2 = result.find('span', {'class': 'a-price-whole'}).text
            price = price1 + price2
            product_url = 'https://amazon.com' + result.h2.a['href']
            items.append([product_name, rating, rating_count, price, product_url])  # Appending data to the list.
        except AttributeError:
            continue  # Skip if price not found.

    sleep(1.5)  # Pause execution to mimic human browsing and avoid being blocked.

# Creating a DataFrame from the scraped data and exporting it to an Excel file.
df = pd.DataFrame(items, columns=['product', 'rating', 'rating count', 'price', 'product_url'])
print(df)
df.to_excel(f'{search_query}.xlsx')
