import  getopt
import  sys

from torrentHandling import TorrentCrawler
from torrentHandling.UtorrentClient import UtorrentClient


def main():

    if len(sys.argv) == 1:
        print "you should add on of the next params"
        print "-n [Name of Show]"
        print "-f force download the show"
        print "-c config file (used instead)"
    else:
        force = False
        name = ''
        optlist, args = getopt.getopt(sys.argv[1:], 'n:fc:')
        for opt, arg in optlist:
            if opt == '-f':
                force = True
            if opt == '-n':
                name = arg


        crawler = TorrentCrawler.TorrentProjectCrawler()
        url, title, time = crawler.GetLatestTorrent(name)
        if not force:
            isDownload = raw_input("Download " +  title + " Y/N: ")
            if isDownload != 'Y' and isDownload != 'y':
                print "Canceled"
                return

        client = UtorrentClient('http://salon:8080/gui', 'admin', 'alonbalon')
        client.SendTorrentLink(url=url)


if __name__ == "__main__":
    main()
