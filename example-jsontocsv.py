import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv à partir de files/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.json')
    with open('output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv', 'w',  encoding="utf-8") as csvfile:
        with open('files/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.json', 'r', encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)
            # est-ce que l'entête du fichier à été écrit
            firstLine = False

            csvwriter = csv.writer(csvfile, delimiter=';',)
            for row in data:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(firstLine):
                    header = list(row.keys())
                    # 'fields' est un élement imbriqué, il faut le remettre à plat pour le csv
                    header.remove('fields')
                    header = header + list(row['fields'].keys())
                    csvwriter.writerow(header)
                    firstLine = True
                # on ajoute une ligne dans le fichier
                fieldsValues = row['fields'].values()
                row.pop('fields')
                # on ne peut écrire que des chaines de caractères, il faut donc convertir chaque valeur
                csvwriter.writerow(list(row.values()) + list(fieldsValues))

            print(
                'Fichier output/statistiques-de-prets-de-dvd-en-2017-cesson-sevigne.csv créé \n')
            print(
                '------------------------------------------------------------------- \n')
