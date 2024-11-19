<p align="center">
    <a href="https://streamlit.io" target="_blank" rel="noopener">
        <img src="https://raw.githubusercontent.com/Phloemus/Streamlit-Coin-Geek/main/img/cover.png" alt="Streamlit - Créer des dashboards web en python" />
    </a>
</p>


<p align="center">
    <em>Une présentation proposée par <a href="https://pf-bird.univ-nantes.fr/bn/">le réseau Bioinfo Nantais</a></em>
</p>

## Objectifs

L'objectif de ce tutoriel est d'apprendre à utiliser Streamlit pour créer des petites démos (dashboard) web. 
L'avantage d'un dashboard c'est qu'il s'agit d'une interface simple que les biologistes peuvent utiliser sans aucun 
problème. 

Streamlit rend le traitement des données biologique plus transparant pour les biologistes humides. Par exemple un 
dashboard Streamlit est excellent pour montrer des résultats d'analyse à son responsable de thèse. 

Malgré tous les avantages qu'offre Streamlit, c'est un outil encore méconnu de la communauté bioinfo. Dans ce coin geek
on va y remédier et apprendre à créer des dashboards web pour montrer ses données !

## Requirements

Pour bien suivre le tutoriel, il y a certains programmes qui sont nécéssaire d'avoir installé sur son ordinateur. 

- git
- python3
- pip

De préférence, utiliser plutôt Linux pour suivre le tutoriel. Sous windows, les étapes devraient être identiques, 
mais des erreurs de packages python peuvent tout de même subsister :/ 

> [!NOTE]
> Si vous rencontrez des difficultés à installer les packages ou un programme, n'hésitez pas à demander de l'aide sur le 
> [serveur mattermost](https://mattermost.univ-nantes.fr/bioinfosnantais/channels/town-square) du réseau BN 
> (c'est un endroit pratique pour demander de l'aide en cas de bloquage !)

## Mise en place de l'environement

Une application streamlit repose sur plusieurs packages python qu'il est pertinent de regrouper dans un même 
environement python. La liste des packages nécéssaire pour créer l'application démo du tutoriel est dans
le fichier **src/environment.yaml**.

La méthode la plus simple pour suivre le tutoriel est de cloner le répertoire github puis de créer un environment avec le fichier **requirements.txt**

Cloner le répertoire github

```
bash 
git clone https://github.com/Phloemus/Streamlit-Coin-Geek.git
```

Créer un environement python avec les packages nécéssaire pour le tutoriels

```
bash
cd Streamlit-Coin-Geek/src
python -m venv ./venv
pip install -r requirements.txt
```

Activer l'environement python du tutoriel

```
bash
source venv/bin/activate
```

Et voilà, maintenant il y un environment contenant streamlit et tous les packages nécéssaire pour déployer l'application 
du tutoriel qui est déployé en local !

## Tutoriel

Le tutoriel est découpé en plusieurs parties afin d'illustrer les différents concepts essentiels à maîtriser pour 
créer un dashboard Streamlit élégant et interactif.

Ce tutoriel est divisé en plusieurs étapes. Chaque partie abouti avec un peu de pratique où 
l'on manip les concepts vu dans la partie dans un dashboard streamlit test (**app.py**)

### Sommaire

1. Créer un layout pour son dashboard
2. Ajouter de nouvelles pages
3. Rendre son dashboard interactif

## Commencer le tutoriel

Pour passer à la suite du tutoriel, voir le *README* du dossier **src**

## Documentation officielle

Il existe plein de composants que l'on a pas exploré dans le tutoriels, vous pouvez tous les retrouver dans la 
documentation officielle de Streamlit

- La documentation officielle de Streamlit est disponible [ici](https://docs.streamlit.io/)
- La liste des composant Streamlit est disponible [ici](https://docs.streamlit.io/develop/api-reference)

## Canaux de discussion 

Pour les membres du réseau Bioinfo Nantais (BN), vous pouvez poser vos questions sur ce tutoriel dans le 
[canal dédié](https://mattermost.univ-nantes.fr/bioinfosnantais/channels/town-square) sur mattermost

Pour les personnes non membre du réseau vous pouvez poser vos question en 
[ouvrant une issue](https://github.com/Phloemus/Streamlit-Coin-Geek/issues/new) avec le label "question"
directement dans ce répertoire Github

<p>
    <em><b>Brieuc Quemeneur</b> pour le réseau <b>Bioinfo Nantais</b></em>
</p>
