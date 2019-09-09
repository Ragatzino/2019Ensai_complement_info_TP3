import requests

import properties
from business_object.frequentation import Frequentation
from dao.dao_frequentation import DaoFrequentation


if __name__ == "__main__":
    dao = DaoFrequentation()

    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/frequentation_parheure.csv à partir de files/frequentation_parheure.json')
    with open('files/frequentation_parheure.json', 'r', encoding="utf-8") as jsonfile:
        try:
            proxies = {
                'http': properties.http_proxy,
                'https': properties.https_proxy
            }

            # On prépare les params de la requête. C'est requests qui va les mettre en forme pour nous !
            params = {
                'apikey': properties.api_key,
                'dataset': "frequentation_parheure",
                "rows": 6288}

            # On envoie une requête poru récupérer les statistiques d'emprunt de films
            response = requests.get(
                'https://data.rennesmetropole.fr/api/records/1.0/search/'
                , proxies=proxies
                , params=params)

            data = response.json()['records']
            # est-ce que l'entête du fichier à été écrit
            result = {}
            for row in data:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                zone = row['fields']['zone']
                if zone in result:
                    result[zone].total_entree += row['fields']['comptage_entrees']
                else:
                    result[zone] = Frequentation(
                        zone, row['fields']['comptage_entrees'])
            for freq in result.values():
                dao.create(freq)
            print('données insérées en base \n')
            print(
                '------------------------------------------------------------------- \n')
        except requests.exceptions.RequestException as error:
            print(error)

