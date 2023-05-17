import requests
from bs4 import BeautifulSoup
import json

def count_words(url):
    # Fetch the webpage content
    response = requests.get(url)
    content = response.text

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')

    # Find all text content within the HTML
    text = soup.get_text()

    # Split the text into words
    words = text.split()

    # Count the occurrence of each word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Convert the word count dictionary to JSON
    result = json.dumps(word_count, indent=4)

    return result
url = 'https://9690-cheeku.github.io/My_Portfolio/'
output = count_words(url)
print(output)
