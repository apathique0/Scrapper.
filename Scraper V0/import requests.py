import requests
from bs4 import BeautifulSoup

url = 'http://lpohdb.fr/'

# Envoi d'une requête HTTP GET à l'URL cible
response = requests.get(url)

# Vérification du statut de la réponse
if response.status_code == 200:
    # Parsing du contenu HTML de la page avec BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraction des données souhaitées
    # ...

else:
    print(f"Erreur lors de la récupération de la page ({response.status_code})")