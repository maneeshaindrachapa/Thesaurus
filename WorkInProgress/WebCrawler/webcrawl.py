from lxml import html
import requests

class WebCrawl:
    def __init__(self,starting_url,depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth =0
        self.depth_links =[]
        self.apps =[]

    def crawl(self):
        app =self.get_app_link(self.starting_url)
        self.apps.append(app)
        self.depth_links.append(app.links)

        while(self.current_depth<self.depth):
            current_links =[]
            for link in self.depth_links[self.current_depth]:
                current_app = self.get_app_link(link)
                current_links.extend(current_links)
                self.apps.append(app)
            self.current_depth +=1
            self.depth_links.append(current_links)
        return;
    
    def get_app_link(self,link):
        start_page =requests.get(link)
        tree = html.fromstring(start_page.text)

        name =tree.xpath('//h1/text()')[0]
        details = tree.xpath('//p/text()')
        links =tree.xpath('//p//a/@href')
        temp =[]
        for link in links:
            if(link[0:5] == '/wiki'):
                link = "https://en.wikipedia.org/"+link
                temp.append(link)
        print(details)
        app =App(name,temp)
        return app

class App:
    def __init__(self,name,links):
        self.name=name
        self.links=links

    #def __str__(self):
     #   return (self.name.encode("ascii"))


crawler =WebCrawl("https://si.wikipedia.org/wiki/%E0%B7%83%E0%B7%92%E0%B6%82%E0%B7%84%E0%B6%BD_%E0%B6%B7%E0%B7%8F%E0%B7%82%E0%B7%8F%E0%B7%80",5)
crawler.crawl()

for app in crawler.apps:
    print(app)

