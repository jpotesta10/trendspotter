trend_list = []

trend_list = [1, 2, 3, 4, 5]


#replace num at later step, return with object path URL

import requests
from bs4 import BeautifulSoup

def get_trending_urls(niche):
    # Specify the URL of a website relevant to the niche
    url = f'https://example.com/{niche}/trending'

    # Make an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the URLs from the parsed HTML (adjust based on website structure)
        urls = [a['href'] for a in soup.find_all('a', href=True)]

        return urls
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")
        return []

def main():
    # Input the niche for which you want to find trending URLs
    niche = input("Enter the niche: ")

    # Get the trending URLs for the specified niche
    trending_urls = get_trending_urls(niche)

    # Display the results
    if trending_urls:
        print(f"Top URLs trending in the {niche} niche:")
        for index, url in enumerate(trending_urls, start=1):
            print(f"{index}. {url}")
    else:
        print("No trending URLs found for the specified niche.")

if __name__ == "__main__":
    main()


