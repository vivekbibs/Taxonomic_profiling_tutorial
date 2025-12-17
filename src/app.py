import streamlit as st
import datetime

# --- Configuration et Titre ---
st.set_page_config(
    page_title="Tutoriel Profiling Taxonomique",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Introduction du Tutoriel ---
st.markdown("# 🧬 Tutoriel: Profiling Taxonomique")
st.markdown("---")

st.markdown(
    """
# Qu'est-ce que le Profiling Taxonomique ?

Le **profiling taxonomique** est une étape clé de l'analyse bioinformatique en métagénomique. \
Son objectif est d'identifier rapidement, sans devoir passer par des méthodes d'assemblage, les micro-organismes présents dans un échantillon \
et d'estimer leur proportion relative.

---

## 📥 Entrée (Input) : Le fichier FASTQ
Le point de départ est un fichier de séquençage brut au format **FASTQ**. 
* L'outil analyse l'ensemble des lectures ADN (reads).

---

## ⚙️ L'Outil de Profiling
L'outil (ex: *Kraken2*, *MetaPhlAn*, *mOTUs*) compare les reads à une base de données de référence. 

### Utilisation du référentiel GTDB
Pour ce profilage, nous utilisons la **GTDB (Genome Taxonomy Database)** plutôt que le NCBI. 
- **Phylogénie génomique** : Les classifications sont basées sur la proximité génétique réelle (protéines marqueurs) \
    plutôt que sur des critères historiques.
- **Nomenclature à jour** : Utilisation des noms normalisés (ex: *Bacillota* au lieu de *Firmicutes*).

L'outil déduit :
1. **La présence des taxons** à plusieurs niveaux (Domaine, Phylum, Classe, Ordre, Famille, Genre, Espèce, Souche).
2. **L'abondance relative** : La part (en %) de chaque taxon dans la communauté globale.

---

## 📤 Sortie (Output) : Tableau de Profiling
Le résultat est un tableau structuré (TSV) qui récapitule la hiérarchie taxonomique et les statistiques de présence.

```text
# Taxonomic Profiling Output
@SampleID:SAMPLEID
@Version:0.9.1
@Ranks:domain|phylum|class|order|family|genus|species
@TaxonomyID:gtdb-r214
@@TAXID	RANK	TAXPATH	TAXPATHSN	PERCENTAGE
d__2	domain	d__2	Bacteria	98.81211
d__2157	domain	d__2157	Archaea	1.18789
p__1239	phylum	d__2|p__1239	Bacteria|Bacillota	59.75801
p__1224	phylum	d__2|p__1224	Bacteria|Pseudomonadota	18.94674
p__28890	phylum	d__2157|p__28890	Archaea|Methanobacteriota	1.18789
c__91061	class	d__2|p__1239|c__91061	Bacteria|Bacillota|Bacilli	59.75801
c__28211	class	d__2|p__1224|c__28211	Bacteria|Pseudomonadota|Alphaproteobacteria	18.94674
c__183925	class	d__2157|p__28890|c__183925	Archaea|Methanobacteriota|Methanobacteria	1.18789
o__1385	order	d__2|p__1239|c__91061|o__1385	Bacteria|Bacillota|Bacilli|Bacillales	59.75801
o__356	order	d__2|p__1224|c__28211|o__356	Bacteria|Pseudomonadota|Alphaproteobacteria|Rhizobiales	10.52311
o__204455	order	d__2|p__1224|c__28211|o__204455	Bacteria|Pseudomonadota|Alphaproteobacteria|Rhodobacterales	8.42263
o__2158	order	d__2157|p__28890|c__183925|o__2158	Archaea|Methanobacteriota|Methanobacteria|Methanobacteriales	1.18789
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

st.markdown("## 🦠 Paramètres de l'Échantillon")

# col_complex_or_not = st.columns(1)[0]

# with col_complex_or_not:
#     st.markdown("### Complexité de l'Échantillon")
#     complexity = st.radio(
#         "**Complexité de l'échantillon**",
#         [
#             "Complexe (Beaucoup d'espèces inconnues)",
#             "Relativement peu d'espèces inconnues",
#         ],
#         index=0,
#         help="Complexe ==> Outils de reconstruction de MAGs ; sinon ==> Profling taxonomique.",
#     )
#     if complexity == "Complexe (Beaucoup d'espèces inconnues)":
#         st.warning(
#             "Pour les échantillons complexes, nous recommandons d'utiliser le pipeline de reconstruction de MAGs."
#         )

# Utilisation des colonnes pour organiser les questions
col_type = st.columns(1)[0]

with col_type:
    st.markdown("### Source de l'Échantillon")
    # Choix de la source principale de l'échantillon
    sample_category = st.selectbox(
        "**2. Quelle est la source générale de votre échantillon ?**",
        ["Humain", "Environnemental", "Animal", "Autre"],
        index=0,
        help="Les bases de données sont souvent spécifiques et adaptées à un ou plusieurs environnements particuliers",
    )

# Question conditionnelle basée sur la catégorie d'échantillon
if sample_category == "Humain":
    st.markdown("### Détails de l'Échantillon Humain")
    human_sample_type = st.radio(
        "**3. Quel type d'échantillon humain analysez-vous ?**",
        ["Intestinal (Gut)", "Cutané (Skin)", "Oral", "Autre"],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes.",
    )
    if human_sample_type == "Intestinal (Gut)":
        catalogue = "hs_10_4_gut"
        tool = "meteor"
    elif human_sample_type == "Cutané (Skin)":
        catalogue = "hs_2_9_skin"
        tool = "meteor"
    elif human_sample_type == "Oral":
        catalogue = "hs_8_14_oral"
        tool = "meteor"

elif sample_category == "Environnemental":
    st.markdown("### Détails de l'Échantillon Environnemental")
    env_sample_type = st.radio(
        "**3. Quel type d'environnement étudiez-vous ?**",
        ["Océanique (Ocean)", "Sol (Soil)", "Autre"],
        index=1,
        horizontal=True,
        help="",
    )
    if env_sample_type == "Océanique (Ocean)" or env_sample_type == "Sol (Soil)":
        catalogue = "GlobDB"

elif sample_category == "Animal":
    st.markdown("### Détails de l'Échantillon Animal")
    animal_sample_type = st.radio(
        "**3. Quel animal analysez-vous ?**",
        [
            "Souris (mouse)",
            "Rat",
            "Chien (dog)",
            "Chat (cat)",
            "Gallus gallus domesticus",
            "Lapin (rabbit)",
            "Cochon (pig)",
            "Mouton (sheep)",
            "Chèvre (goat)",
            "Autre",
        ],
        index=0,
        horizontal=True,
        help="Ces sites ont des communautés microbiennes très distinctes.",
    )
    if animal_sample_type == "Mouton (sheep)" or animal_sample_type == "Chèvre (goat)":
        catalogue = "GlobDB"  # use singleM and/or sylph
    else:
        tool = "meteor"
        if animal_sample_type == "Souris (mouse)":
            catalogue = "mm_5_0_gut"  # use meteor
        if animal_sample_type == "Chien (dog)":
            catalogue = "clf_1_0_gut"  # use meteor
        if animal_sample_type == "Chat (cat)":
            catalogue = "fc_1_3_gut"  # use meteor
        if animal_sample_type == "Gallus gallus domesticus":
            catalogue = "gg_13_6_caecal"  # use meteor
        if animal_sample_type == "Cochon (pig)":
            catalogue = "ssc_9_3_gut"  # use meteor
        if animal_sample_type == "Rat":
            catalogue = "rn_5_9_gut"  # use meteor
        if animal_sample_type == "Lapin (rabbit)":
            catalogue = "oc_5_7_gut"  # use meteor


st.markdown("---")

# Autres paramètres de l'analyse (inchangés ou adaptés)
st.markdown("## 🧬 Paramètres de Séquençage")
col_reads = st.columns(1)[0]
with col_reads:
    st.markdown("### Type de Séquençage")
    # Choix entre Long Reads et Short Reads
    reads_type = st.radio(
        "**1. Quel est le type de lectures générées ?**",
        ["Short Reads (Illumina, etc.)", "Long Reads (PacBio, Nanopore, etc.)"],
        help="",
    )

st.markdown("---")

# Autres paramètres de l'analyse (inchangés ou adaptés)
st.markdown("## ⚙️ Paramètres d'Analyse")

col_organisms_searched, col_analysis_type = st.columns(2)

with col_organisms_searched:
    st.markdown("### Organismes Recherchés")
    organisms = st.multiselect(
        "**Types d'organismes recherchés dans l'échantillon**",
        ["Bactéries", "Archées", "Eucaryotes", "Virus"],
        default=["Bactéries", "Archées", "Eucaryotes", "Virus"],
        help="Sélectionnez les types d'organismes que vous souhaitez identifier dans votre échantillon.",
    )
    if "Virus" in organisms or "Eucaryotes" in organisms:
        st.info(
            "Nos outils ne permettent pas une identification des Virus et des Eucaryotes pour le moment. "
        )

with col_analysis_type:
    st.markdown("### Type d'Analyse")
    analysis_type = st.multiselect(
        "**Type d'analyse souhaitée en + du profiling taxonomique**",
        ["Profiling fonctionnel ", "Strain-level profiling"],
    )
    if (
        "Profiling fonctionnel " in analysis_type
        and "Strain-level profiling" in analysis_type
    ):
        st.info(
            "Le profiling fonctionnel et le strain-level profiling seront effectués en plus du profiling taxonomique."
        )
        st.info(
            "Ce sera effectué par meteor2 et la suite Biobakery (Humann3, StrainPhlAn3, metaphlan)."
        )


# with col_seuil:
#     st.select_slider(
#         "**5. Seuil minimal de confiance (%)**",
#         options=list(range(50, 101, 5)),
#         value=80,
#         help="Définissez le pourcentage minimal de confiance pour l'assignation taxonomique.",
#     )


st.markdown("---")

# Bouton de soumission
if st.button(
    "Lancer la Préparation du Pipeline et Visualiser les Résultats", type="primary"
):
    st.success(
        "Configuration de l'échantillon enregistrée. Le pipeline sera optimisé pour votre type de données."
    )

st.button("Réinitialiser les paramètres")
