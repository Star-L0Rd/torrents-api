import requests
from configs import Config
from lxml import html

class TorrentProjectCrawler:

    domain = Config.TorrentRepositoryHost
    def GetLatestTorrent(self, name):

        #get the torrent we are looking for and its properties
        url = self.domain + '?s=' + name + '&orderby=best'
        page = requests.get(url)
        tree = html.fromstring(page.content)

        url = tree.xpath('//div[@class="torrent"]/h3/a')[0].attrib['href']
        time = tree.xpath('//div[@class="torrent"]/div/span[@class="bc cated"]')[0].text
        title = tree.xpath('//div[@class="torrent"]/h3/a')[0].attrib['title']
        torUrl = ''

        #now lets get the torrent magnet link
        page = requests.get(url)
        tree = html.fromstring(page.content)
        nodes = tree.xpath('//div[@class="usite"]/a')
        for n in nodes:
            if n.attrib['href'].find('magnet') >= 0:
                url = n.attrib['href']
            else:
                torUrl = n.attrib['href']

        #add http for '//' urls -> torrent client doesn't know how to work with that
        if torUrl.find('//') == 0:
            torUrl = 'http:' + torUrl
        return url, title, time, torUrl





