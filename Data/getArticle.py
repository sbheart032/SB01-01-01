import urllib.request
import bs4
import re

def getArticle(vUrl):
    url = vUrl
    
    try:
        html = urllib.request.urlopen(url)
    except HTTPError as e:
        return "F"

    bsObj = bs4.BeautifulSoup(html, "html.parser")

    try:
        vFindArticle = ""
        vArticle = bsObj.find("section", class_="center1080 position_r").find_all("div",class_="news_body")
            
        for p in vArticle:
            if "".join(p.find_all(text = True)) not in vFindArticle:
                vFindArticle += "\n" + "".join(p.find_all(text = True)).strip()
        return vFindArticle
                    
    except Exception as r:
        return "F"
        
