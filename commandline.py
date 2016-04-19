import  getopt
import  sys

from torrentHandling.configs import Config
from torrentHandling.TorrentCrawler import TorrentProjectCrawler
from torrentHandling.UtorrentClient import UtorrentClient


def iterativeDownloading(name):
    list = name.split('-')
    if len(list) > 2 or len(list) < 1:
        raise IndexError('name is wrong')

    startName = list[0]
    index = startName.lower().rfind('e') + 1
    startIndex = int(startName[index:])
    endIndex = int(list[1])

    crawler = TorrentProjectCrawler()
    client = UtorrentClient(Config.UtorrentHost, Config._utorrentUser, Config._utorrentPassword)

    for i in range(startIndex, endIndex):
        curName = startName[:index] + format(i,'02')
        url, title, time, torUrl = crawler.GetLatestTorrent(curName)
        if client.SendTorrentLink(url=url) == 0:
             if client.SendTorrentLink(torUrl) == 0:
                 print title + " Failed"
             else:
                 print title + " Succeed"
        else:
            print title + " Succeed"

def singleDownloading(name, force):
     crawler = TorrentProjectCrawler()
     url, title, time, torUrl = crawler.GetLatestTorrent(name)
     if not force:
        isDownload = raw_input("Download " +  title + "(" + time + ") Y/N: ")
        if isDownload != 'Y' and isDownload != 'y':
            print "Canceled"
            return

     client = UtorrentClient(Config.UtorrentHost, Config._utorrentUser, Config._utorrentPassword)
     if client.SendTorrentLink(url=url) == 0:
         if client.SendTorrentLink(torUrl) == 0:
             print "Failed"
         else:
             print "Succeed"
     else:
        print "Succeed"

def main():

    if len(sys.argv) == 1:
        print "you should add on of the next params"
        print "-n [Name of Show]"
        print "-m [multiple download of Show eg. -m S01E10-12]"
        print "-f force download the show"
        print "-c config file (used instead)"
    else:
        force = False
        name = ''
        optlist, args = getopt.getopt(sys.argv[1:], 'm:n:fc:')
        multi = False
        for opt, arg in optlist:
            if opt == '-f':
                force = True
            if opt == '-n':
                name = arg
            if opt == '-m':
                name = arg
                multi = True

        if multi == True:
            iterativeDownloading(name)
        else:
            singleDownloading(name, force)


if __name__ == "__main__":
    main()
