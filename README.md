# Pondok Data Web Scraper

## Purpose:
This project aims to scrape data about Pondok (Islamic boarding schools) in the Kelantan region from the website [http://yayasanpondok.blogspot.com/p/senarai-pondok-di-kelantan.html]. The scraped data is then cleaned and organized into a CSV file.

## Data Extracted:

- Pondok Name
- Mudir (Principal) Contact Information
- Address and Other Relevant Details

## Dependencies:

- Python
- BeautifulSoup
- Pandas

## Usage:

1. **Clone the Repository**:

    ```Bash
    git clone <your_repository_url>
    ```

2. **Install Dependencies**:

    ```Bash
    pip install beautifulsoup4 pandas
    ```

3. **Run the Script**:

    ```Bash
    python main.py
    ```

4. **View the Output**: The scraped data will be saved as a CSV file named ```pondok_data_detailed.csv```. You can open this file using a spreadsheet application like Excel or Google Sheets.

## Data Cleaning:

The script performs basic data cleaning to remove rows with missing or incomplete information.

## Note:

Ensure you have a stable internet connection to avoid errors during the scraping process.
The website's structure may change, potentially affecting the scraper's functionality. Regular updates may be necessary to maintain compatibility.

## Contributing:

If you'd like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request.
