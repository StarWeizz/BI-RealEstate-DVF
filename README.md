# BI-RealEstate-DVF

Projet d'analyse de données immobilières françaises combinant data science, scraping web et visualisation cartographique, basé sur les données DVF (Demandes de Valeurs Foncières) du gouvernement français.

---

## Stack technique

| Couche | Technologie |
|---|---|
| Analyse de données | Python, Pandas, NumPy |
| Visualisation | Folium, Branca, Matplotlib |
| Machine Learning | Scikit-learn (RandomForestRegressor) |
| Web scraping | requests, lxml, BeautifulSoup4 |
| Backend API | Node.js, Express 5, pg (PostgreSQL) |
| Base de données | PostgreSQL |
| Frontend | HTML + JavaScript (Fetch API) |
| Notebooks | Jupyter |
| Source de données | DVF — données ouvertes du gouvernement français |

---

## Structure du projet

```
RealEstate/
│
├── --- Python / Data Science ---
├── main.py                                      # Script de génération de carte Folium via l'API DVF
├── scrap.py                                     # Scraper paruvendu.fr (lxml + requests)
│
├── --- Notebooks Jupyter ---
├── realestate.ipynb                             # Analyse exploratoire via l'API DVF (Paris 19e)
├── valeur_fonctiere.ipynb                       # Analyse par département + cartes choroplèthes
├── prediction.ipynb                             # Prédiction de prix (Random Forest, R² ~0.77)
├── folium.ipynb                                 # Expérimentations de cartes interactives
├── folium_test.ipynb                            # Sandbox Folium
├── scraper_paruvendu.ipynb                      # Scraping paruvendu.fr en notebook
│
├── --- Cartes HTML générées ---
├── map.html                                     # Carte Folium basique
├── carte_filtrable_biens_par_departement.html   # Carte filtrée par type de bien et département
├── carte_valeur_fonciere_par_departement.html   # Choroplèthe — valeur moyenne par département
├── carte_valeur_fonciere_interactive.html       # Version interactive alternative
│
├── --- Données ---
├── ValeursFoncieres.txt                         # Données DVF brutes (185 Mo, gitignored)
├── moyenne_valeur_fonciere_par_departement.csv  # Statistiques agrégées par département
├── france.json                                  # GeoJSON des départements français
│
├── --- Application Web (Node.js) ---
├── paruvendu.js                                 # Serveur Express + API PostgreSQL (port 9000)
├── front-paruvendu.js                           # Logique frontend (fetch + affichage)
├── paruvendu.html                               # Interface de consultation des annonces
└── bloc_annonce-sample.html                     # Exemple de HTML scraped (dev/debug)
```

---

## Fonctionnalités

### Analyse des données DVF
- Chargement et nettoyage du fichier DVF (185 Mo, délimité par `|`)
- Agrégation par département : valeur moyenne, nombre de biens, répartition par type (Maison, Appartement, Dépendance, Local commercial)
- Export CSV des statistiques agrégées

### Visualisation cartographique
- Cartes choroplèthes interactives avec Folium
- Couches filtrables par type de bien
- Marqueurs géolocalisés pour les transactions individuelles

### Prédiction de prix (ML)
- Modèle : `RandomForestRegressor(n_estimators=50, max_depth=15)`
- Features : type de bien, surface bâtie, surface terrain, nombre de pièces, code département, code commune
- Résultat : R² ≈ 0.77
- Exemple : prédiction de ~205 308 € pour une maison de 69m² à Meximieux (01)

### Scraping paruvendu.fr
- Extraction des annonces immobilières (prix, description, agence, agent)
- Stockage en base PostgreSQL (`paruvendu` DB, table `biens`)

### API & Interface web
- API REST Express (port 9000) : `GET /api/all` retourne toutes les annonces en JSON
- Interface HTML minimaliste pour consulter les annonces en temps réel

---

## Architecture

```
API DVF publique (cquest.org)
        │
        ├─> realestate.ipynb     — Analyse exploratoire, scatter plots
        └─> main.py              — Génération rapide de carte

ValeursFoncieres.txt (185 Mo, local)
        │
        ├─> valeur_fonctiere.ipynb  — Agrégation, cartes choroplèthes, export CSV
        └─> prediction.ipynb        — Modèle Random Forest, importance des features

paruvendu.fr
        │
        └─> scrap.py / scraper_paruvendu.ipynb
                │
                └─> PostgreSQL (DB: paruvendu, table: biens)
                        │
                        └─> paruvendu.js (Express API, port 9000)
                                │
                                └─> paruvendu.html + front-paruvendu.js
```

---

## Lancement

### Prérequis
- Python 3.x + environnement virtuel (`venv/`)
- Node.js
- PostgreSQL (base `paruvendu`, table `biens`)

### Python (notebooks / scripts)
```bash
# Activer l'environnement virtuel
.\venv\Scripts\activate       # Windows
source venv/bin/activate      # Linux/Mac

# Installer les dépendances
pip install pandas numpy matplotlib folium requests branca scikit-learn lxml beautifulsoup4 jupyter

# Lancer Jupyter
jupyter notebook

# Ou exécuter le script de carte directement
python main.py
```

### Application web (Node.js)
```bash
npm install
node paruvendu.js
# API disponible sur http://localhost:9000/api/all
# Ouvrir paruvendu.html dans le navigateur
```

---

## Source des données

- **DVF (Demandes de Valeurs Foncières)** : [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/) — transactions immobilières françaises enregistrées par les notaires
- **API DVF** : [api.cquest.org/dvf](https://api.cquest.org/dvf)
- **Annonces** : paruvendu.fr (scraping)

---

## Auteur

Projet réalisé dans le cadre de Yboost — Ynov 2025
