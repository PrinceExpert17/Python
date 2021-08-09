from requests_html import HTMLSession

url = "https://www.amazon.com/s?k=nvme&ref=nb_sb_noss"

headers = {"User-Agents": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

s = HTMLSession()


def getcode(item):
    r = s.get(f"https://www.amazon.com/s?k={item}&ref=nb_sb_noss", headers=headers)
    asins = r.html.find('div.s-main-slot div[data-asin]')
    return [asin.attrs['data-asin'] for asin in asins if asin.attrs['data-asin'] != '']


def getinfo(asin):
    r = s.get(f'https://www.amazon.com/dp/{asin}')
    product = r.html.find('#productTitle', first=True)
    print(product, asin)
    return

getinfo('B07MG119KG')
