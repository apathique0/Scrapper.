import requests
from bs4 import BeautifulSoup
import csv
import concurrent.futures

def extract_data_from_page(link):
        page_content = requests.get(link).content
        soup = BeautifulSoup(page_content, 'html.parser')
        title = soup.find('title').text
        content = soup.find('body').text
        return {'link': link, 'title': title, 'content': content}

def scrape_site_from_sitemap(sitemap_url):
        sitemap_content = requests.get(sitemap_url).content
        soup = BeautifulSoup(sitemap_content, 'html.parser')
        links = [link.text for link in soup.find_all('loc')]

        # liste pour stocker les résultats
        results = []
        # pool de connexions pour effectuer plusieurs requêtes simultanément
        with concurrent.futures.ThreadPoolExecutor() as executor:
                # tâches d'extraction de données pour chaque lien
                futures = [executor.submit(extract_data_from_page, link) for link in links]
                # itérer sur les résultats des tâches dès qu'ils sont disponibles
                for future in concurrent.futures.as_completed(futures):
                        results.append(future.result())

        with open('scrapped_data.csv', mode='w', newline='') as csv_file:
                fieldnames = ['link', 'title', 'content']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(results)

        print('Scraping terminé. Regarde dans scraped_data.csv.')
        
scrape_site_from_sitemap('https://pastebin.com/raw/i0dkkPbF')