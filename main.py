from urllib.request import urlopen
from bs4 import BeautifulSoup
import random


knifebudget = int(input('What is your budget? '))

if knifebudget < 100:
    print('Sorry mate! Knives are not cheap!') 

quote_page = ["https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730", "https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730#p2_default_desc", "https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730#p3_default_desc", "https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730#p4_default_descv", "https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730#p5_default_desc", "https://steamcommunity.com/market/search?q=knife&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Quality%5B%5D=tag_strange&appid=730#p6_default_desc"]

for i in range(len(quote_page)):
  

  page = urlopen(quote_page[5])

  soup = BeautifulSoup(page, 'html.parser')

  results = soup.find_all("div", {"class": "market_listing_row market_recent_listing_row market_listing_searchresult"})

  affordable_knives = []

  for item in results:
    name = item.find("span", {"class": "market_listing_item_name"}).get_text()

    price = int((item.find("span", {"class": "normal_price"}).find("span", {"class": "normal_price"}).get("data-price"))) / 100

    print(name + " : " + str(price) + " US Dollars")

    if price < knifebudget:
        affordable_knives.append([name, price])
    elif knifebudget < 100:
        affordable_knives.append('Nothing' if random.randrange(2) == 0 else 'nada')


print("You can afford the following: ")

for knife in affordable_knives:
  print(knife)

