import streamlit as st
import datetime

# --- Configuration et Titre ---
st.set_page_config(
    page_title="Tutoriel Profiling Taxonomique",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Introduction du Tutoriel ---
st.markdown("# 🧬 Tutoriel: Profiling Taxonomique")
st.markdown("---")

st.markdown(
    """
    **Bienvenue sur l'interface de Profiling Taxonomique du NNCR !**

    Cette application est conçue pour vous permettre d'explorer et d'analyser vos données
    de séquençage métagénomique. Le profiling taxonomique est
    une étape cruciale en métagénomique : il permet d'identifier et de quantifier les micro-organismes rapidement
    (bactéries, archées, eucaryotes, virus) présents dans un échantillon (sol, eau, intestin, etc.).
    Le profilage des métagénomes vis à vis des bases de données permet la détection et la quantification relative
    des micro-organismes, même en faibles abondances lorsque l'assemblage n'est pas possible.
    """
)

st.info(
    """
    **Objectif du Tutoriel :**
    Nous allons commencer par définir la nature de votre échantillon, car ce choix
    conditionne le choix de l'outil bioinformatique qui va être utilisé ainsi que sa base de données associée.
    """
)
st.markdown("---")

# --- Début des composants interactifs de l'application ---

st.markdown("## 🦠 Classification et Paramètres de l'Échantillon")

complex_or_not= st.columns(1)[0]

with complex_or_not:
    st.markdown("### Complexité de l'Échantillon")
    complexity = st.radio(
        "**Complexité de l'échantillon**",
        ["Complexe (Beaucoup d'espèces inconnues)", "Relativement peu d'espèces inconnues"],
        index=0,
        help="Complexe ==> Outils de reconstruction de MAGs ; sinon ==> Profling taxonomique."
    )
    if complexity == "Complexe (Beaucoup d'espèces inconnues)":
        st.warning("Pour les échantillons complexes, nous recommandons d'utiliser le pipeline de reconstruction de MAGs.")
        
# Utilisation des colonnes pour organiser les questions
col_reads, col_type= st.columns(2)

with col_reads:
    st.markdown("### Type de Séquençage")
    # Choix entre Long Reads et Short Reads
    reads_type = st.radio(
        "**1. Quel est le type de lectures générées ?**",
        ["Short Reads (Illumina, etc.)", "Long Reads (PacBio, Nanopore, etc.)"],
        help=""
    )

with col_type:
    st.markdown("### Source de l'Échantillon")
    # Choix de la source principale de l'échantillon
    sample_category = st.selectbox(
        "**2. Quelle est la source générale de votre échantillon ?**",
        ["Humain", "Environnemental", "Animal", "Autre"],
        index=0,
        help="Les bases de données sont souvent spécifiques et adaptées à un ou plusieurs environnements particuliers"
    )

# Question conditionnelle basée sur la catégorie d'échantillon
if sample_category == "Humain":
    st.markdown("### Détails de l'Échantillon Humain")
    human_sample_type = st.radio(
        "**3. Quel type d'échantillon humain analysez-vous ?**",
        ["Intestinal (Gut)", "Cutané (Skin)", "Oral", "Autre"],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes."
    )
    if human_sample_type == "Intestinal (Gut)":
        catalogue = "hs_10_4_gut"
    elif human_sample_type == "Cutané (Skin)":
        catalogue = "hs_2_9_skin"
    elif human_sample_type == "Oral":
        catalogue = "hs_8_14_oral"
    
elif sample_category == "Environnemental":
    st.markdown("### Détails de l'Échantillon Environnemental")
    env_sample_type = st.radio(
        "**3. Quel type d'environnement étudiez-vous ?**",
        ["Océanique (Ocean)", "Sol (Soil)","Autre"],
        index=1,
        horizontal=True,
        help=""
    )
    if env_sample_type == "Océanique (Ocean)" or env_sample_type == "Sol (Soil)":
        catalogue = "GlobDB"

elif sample_category == "Animal":
    st.markdown("### Détails de l'Échantillon Animal")
    animal_sample_type = st.radio(
        "**3. Quel animal analysez-vous ?**",
        ["Souris (mouse)", "Rat", "Chien (dog)", "Chat (cat)", "Gallus gallus domesticus", "Lapin (rabbit)", "Cochon (pig)","Autre"],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes."
    )

st.markdown("---")

# Autres paramètres de l'analyse (inchangés ou adaptés)
st.markdown("## ⚙️ Paramètres d'Analyse")

col_seuil,col_organisms_searched = st.columns(2)

with col_organisms_searched:
    st.markdown("### Organismes Recherchés")
    organisms = st.multiselect(
        "**Types d'organismes recherchés dans l'échantillon**",
        ["Bactéries", "Archées", "Eucaryotes", "Virus"],
        default=["Bactéries", "Archées", "Eucaryotes", "Virus"],
        help="Sélectionnez les types d'organismes que vous souhaitez identifier dans votre échantillon."
    )

with col_seuil:
    st.select_slider(
        "**5. Seuil minimal de confiance (%)**",
        options=list(range(50, 101, 5)),
        value=80,
        help="Définissez le pourcentage minimal de confiance pour l'assignation taxonomique."
    )

st.markdown("---")

# Bouton de soumission
if st.button("Lancer la Préparation du Pipeline et Visualiser les Résultats", type="primary"):
    st.success("Configuration de l'échantillon enregistrée. Le pipeline sera optimisé pour votre type de données.")

st.button("Réinitialiser les paramètres")