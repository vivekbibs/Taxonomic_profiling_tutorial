import streamlit as st

st.title("Introduction")

st.markdown("")

st.markdown(
    """
        **Streamlit** est un outil permettant de créer des applications web en python. 
        C'est très pratique pour créer des dashboard web qui permettent aux biologistes
        d'intéragir avec leur données de façon visuelle.

        Dans ce tutoriel, on va apprendre à créer des dashboards avec Streamlit pour visualiser
        des données !
    """
)

st.header("Installer son environment")

st.markdown(
    """
        Il y a peu de choses à configurer pour commencer avec streamlit. En théorie, il n'y a que le package python de streamlit à ajouter à importer

        Mais pour suivre le tutoriel on aura besoin d'un peu plus que ça !
    """
)

st.subheader("Cloner la repo du tutoriel")

st.markdown(
    """
    Le tuoriel est disponible sur ces repos: 
    - Github : [https://github.com/Phloemus/Streamlit-Coin-Geek](https://github.com/Phloemus/Streamlit-Coin-Geek)
    - Gitlab (equipe Bird) : [https://gitlab.univ-nantes.fr/BiRD/reseau_bn/-/tree/main/coins-geek/streamlit?ref_type=heads](https://gitlab.univ-nantes.fr/BiRD/reseau_bn/-/tree/main/coins-geek/streamlit?ref_type=heads)
    """
)

st.warning(
    """
        **Différence entre les deux repos**    

        Ces deux repos sont identique, mais il est possible qu'il y ai besoin d'une 
        compte gitlab de l'université de Nantes pour accèder au gitlab. La repo github 
        en revenche est accessible par tout le monde
    """
)

st.markdown("")

st.markdown("Cloner la repo du tutoriel")

st.code(
    """
        git clone https://github.com/Phloemus/Streamlit-Coin-Geek
    """
)

st.markdown("")

st.subheader("Installer son environment python pour ce tutoriel")

st.markdown(
    """
        Le package streamlit est le seul nécéssaire pour créer une application simple. 
        Mais comme on va manipuler des données on aura aussi besoin de packages comme
        **panda**
    """
)

st.code(
    """
        ## Créer l'envrionment du tutoriel
        cd src
        python -m venv ./venv
        pip install -r requirements.txt

        ## Activer l'environment 
        source venv/bin/activate
    """
)

st.info(
    """
        **Tout est prêt**

        A ce stade là tout est prêt pour créer une application streamlit !
    """
)
