import requests
from lxml import html

url = 'https://www.paruvendu.fr/immobilier/vente/aquitaine/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9",
}

req = requests.get(url, headers=headers)
tree = html.fromstring(req.content)

blocs = tree.xpath('//div[contains(@class, "blocAnnonce")]')

print(f"{len(blocs)} annonces trouvées\n")

for bloc in blocs:

    h3 = bloc.xpath('.//h3/text()')

    prix = bloc.xpath('.//div[contains(@class,"encoded-lnk")]/text()')

    description = bloc.xpath('.//p/text()')

    agence = bloc.xpath('.//a[contains(@class,"text-sm")]/text()')

    agent = bloc.xpath('.//p[contains(@class,"text-grey-600")]/text()')

    prix_val = prix[0] if prix else None
    description_val = description[0] if description else None
    agence_val = agence[0] if agence else None
    agent_val = agent[0] if agent else None

    print("Prix:", prix_val)
    print("Description:", description_val)
    print("Agence:", agence_val)
    print("Agent:", agent_val)
    print("-" * 40)

