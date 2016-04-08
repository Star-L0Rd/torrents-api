import  getopt
import  sys

from torrentHandling.configs import Config
from torrentHandling.TorrentCrawler import TorrentProjectCrawler
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


        crawler = TorrentProjectCrawler()
        url, title, time = crawler.GetLatestTorrent(name)
        if not force:
            isDownload = raw_input("Download " +  title + "(" + time + ") Y/N: ")
            if isDownload != 'Y' and isDownload != 'y':
                print "Canceled"
                return

        client = UtorrentClient(Config.UtorrentHost, Config._utorrentUser, Config._utorrentPassword)
        client.SendTorrentLink(url=url)


if __name__ == "__main__":
    main()
