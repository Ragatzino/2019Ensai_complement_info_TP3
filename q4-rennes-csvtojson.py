import csv
import json

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/prenoms-a-rennes-total.json à partir de files/prenoms-a-rennes.csv')
    with open('output/prenoms-a-rennes-total.json', 'w', encoding="utf-8") as jsonfile:
        with open('files/prenoms-a-rennes.csv', 'r', encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            # dictionnaire de résultat
            result = {}
            firstLine = False

            for row in csvreader:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not firstLine:
                    firstLine = True
                else:
                    key = row[3]+row[4]
                    if key in result:
                        result[key]['Total'] = result[key]['Total'] + \
                            int(row[5])
                    else:
                        result[key] = {'Sexe': row[3],
                                       'Prénom': row[4], 'Total': int(row[5])}

            # on transforme le tableau en json et on écrit le résultat dans le fichier
            jsonfile.write(json.dumps(list(result.values())))

            print('Fichier output/prenoms-a-rennes-total.json créé \n')
            print(
                '------------------------------------------------------------------- \n')
