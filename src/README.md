# Code de l'application streamlit 

## Lancer son dashboard en local

### Créer et activer l'environement python

Pour lancer une application Streamlit il faut avoir le package **streamlit** installé. Il peut être installé 
de façon globale mais le mieux est quand même de créer un environment python avec les packages que vous 
voulez utiliser en plus !

Pour aller plus vite, il est possible de créer un environment avec tous les packages utilisé pour créer le dashboard
du point geek en utilisant le fichier *environment.yaml*

```
bash
## Crée l'environement python avec les packages utilisé pour le dashboard du tutoriel
cd src
python -m venv ./venv
pip install -r requirements.txt
```

### Créer son un dashboard de base

Pour créer son dashboard, il suffit de créer un fichier **app.py** dans le dossier **src** de 
la repo

```
bash 
cd src
touch app.py
```

Pour avoir un dashboard minimal avec Streamlit il suffit d'ajouter le package streamlit à 
**app.py** 

```
python
## Dans le fichier app.py
import streamlit as st
```

### Lancer son dashboard 

```
bash
streamlit run app.py
```

Streamlit se lance par défaut sur le port **8051** - [Voir mon dashboard local](http://localhost:8051)

Normalement le dashboard est vide, il s'agit juste d'une page blanche avec une barre de 
navigation sur le côté permettant d'accèder aux différentes pages du tutoriel. 

### Suivre le tutoriel

Le tutoriel se découpe en plusieurs parties. Une partie par page. Aller sur la page **Bases** 
grâce à la barre de navigation pour commencer le tutoriel !
