# Gestion du Budget

Gestion du Budget est une application web construite avec Flask pour gérer vos dépenses et revenus de manière efficace.

## Fonctionnalités

- **Navigation** :
  - Un navbar contenant un lien vers l'accueil et une page "À propos".
  - Un formulaire pour rechercher les éléments d'intérêt.

- **Page d'accueil** :
  - Deux tableaux : un pour les dépenses et un pour les revenus.
  - Chaque tableau a une cellule contenant une icône d'ajout.
  - Après l'ajout d'une dépense ou d'un revenu, deux boutons apparaissent dans la colonne des actions pour modifier ou supprimer l'entrée.

## Installation

### Prérequis

- Python 3.x
- Git

### Étapes d'installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/CheikhSadibouSow/2ndProject.git
    cd 2ndProject
    ```

2. Créez et activez un environnement virtuel :

    ```bash
    python3 -m venv myvenv
    source myvenv/bin/activate  # Sur Windows: myvenv\Scripts\activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

Pour démarrer le serveur Flask, exécutez les commandes suivantes :

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run

## Utilisation

Les contributions sont les bienvenues. Veuillez suivre ces étapes pour contribuer :

Fork le dépôt.
Créez une branche pour votre fonctionnalité ou bug fix (git checkout -b feature/AmazingFeature).
Commitez vos modifications (git commit -m 'Add some AmazingFeature').
Pushez vers la branche (git push origin feature/AmazingFeature).
Ouvrez une Pull Request.
## A propos
Cette application a été développée pour aider les utilisateurs à gérer leurs finances personnelles de manière simple et intuitive.

##Auteur
Cheikh Sadibou Sow


