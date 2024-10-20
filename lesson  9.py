"""
import requests

#opener = urllib.request.build_opener()
response = requests.get('https://httpbin.org/get')
print(response.content)
print(f"Datatype {type(response.content)}")
"""
"""
import requests

res_parse = []

response = requests.get("https://coinmarketcap.com/")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</span>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                res_parse.append(parse_elem_2)

znach_bitcoin = res_parse[0]
print(znach_bitcoin)
"""

from bs4 import BeautifulSoup

import requests
response = requests.get("https://www.binance.com/uk-UA/price/bitcoin")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    soup_list = soup.find_all("div", {"class": "css-1267ixm"})

    if soup_list:
        price_div = soup_list[0]
        price = price_div.find("div")

        if price:
            print(price.text)
    else:
        print("Element not found")
else:
    print("Response code is not 200")

