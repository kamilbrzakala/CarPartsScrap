from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import OrderedDict
import json, requests

i = 1
data = open('onlinecarparts.html')

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

soup = BeautifulSoup(data, "html.parser")



links = []
scraped_store = []
store_info = {}
store = []

def download(link):
    try:
        response = requests.get(link, headers=headers)
        res_status = response.status_code
        res_status2 = response.raise_for_status()
        # print(res_status)
        # print(response.raise_for_status())
        soupp = BeautifulSoup(response.content, "html.parser")

        # print(soup.prettify())

        # saving to file
        if res_status == 200:
            file = open('parts.html', 'w')
            file.write(str(soupp.prettify()))
            file.close()
    except Exception as exc:
        print('There was a problem with error: {}'.format(exc))

for div in soup.find_all("div", attrs={'class': 'dir-catalog-item'}):

    f = open('example.csv', 'a')

    category = div.find('div', attrs={'class': 'dir-catalog-item__title'}).get_text().strip()
    print(category)

    for li in div.find_all('li'):

        ### szukamy linki do produktów każdej podkategorii
        a = li.find('a')

        if a:
            links.append(a['href'])
            link = a['href']
            download(link)
            # z = a.get_text().strip()# + ": " + a['href']
            # item = a.get_text().strip()
            print(a.get_text().strip() + ": " + a['href'])

            free_slot_file = open('parts.html')
            soup3 = BeautifulSoup(free_slot_file, "html.parser")

            for div in soup3.find_all("div", attrs={'class': 'item '}):
                item_Title = div.find('div', attrs={'class': 'item_title'}).get_text().strip()
                item_price = div.find('div', attrs={'class': 'price'}).next_element
                print(item_Title + ": " + item_price.strip())

                string = category + " | " + a.get_text().strip() + " | " + item_Title + " | " + item_price.strip() + "\n"
                f.write(string)



        aa = li.find('span')

        if aa:
            links.append(aa['url'])
            # z = aa.get_text().strip()# + ": " + aa['url']
            link = aa['url']
            download(link)
            print(aa.get_text().strip() + ": " + aa['url'])
            # item = aa.get_text().strip()

            free_slot_file = open('parts.html')
            soup3 = BeautifulSoup(free_slot_file, "html.parser")

            for div in soup3.find_all("div", attrs={'class': 'item '}):
                item_Title = div.find('div', attrs={'class': 'item_title'}).get_text().strip()
                item_price = div.find('div', attrs={'class': 'price'}).next_element
                print(item_Title + ": " + item_price.strip())
                string = category + " | " + aa.get_text().strip() + " | " + item_Title + " | " + item_price.strip()+ "\n"
                f.write(string)


    f.close()

# Start from
print(store)
print(len(links))

# poniżej otwieram plik json
with open('onlinecarparts.json', 'w') as json_file:
    json.dump(scraped_store, json_file, indent=4, ensure_ascii=False)

# TODO

# script should download all pages with parts, if any.