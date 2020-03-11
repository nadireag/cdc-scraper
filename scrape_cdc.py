# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# create scrape function
def scrape():
    browser = init_browser()

    # use browser to open the url 
    url = "https://www.cdc.gov/"

    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # grab the first info and the image in the page
    info  = soup.find("div",  class_="jumbotron")
    info_p = info.find_all("p")
    # p_list = []
    for p in info_p:
        par = p.text
        # p_list.append(parag)
    
    img = info("img")
    for i in img:
        pic="https://www.cdc.gov" + i["src"]
    
    # print(card)
    
    # get the images, headers and text related to each image
    card = soup.find("div", class_="match-height")
    
    # create a list that holds relative ifo
    card_data = []
    for i in card:
        card_info = i.find("a", class_="bt-5")
        # print(card_info)

        card_img = i("img")
    
        for img in card_img:
            image = "https://www.cdc.gov" + img["src"]
            # images.append(image)
            
    

        card_header = i("div", class_="card-title")
    
        for header in card_header:
            # titles.append(header.text)
            titles = header.text
        
    
        paragraph = i("p")
        for p in paragraph:
            # parag.append(p.text)
            parag = p.text

        # create the dictionary to hold secondary data
        card_data.append({"card_img": image, "card_titles":titles, "card_text": parag})

    # grab the outbreaks info

    outbreak = soup.find("ul", class_="mb-0")
    header = soup.find_all("div", class_="card-header h4 bg-white")[0].text
    # print(header)

    item_list = []
    for i in outbreak:
        items = i.text
        item_list.append(items)
        
    # print(item_list)

    
    # create the dictionary to  hold the data
    cdc_data = {
        "first_img": pic,
        "first_info": par,
        "card_data": card_data,
        "header": header,
        "item_list":item_list
    }

    # quit browser
    browser.quit()

    return  cdc_data


        