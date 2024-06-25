from bs4 import BeautifulSoup
import requests
import json

def get_asiaf_product_list():
    product_grid = []
    n = 2
    #product_dict = {}
    url = 'https://bolter.pl/pl/c/A-SONG-OF-ICE-AND-FIRE/1021'
    #html_text = requests.get(url).text
    #print(requests.get(url).status_code)
    #soup = BeautifulSoup(html_text, 'lxml')
    while requests.get(url).status_code == 200:
        html_text = requests.get(url).text
        soup = BeautifulSoup(html_text, 'lxml')
        products = soup.find_all('div', class_='product s-grid-3 product-main-wrap')
        #names = [product.find('a', class_='prodname').text.replace('\n', '') for product in products]
        url = 'https://bolter.pl/pl/c/A-SONG-OF-ICE-AND-FIRE/1021'
        for product in products:
            name = product.find('a', class_='prodname').text.replace('\n', '')
            link = 'https://bolter.pl' + product.div.a['href']
            price = (product.find('div', class_='price f-row'))
            price_final = price.find('em').text.replace('\xa0', '')
            availability = product.find('span', class_='availability')
            if availability is None:
                availability = 'Brak na stanie'
            else:
                availability = availability.text.strip()
            product_grid.append([name, price_final, availability, link])
        url = url + '/' + str(n)
        n += 1
        #    product_dict.update({"ASOIAF": product_grid})
        #    print(name, price_final, availability)
        #print(product_grid)

    return product_grid
        #print(json.dumps(product_grid))

print(get_asiaf_product_list())    