# Klondike

# Théorie de Markovitch
## 1. Récupérer les données et début du code
 - Télécharger les données historiques de tous les ETFs dans le dossier `/data`. Un fichier par ETF.
 - Faire la structure des objets pandas pour stocker les données
 - Trouver une bibliothèque pour afficher les données
 - Créér un script pour calculer la covariance
 - Créér un script pour calculer la rentabilité sur une période de temps 
 - Créér un script pour calculer la volatilité
 
## 2. Creation du modèle de Markovitch
 - Préciser le l'intervalle de temps d'apprentissage et de test.
 - Creer la fonction de Markovitch à appliquer sur un portefeuille
```
# Portefeuille = combinaison linéaire d'ETFs
markovitch(Portefeuille, learningRange) -> (Volatility, ExpectedReturn)
```
 - Optimiser la composition du portefeuille pour optimiser `markovitch`.
 - Choix du portefeuille

## 3. Stratégie de business
 - Comment créer une société d'investissement ?
 - Comment créér un ETF ? 
 - Comment fonctionne les taxes ?
 - ...

## 4. Confrontation du modèle 
 - Présenter le modèle 

## 5. Mise en place
 -  Structure juridique pour acheter et vendre des ETF

# Sources
## Python & finance
(Introduction de la bourse visualisée en python)[https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/]

## Administration des ETF
[lien](https://www.etf.com/publications/journalofindexes/joi-articles/2305.html): La création d'ETFs aux US. C'est bien détaillé et met en avant les points importants de la création de l'indice. 
  - L'auteur parle aussi des ETVs (Exchange Trade Vehicule) qui est similaire aux ETFs mais sans la prise de tête de créer/avoir un partenariat avec un fond.
  - Pour la mise en place sur le marché primaire, il suffit de trouver des `Authorized Participants` (AP) alias des investisseurs, prêt à acheter les actifs sous jacents en échange de parts. Ça devrait pouvoir se trouver.
  - Par contre pour le marché secondaire, c'est la que ça se complique avec l'accord de la SEC (AMF américaine) qui est long et complexe. Le risque est d'avoir des actifs que l'on ne peut pas échanger sur une place boursière mais uniquement de gré-à-gré .
  - J'aime bien aussi le dernier paragraphe de l'article : quand l'ETF est mis en place, il faut ensuite faire de la communication et du marketing. En faite c'est un produit comme un autre.
https://investisseur-individuel.com/une-strategie-alternative-pour-gagner-en-bourse-les-etf/
