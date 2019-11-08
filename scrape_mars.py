# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import pymongo

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    mission_mars_data = {}
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    news_title = soup.find("div", class_="content_title").text
    news_p = soup.find("div", class_="rollover_description_inner").text

# Visit the url for JPL Featured Space Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    print(featured_image_url)

#Scrape the latest Mars weather tweet from the page
    tweet_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(tweet_url)
    browser = Browser('chrome', headless=False)
    html = browser.html
    soup = bs(tweet_html, "html.parser")

#Getting mars weather
    mars_weathers = []
    for weather_info in tweet_soup.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        mars_weathers.append(weather_info.text.strip())
        mars_weather = mars_weathers[0]
        mars_weather

# Visit /getting the Mars Facts webpage
    facts_url = "https://space-facts.com/mars/"
    fact_list = pd.read_html(facts_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    facts_df = fact_list[0]
    facts_table = facts_df.to_html(header=False, index=False)
    print(facts_table)

# Mars Hemispheres
    usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(usgs_url)
    usgs_html = browser.html
    usgs_soup = bs(usgs_html, 'html.parser')
    hemisphere_image_urls = []                                                  

    products = usgs_soup.find('div', class_='result-list')                       
    hemispheres = products.find_all('div', class_='item')                        

    for hemisphere in hemispheres:                                              
        title = hemisphere.find('div', class_='description')
    
        title_text = title.a.text                                                
        title_text = title_text.replace(' Enhanced', '')
        browser.click_link_by_partial_text(title_text)
    
    usgs_html = browser.html 
    usgs_soup = bs(usgs_html, 'html.parser')
    
    image = usgs_soup.find('div', class_='downloads').find('ul').find('li')
    img_url = image.a['href']
    
    hemisphere_image_urls.append({'title': title_text, 'img_url': img_url})


    mission_mars_data = {
    "news_title": news_title,

    "news_p": news_p,

    "featured_img_url": featured_img_url,

    "mars_weather": mars_weather,

    "hemisphere_full_image": hemisphere_full_image
    }
    return mission_mars_data