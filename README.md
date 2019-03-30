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

# Python & finance
## Sources
(Introduction de la bourse visualisée en python)[https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/]
