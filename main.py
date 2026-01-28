import requests
import folium

code_commune = 75119

def fetch(codeC):
    response = requests.get(f"http://api.cquest.org/dvf?code_commune={codeC}")
    return response.json()

data = fetch(code_commune)

# On récupère les coordonnées valides
points = []
for item in data.get("resultats", []):
    lat = item.get("lat")
    lon = item.get("lon")
    
    # On ne garde que si les valeurs existent et sont numeriques
    if lat is not None and lon is not None:
        points.append((float(lat), float(lon)))

# Si on a au moins un bien, on centre la carte dessus
if points:
    center = points[0]
else:
    center = (48.8566, 2.3522)  # fallback Paris

m = folium.Map(location=center, zoom_start=13)

# Ajout des marqueurs uniquement pour les points valides
for lat, lon in points:
    folium.Marker(
        location=[lat, lon],
        tooltip="Bien DVF",
        icon=folium.Icon(color="blue"),
    ).add_to(m)

m.save("test.html")
