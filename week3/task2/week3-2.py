import urllib.request as movie
good = []
normal = []
bad = []
def getData(url):
    request=movie.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    })
    with movie.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #print(data)
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")
    titles=root.find_all("div", class_="title")
    #print(titles)
    for title in titles:
        #print(title.a.string)
        if title.a !=None and "Re:" not in title.a.string and "[好雷]" in title.a.string:
            good.append(title.a.string)
        elif title.a !=None and "Re:" not in title.a.string and "[普雷]" in title.a.string:
            normal.append(title.a.string)
        elif title.a !=None and "Re:" not in title.a.string and "[負雷]" in title.a.string:
            bad.append(title.a.string)
   
    #with open("movie.txt", mode="a", encoding="utf-8") as file:
        #file.write(str(good)+"\n")

    nextLink = root.find("a", string="‹ 上頁")
        #print(nextLink["href"])
    return nextLink["href"]
pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
#print(pageURL)
with open("movie.txt", mode="w", encoding="utf-8") as file:
    for good in good:
        file.write(str(good)+"\n")
    for normal in normal:
        file.write(str(normal)+"\n")
    for bad in bad:
        file.write(str(bad)+"\n")


