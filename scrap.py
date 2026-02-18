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

prix = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[3]/div[1]/div/div[1]/div/div/text()')

badges = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[4]/div[1]/div/div[2]/div')

dpe = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[4]/div[1]/div/div[2]/div/div/button/span/text()')

description = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[3]/div[1]/div/div[2]/a/p/text()')

agence = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[3]/div[2]/div[1]/div/a/text()')

agent = tree.xpath('/html/body/div[2]/div[5]/div[1]/div[3]/div[2]/div[1]/div/p/text()')

print(prix)
print(badges)
print(dpe)
print(description)
print(agence)
print(agent)