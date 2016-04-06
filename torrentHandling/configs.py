import ConfigParser

class Configs:
    TorrentRepositoryHost = ""
    UtorrentHost = ""
    _utorrentUser= ""
    _utorrentPassword =""

    def __init__(self):
        config = ConfigParser.RawConfigParser()
        config.read('torrentHandling\config.cfg')
        self.TorrentRepositoryHost =  config.get('TorrentRepository', 'torrent_repository_host')
        self.UtorrentHost =  config.get('Utorrent', 'host')
        self._utorrentUser =  config.get('Utorrent', 'user')
        self._utorrentPassword =  config.get('Utorrent', 'password')



global Config
Config = Configs()