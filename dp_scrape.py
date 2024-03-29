import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from fake_useragent import UserAgent


def get_scrape_data(url):
    user_agent = UserAgent()
    headers = {'User-Agent': user_agent.random}
    response = requests.get(url, headers=headers)

    

    if response.status_code == 200:
        html_text = response.text
        soup = BeautifulSoup(html_text, 'html.parser')

        tags_list = ['div', 'span', 'p', 'a', 'ul', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        text_list = []
        for tag in tqdm(soup.find_all(tags_list), desc='Extracting Text', unit='tags'):
            text_list.append(tag.get_text())

        text = ' '.join(text_list)

        return text

    else:
        print(f"Error: Unable to fetch content from {url}. Status code: {response.status_code}")
        return None
    

my_url = fetch(locals)
scraped_text = get_scrape_data(my_url)

if scraped_text:
    print(f"Scraped Text : {scraped_text}")
else:
    print("Failed to Scrape")
