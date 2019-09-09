# Complément informatique, 2A, TP2

## Formats de données, webservices

Le but de ce TP est de vous faire un peu plus manipuler des fichier de différents formats, et de passer d'un format à l'autre.

Technologies que vous aller voir et utiliser :
- json
- xml
- csv
- git
- webservice
- webscrapping

### 0. Récupérer le code du TP

Ouvrez git bash et déplacer vous vers le dossier où vous voulez télécharger le code.

- Pour aller sur P:
```
cd p:
```

- Pour voir les dossiers et fichiers où vous vous situez

```bash
ls
```

- Pour se déplacer dans monDosier (utiliser la touche tab pour vous aider à taper)

```
cd monDosier
```

Pour télécharger le code :

```bash
git clone https://github.com/HealerMikado/2019Ensai_complement_info_TP3.git squelette-TP3
``` 

Si vous avez besoin de configurer le proxy ensai :

```bash
git config --global http.proxy http://pxcache-02.ensai.fr:3128
git config --global https.proxy http://pxcache-02.ensai.fr:3128
```


### 2. Lancement des exemples

Les programmes example-csvtojson.py, example-csvtoxml.py et example-jsontocsv.py sont des exemples de programmes qui lisent un fichier dans un format pour le convertir dans un autre format.
Lancez ses programmes et comparez les fichiers qui ont été utilisés en entrée et les fichiers obtenus en sorties. Les fichier peuvent mettre dutemps à apparaitre dans votre IDE. Vous pouvez aller les chercher directement dans l'explorateur de fichier windows.

### 3. Conversion d’un nouveau fichier

En s’inspirant de ce qui a été fait avec le fichier prenoms-cesson-sevigne.csv, créez 2 programmes qui convertissent le fichier prenoms-a-rennes.csv en json (prenoms-a-rennes.json) et xml (prenoms-a-rennes.xml)


### 4. Transformer et convertir

Dans le fichier prenoms-a-rennes.csv nous avons le nombre de prénoms par code postal et année de naissance. Nous aimerions avoir une vue plus synthétique en cumulant le nombre de fois
qu’un prénom apparait quelque soit l’année.

Faites un nouveau programme qui convertit prenoms-a-rennes.csv vers un fichier json mais dans
le format suivant :

```js
{
    "Prénom" : "Toto",
    "Sexe" : "H",
    "Total": "1"»
}
```

Ou total est la somme des valeurs trouvées pour le prénom.
Indication : vous utiliserez un dictionnaire avec pour clé le prénom et le sexe (certains prénoms
sont données aux 2 sexes, exemple: Camille) et pour valeur le dictionnaire que vous calculez
(prénom, sexe, total)

### 5. JSON vers CSV

Dans cette partie au lieu d'utiliser un fichier statique, vous allez requêter un des webservices de la ville de Rennes.

En requêtant l'URL suivante 

https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=frequentation_parheure&refine.periode=2017

vous aller obtenir un fichier json avec la fréquentation par heure des zones des Champs Libres en 2017.

(Voici le webservice requêté pour avoir plus de documentation : https://data.rennesmetropole.fr/explore/dataset/frequentation_parheure/information/?disjunctive.zone)

**On souhaite connaitre le nombre totale ayant visité chaque zone en 2017 et exporter cela dans un fichier csv.**

Créez un programme qui requête le webservice de la ville de Rennes, calcule le nombre de visiteur par zone, et qui exporte le résultat vers un fichier csv qui contiendra 2 colonnes :
• zone (pour le nom de la zone)
• total_entree (pour le total des entrée)

**Informatique verte** : vous allez requêter des informations sur une **machine distante**. Ainsi chaque requête consomme de la bande passante. Plus vous allez demander de données, et plus vous allez consommer de bande passante. Cela peut poser des problèmes et dégrader le réseau de l'Ensai. **MAIS SURTOUT**, chaque requête dépense de l'énergie. En effet, **internet n'est pas magique**. Vos données transittent de serveur en serveur, et cela a un coût (en argent mais aussi en équivalent CO2 produit). Plus vous transférez de grosses données, plus vous allez dépenser de l'énergie. Dans la phase de test de votre programme, je vous conseille de travailler avec peu de données. Limitez vous à 50 lignes. Cela est suffisant pour voir si votre programme fonctionne. Une fois le programme au point requêtez le nombre de ligne souhaitées (6288 pour l'année 2017). Cela s'appliquer à cet exercice, mais est également une bonne pratique pour votre future vie de data scientist.

### 7. Webscrapping (again)

Nous allons récupérer directement du contenu disponible sur le web. Essayez de requête la page wikipedia suivante : https://fr.wikipedia.org/wiki/Web_scraping pour récupérer tous les paragraphes qui suivent une balise h2

Le contenu que vous allez récupérer sera du html, pour extraire ce contenu, vous pouvez utiliser la libraire lxml et les xpath. Une recherche google avec les mot clef lxml et xpath devrait vous aider à trouver la syntaxe

### 8. JSON vers Base de données

Reprenez le code de la question 6. Au lieu d’enregistrer la frequentation par zone dans un fichier csv, on souhaite maintenant l’enregistrer en base de données.

Créez une table Frequentation avec pour colonnes Zone (clé primaire) et Total_entree. Puis en s’inspirant du TP 1 créez une classe Frequentation et un dao DaoFrequentation
que vous utiliserez pour alimenter votre table

### 9. Pourquoi ce limiter à 2017 ?

Au lieu de se limiter à 2017, modifiez pour calculer le nombre de visite par zone des Champs Libre par an. Ajouter une colonne année à votre csv et votre table. Puis si vous avez le temps essayez de faire une représentation graphique de vos données

Voici un exemple de code qui peut vous aider : https://python-graph-gallery.com/132-basic-connected-scatterplot/
