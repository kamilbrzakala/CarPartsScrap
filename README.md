# This project has been written in order to download all parts for Jaguar xj350 v8.

# Concerned Website:
https://www.onlinecarparts.co.uk/car-brands/spare-parts-jaguar/xj-x350-x358/17228.html

# Logic of this project:
- Parse each category and it's subcategories.
- Open each subcategory and parse all items from 1st page.
- Save data to csv file.

# TODO
Implement below function in order to open each subpage and parse all of the items.

# def responsee(url):
#     try:
#         response = requests.get(url, headers=headers)
#         res_status = response.status_code
#         print(res_status)
#         soup = bs4.BeautifulSoup(response.content, "html.parser")
#
#         # below add css which refers to URL that redirects to the next page 
#         s = soup.find(class_='nicdark_btn nicdark_bg_green medium white nicdark_press') 
#         # print(s.get('href'))
#         url = s.get('href')
#         # saving to file
#         if res_status == 200:
#             www = os.path.join(save_path, "integra-wyjazdy.html")
#             file = open(www, 'w')
#             file.write(str(soup.prettify()))
#             file.close()
#         responsee(url)
#     except AttributeError:
#         print("end")
