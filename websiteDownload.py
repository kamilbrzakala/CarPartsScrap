from urllib.error import URLError
import requests, bs4, re, logging
from urllib.request import urlopen, Request

headers = requests.utils.default_headers()
headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
})

# logging.debug('Connected.')

def webScrap(www):

    url = www

    if ('www' not in www):
        www = www.split('/')[2].split('.')[0]
        print(www)
    else:
        www = www.split('.')[1]
        print(www)

    #request

        try:
            response = requests.get(url, headers=headers)
            res_status = response.status_code
            res_status2 = response.raise_for_status()
            print(res_status)
            # print(response.raise_for_status())
            soup = bs4.BeautifulSoup(response.content, "html.parser")

            # print(soup.prettify())

            # saving to file
            if res_status == 200:
                file = open(www + '.html', 'w')
                file.write(str(soup.prettify()))
                file.close()
        except Exception as exc:
            print('There was a problem with error: {}'.format(exc))


# storeList = ['https://www.onlinecarparts.co.uk/car-brands/spare-parts-jaguar/xj-x350-x358/17228.html']

webScrap('https://www.onlinecarparts.co.uk/car-brands/spare-parts-jaguar/xj-x350-x358/17228.html')


