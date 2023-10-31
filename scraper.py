import requests
from bs4 import BeautifulSoup
from database_manager import insert_data
from fuzzywuzzy import process

BASE_URL = "https://www.liveaquaria.com"
START_URLS = [
    "/category/830/freshwater-fish",
    "/category/1075/freshwater-inverts",
    "/category/768/freshwater-plants",
    "/category/15/marine-fish",
    "/category/497/marine-invert-plant"
]

EXPECTED_LABELS = ['Common Name', 'Scientific Name', 'Care Level', 'Temperament', 'Color Form', 'Diet', 'Water Conditions', 'Max. Size', 'Family', 'Minimum Tank Size', 'Price']

def map_labels(labels):
    mapped_labels = {}
    for label in labels:
        best_match, score = process.extractOne(label, EXPECTED_LABELS)
        if score > 80:  # Adjust this threshold as needed
            mapped_labels[label] = best_match
    return mapped_labels

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data from the page
    data_labels = [label.text.strip() for label in soup.select(".productQuickStatsLabel")]
    data_values = [value.text.strip() for value in soup.select(".productQuickStatsValue")]

    label_mapping = map_labels(data_labels)

    data = {}
    for label, value in zip(data_labels, data_values):
        mapped_label = label_mapping.get(label)
        if mapped_label:
            data[mapped_label] = value

    # Additional data extraction can be added here

    insert_data(data)

def main():
    for start_url in START_URLS:
        response = requests.get(BASE_URL + start_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract links to individual fish/invertebrate/plant pages
        product_links = [a['href'] for a in soup.select(".product a")]

        for link in product_links:
            scrape_data(BASE_URL + link)

if __name__ == "__main__":
    main()
