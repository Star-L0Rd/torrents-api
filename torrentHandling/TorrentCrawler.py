import requests
from lxml import html

class TorrentProjectCrawler:

    domain = "https://torrentproject.se/"
    def GetLatestTorrent(self, name):
        url = self.domain + '?s=' + name + '&orderby=best'
        page = requests.get(url)
        tree = html.fromstring(page.content)
        url = tree.xpath('//div[@class="torrent"]/h3/a')[0].attrib['href']
        time = tree.xpath('//div[@class="torrent"]/div/span[@class="bc cated"]')[0].text
        url = self.domain + 'torrent/' + url.split('/')[3].upper() + ".torrent"
        return url, tree.xpath('//div[@class="torrent"]/h3/a')[0].attrib['title'], time
        # print page.content
        # listNames = tree.xpath('//div[@id="download"]/div/div/a/text()')




