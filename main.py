import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_pondok_list(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    pondok_links = soup.select('div.post-body.entry-content ol li a')

    return [(link.text.strip(), link['href']) for link in pondok_links]


def extract_key_value_pairs(text):
    # Split the text into lines
    lines = text.split('\n')
    data = {}
    current_key = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Check if the line is a key (ends with a colon)
        if line.endswith(':'):
            current_key = line[:-1].strip()
            data[current_key] = ""
        elif current_key:
            # If we have a current key, this line is a value
            data[current_key] += " " + line if data[current_key] else line

    return data


def scrape_pondok_details(url, name):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    details = soup.select_one('div.post-body.entry-content')

    if details:
        content = details.get_text(separator='\n')
        data = extract_key_value_pairs(content)
        data['Name'] = name
        data['URL'] = url
    else:
        data = {'Name': name, 'URL': url, 'Error': 'Details not found'}

    return data


def main():
    base_url = 'http://yayasanpondok.blogspot.com/p/senarai-pondok-di-kelantan.html'

    pondok_links = scrape_pondok_list(base_url)

    all_pondok_data = []

    for name, link in pondok_links:
        print(f"Scraping data for: {name}")
        pondok_data = scrape_pondok_details(link, name)
        all_pondok_data.append(pondok_data)
        time.sleep(1)  # Be polite, wait a second between requests

    # Create a DataFrame
    df = pd.DataFrame(all_pondok_data)

    # Reorder columns to put Name and URL first
    cols = ['Name', 'URL'] + [col for col in df.columns if col not in ['Name', 'URL']]
    df = df[cols]

    # Display the DataFrame
    print("\nScraped Data:")
    print(df)

    # Display more detailed information
    print("\nDataFrame Info:")
    df.info()

    print("\nDataFrame Description:")
    print(df.describe(include='all'))

    # Save to CSV
    df.to_csv('pondok_data_detailed.csv', index=False)
    print("\nData saved to pondok_data_detailed.csv")


if __name__ == "__main__":
    main()