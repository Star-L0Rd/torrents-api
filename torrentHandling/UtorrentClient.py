from lxml import html
import requests
import urllib
class UtorrentClient:
    _host = ''
    _token =''
    _user = ''
    _password = ''
    _session = requests.Session()

    def __init__(self, host, user , password):
        self._host = host
        self._user = user
        self._password = password
        response = self._session.get(self._host + '/token.html', auth=(self._user, self._password))
        tree = html.fromstring(response.content)
        self._token = tree.xpath('//div')[0].text


    def SendTorrentLink(self, url):
        result = self._session.get(self._host + '/?token=' + self._token + '&action=add-url&s=' + urllib.quote(url, safe='') ,
             auth=(self._user,self._password))
        if str(result).find('200') > 0:
            return 1
        else:
            return  0
