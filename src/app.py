import streamlit as st
import datetime

# --- Configuration et Titre ---
st.set_page_config(
    page_title="Tutoriel Profiling Taxonomique",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Introduction du Tutoriel ---
st.markdown("# 🧬 Tutoriel: Profiling Taxonomique Interactif")
st.markdown("---")

st.markdown(
    """
    **Bienvenue sur l'interface de Profiling Taxonomique du NNCR !**

    Cette application est conçue pour vous permettre d'explorer et d'analyser vos données
    de séquençage métagénomique. Le profiling taxonomique est
    une étape cruciale en métagénomique : il permet d'identifier et de quantifier les micro-organismes
    (bactéries, archées, eucaryotes, virus) présents dans un échantillon complexe (sol, eau, intestin, etc.).
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

st.markdown("## ⚙️ Classification et Paramètres de l'Échantillon")

# Utilisation des colonnes pour organiser les questions
col_reads, col_type, complex_or_not = st.columns(3)

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
        ["Intestinal (Gut)", "Cutané (Skin)", "Oral", "Vaginal", "Sanguin (Blood)", "Autre"],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes."
    )
elif sample_category == "Environnemental":
    st.markdown("### Détails de l'Échantillon Environnemental")
    env_sample_type = st.radio(
        "**3. Quel type d'environnement étudiez-vous ?**",
        ["Marin (Océan, Récif)", "Sol (Soil)", "Eau douce (Freshwater)", "Air", "Sédiment"],
        index=1,
        horizontal=True,
        help=""
    )
elif sample_category == "Animal":
    st.markdown("### Détails de l'Échantillon Animal")
    animal_sample_type = st.radio(
        "**3. Quel animal analysez-vous ?**",
        ["Souris (mouse)", "Rat", "Chien (dog)", "Chat (cat)", "Gallus gallus domesticus", "Lapin (rabbit)", "Cochon (pig)"],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes."
    )
with complex_or_not:
    st.markdown("### Complexité de l'Échantillon")
    complexity = st.radio(
        "**Complexité de l'échantillon**",
        ["Complexe (Beaucoup d'espèces inconnues)", "Relativement peu d'espèces inconnues"],
        index=0,
        help="Complexe ==> Outils de reconstruction de MAGs ; sinon ==> Profling taxonomique."
    )


st.markdown("---")

# Autres paramètres de l'analyse (inchangés ou adaptés)
st.markdown("## ⚙️ Paramètres d'Analyse (Filtres)")

col_gene, col_seuil, col_date = st.columns(3)

with col_gene:
    st.selectbox(
        "**4. Nom du marqueur génétique (si ciblé)**",
        ("Métagénome total", "16S rRNA", "ITS", "18S rRNA"),
        help="Sélectionnez 'Métagénome total' si vous utilisez des séquences Shotgun."
    )

with col_seuil:
    st.select_slider(
        "**5. Seuil minimal de confiance (%)**",
        options=list(range(50, 101, 5)),
        value=80,
        help="Définissez le pourcentage minimal de confiance pour l'assignation taxonomique."
    )

with col_date:
    st.date_input(
        "**6. Date de l'analyse**",
        datetime.date(2024, 7, 6),
        help="Indiquez la date de réalisation de l'analyse bio-informatique."
    )

st.markdown("---")

# Bouton de soumission
if st.button("Lancer la Préparation du Pipeline et Visualiser les Résultats", type="primary"):
    st.success("Configuration de l'échantillon enregistrée. Le pipeline sera optimisé pour votre type de données.")

st.button("Réinitialiser les paramètres")