import folium

# Zentrum der Karte: Essen-Frohnhausen
frohnhausen_coords = [51.44920345761231, 6.980362111327998]

# Erstelle die Karte
map_frohnhausen = folium.Map(location=frohnhausen_coords, zoom_start=16)

# Orte definieren – einfach erweiterbar!
orte = [
    {
        "name": "HNBK Berufskolleg",
        "coords": [51.45304, 6.9802],
        "beschreibung": "Berufskolleg des HNBK in Frohnhausen",
        "url": "https://hnbk.de"
    },
    {
        "name": "Bioladen Frohnhausen",
        "coords": [51.44670060010371, 6.97690142157827],
        "beschreibung": "Kleiner Bioladen mit regionalen und frischen Produkten.     ",
        "url": "https://www.startnext.com/bioladenretterfrohnhausen"
    },
    {
        "name": "Gemeinschaftsgarten „Buntes Grün“ des Mehrgenerationenhauses ",
        "coords": [51.45333787157612, 6.984234112924383],
        "beschreibung": "Interkultureller Gemeinschaftsgarten am Mehrgenerationenhaus Essen-West.   ",
        "url": "https://mgh-essen.de/"
    },
    {
        "name": "Veganes Restaurant Hummelbude",
        "coords": [51.449818596169685, 6.9771801822436865],
        "beschreibung": "Beliebtes veganes Restaurant mit abwechslungsreichem Mittagstisch.    ",
        "url": "https://www.hummelbude.com"
    },
    {
        "name": "Kaffeerösterei und Café Arcangelo",
        "coords": [51.44695109778423, 6.976376897583824],
        "beschreibung": " Café und Rösterei für handwerklich gerösteten Kaffee.   ",
        "url": "http://www.arcangelo-kaffee.de/"
    },
    {
        "name": "Nachbarschaftsgärten Diergardtstraße",
        "coords": [51.452634002108645, 6.986805912924353],
        "beschreibung": "Gemeinschaftlicher Garten für Nachbarn in Frohnhausen.    ",
        "url": "https://transitiontown-essen.de/gruppen/gemeinschaftsgaerten/frohnhausen/"
    },
    {
        "name": "Diakonieladen Frohnhausen",
        "coords": [51.44992702692617, 6.976800182243684],
        "beschreibung": "Sozialer Laden mit Secondhand-Waren und Hilfsangeboten.    ",
        "url": "https://www.diakoniewerk-essen.de/Arbeitsprojekte/Diakonielaeden/104-Diakonieladen+Frohnhausen"
    },
    {
        "name": "Kolpingfamilie Frohnhausen",
        "coords": [51.44967635533788, 6.9766597245734925],
        "beschreibung": "Katholische Gemeinschaft mit sozialen und kulturellen Aktivitäten.    ",
        "url": "https://vor-ort.kolping.de/kolpingsfamilie-essen-frohnhausen/"
    },
    {
        "name": "Biohof Felchner (Wochenmarkt)",
        "coords": [51.44747811889998, 6.978146942106391],
        "beschreibung": "Regionaler Biohof auf dem Frohnhauser Wochenmarkt.    ",
        "url": "https://biohof-felchner.de/unser-hofladen"
    },
        {
        "name": "Apostelkirche Essen",
        "coords": [51.44596442471481, 6.974397499429239],
        "beschreibung": "Kirche mit sozialem Apostelladen und Gemeindecafé.    ",
        "url": "https://ekef.de/gemeinde-frohnhausen-apostelkirche.html"
    },
    {
        "name": "Café Forum der Apostelkirche",
        "coords": [51.446104914474176, 6.97462025340841],
        "beschreibung": "Gemütliches Café in der Apostelkirche mit vielfältigen Angeboten.    ",
        "url": "https://ekef.de/angebote-gruppen-frohnhausen.html"
    },
    {
        "name": "Café Mundgerecht",
        "coords": [51.45058814946153, 6.9822411822437],
        "beschreibung": "Kleines Café hinter der Alfred-Krupp-Schule.    ",
        "url": "https://cafemundgerecht.de/"
    },
]
    

# Marker hinzufügen
for ort in orte:
    tooltip_text = f"{ort['name']}"
    popup_html = f"""
    <b>{ort['name']}</b><br>
    {ort['beschreibung']}<br>
    <a href="{ort['url']}" target="_blank">Zur Webseite</a>
    """
    folium.Marker(
        location=ort["coords"],
        tooltip=tooltip_text,
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(map_frohnhausen)

# Karte speichern
map_frohnhausen.save("frohnhausen_karte.html")

print("Karte wurde erstellt: 'frohnhausen_karte.html'")
