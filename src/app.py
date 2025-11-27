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
    **Bienvenue sur l'interface de Profiling Taxonomique du cluster !**

    Cette application est conçue pour vous permettre d'explorer et d'analyser vos données
    de séquençage avec une simplicité et une réactivité maximales. Le profiling taxonomique est
    une étape cruciale en métagénomique : il permet d'identifier et de quantifier les micro-organismes
    (bactéries, archées, eucaryotes, virus) présents dans un échantillon complexe (sol, eau, intestin, etc.).
    """
)

st.info(
    """
    **Objectif du Tutoriel :**
    Nous allons commencer par définir la nature de votre échantillon, car ce choix
    conditionne la stratégie d'assemblage et les bases de données taxonomiques utilisées.
    """
)
st.markdown("---")

# --- Début des composants interactifs de l'application ---

st.markdown("## ⚙️ Classification et Paramètres de l'Échantillon")

# Utilisation des colonnes pour organiser les questions
col_reads, col_type = st.columns(2)

with col_reads:
    st.markdown("### Type de Séquençage")
    # Choix entre Long Reads et Short Reads
    reads_type = st.radio(
        "**1. Quel est le type de lectures générées ?**",
        ["Short Reads (Illumina, etc.)", "Long Reads (PacBio, Nanopore, etc.)"],
        help="Le choix impacte les outils d'assemblage (e.g., MEGAHIT vs Flye/Canu)."
    )

with col_type:
    st.markdown("### Source de l'Échantillon")
    # Choix de la source principale de l'échantillon
    sample_category = st.selectbox(
        "**2. Quelle est la source générale de votre échantillon ?**",
        ["Humain", "Environnemental", "Animal", "Autre"],
        index=0,
        help="Permet de pré-filtrer les bases de données de référence."
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
        help="Crucial pour l'ajustement des bases de données de taxonomie environnementale."
    )
elif sample_category == "Animal":
    st.markdown("### Détails de l'Échantillon Animal")
    animal_sample_type = st.text_input(
        "**3. Précisez le type d'animal et le site de prélèvement (ex: Microbiome intestinal de Souris)**",
        "Microbiome de Rat, site intestinal",
        help="Plus la description est précise, meilleur sera le calibrage du pipeline."
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