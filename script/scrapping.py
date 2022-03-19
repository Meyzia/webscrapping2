from selenium import webdriver
import urllib.request
import json
from datetime import datetime

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.goodreads.com/list/show/43.Best_Young_Adult_Books")

content = driver.find_element_by_class_name("tableList")

bookList = []
i = 1
while i<=100:
    for book in driver.find_elements_by_tag_name("tr"):
        print(book.text.split("\n"))
        img = book.find_element_by_tag_name("img")
        print(img.get_attribute("src"))
        urllib.request.urlretrieve(img.get_attribute("src"), str(i)+".jpg")
        i = i+1
        bookList.append(
            {"No": book.find_element_by_class_name("number").text.split("\n")[0],
            "Judul": book.find_element_by_class_name("bookTitle").text.split("\n")[0],
            "Author": book.find_element_by_class_name("authorName").text.split("\n")[0],
            "Rating": book.find_element_by_class_name("minirating").text.split("\n")[0],
            "Image": img.get_attribute("src"),
            "Waktu_scrap": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )
    
hasil_scraping = open("scrapping.json", "w")
json.dump(bookList, hasil_scraping, indent=6)
hasil_scraping.close()

driver.quit()
