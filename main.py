import requests as rs
import os
from lxml import etree

def getHTML(webUrl):
    html_doc = rs.get(webUrl).text
    return etree.HTML(html_doc)

def downLoadPic(imgUrls):
    pictures = {}
    for i in imgUrls:
        picUrl = getHTML(i).xpath('//div[@class="scrollbox"]/img/@src')
        if(len(picUrl)>0):
            # print(picUrl)
            picData = rs.get(picUrl[0], timeout=6)
            pictures[picUrl[0][31:]] = picData

    return pictures

    
def saveFile(pictures):
    for key, value in pictures.items():
        with open(os.path.dirname(__file__)+'\\source\\'+key,'wb') as f:
            for image in value.iter_content(100000):
                f.write(image)



def main():
    print("One_Round_Start")
    #create an empty directory
    if not os.path.isdir('source'):
        os.mkdir('source')

    parentUrl = "https://wallhaven.cc/search?q=girl&categories=010&purity=100&atleast=3840x2400&sorting=random&order=desc&colors=ea4c88"

    # parentUrl = "https://wallhaven.cc/hot"

    imgs = getHTML(parentUrl).xpath('//section[@class="thumb-listing-page"]/ul/li/figure/a[@class="preview"]/@href')
    
    pictureDatas = downLoadPic(imgs);
    saveFile(pictureDatas)

    print("One_Round_Finish")



for i in range(3):
    main()



