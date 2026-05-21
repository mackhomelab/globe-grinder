import requests

url = "https://restcountries.com/v3.1/all?fields=cca2,cca3,name,capital,languages,latlng"
response = requests.get(url, timeout=30)

countries = response.json()

for c in countries:
    iso2      = c["cca2"]
    iso3      = c["cca3"]
    name      = c["name"]["common"]
    capital   = (c.get("capital") or [None])[0]       # handles missing AND empty list
    languages = list(c.get("languages", {}).values())
    lat, lng  = c.get("latlng", [None, None])
    flag_url  = f"https://flagcdn.com/{iso2.lower()}.svg"

    print(iso2, iso3, name, capital, languages, [lat, lng], flag_url)