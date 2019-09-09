import csv
from lxml import etree

if __name__ == "__main__":
    print('------------------------------------------------------------------- \n')
    print('Création du fichier output/prenoms-a-rennes.xml à partir de files/prenoms-a-rennes.csv')
    with open('output/prenoms-a-rennes.xml', 'wb') as xmlfile:
        with open('files/prenoms-a-rennes.csv', 'r', encoding="utf-8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            # tableau de résultat
            result = etree.Element("Prenoms")
            firstLineProcessed = False
            for row in csvreader:
                # la première ligne va servir pour les clés de nos dictionnaires pythons
                if not(firstLineProcessed):
                    firstLineProcessed = True
                else:
                    # on transforme les lignes suivantes en dictionnaire
                    prenomParent = etree.SubElement(result, "Prenom")

                    annee = etree.SubElement(prenomParent, "Annee")
                    annee.text = row[0]

                    commune = etree.SubElement(prenomParent, "CodeCommune")
                    commune.text = row[1]

                    codeInsee = etree.SubElement(
                        prenomParent, "LibelleCommune")
                    codeInsee.text = row[2]

                    sexe = etree.SubElement(prenomParent, "Sexe")
                    sexe.text = row[3]

                    prenom = etree.SubElement(prenomParent, "Prenom")
                    prenom.text = row[4]

                    nombre = etree.SubElement(prenomParent, "Nombre")
                    nombre.text = row[5]

            # on transforme le
            xmlfile.write(etree.tostring(result, pretty_print=True))

            print('Fichier output/prenoms-a-rennes.xml créé \n')
            print(
                '------------------------------------------------------------------- \n')
