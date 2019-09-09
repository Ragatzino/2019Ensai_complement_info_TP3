import csv
import requests

import properties

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/frequentation_parheure.csv à partir du webservice de la ville de Rennes')

     # Sans le newline='' mon csv avait des lignes vides entre chaque ligne
    with open('output/frequentation_parheure.csv', 'w', encoding="utf-8", newline='') as csvfile:

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
            csvwriter = csv.writer(csvfile, delimiter=';',)
            # est-ce que l'entête du fichier à été écrit
            firstLine = False
            result = {}
            for row in data:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(firstLine):
                    csvwriter.writerow(['zone', 'total_entree'])
                    firstLine = True

                # la première ligne va servir pour les clés de nos dictionnaires pythons
                zone = row['fields']['zone']
                if zone in result:
                    result[zone]['total_entree'] += row['fields']['comptage_entrees']
                else:
                    result[zone] = {
                        "zone": zone, "total_entree": row['fields']['comptage_entrees']}

            for item in result.values():
                csvwriter.writerow(item.values())

            print(
                'Fichier output/frequentation_parheure.csv créé \n')
            print(
                '------------------------------------------------------------------- \n')
        # On a rencontré une erreur dans lors de la communication avec le WS
        except requests.exceptions.RequestException as error:
            print(error)
