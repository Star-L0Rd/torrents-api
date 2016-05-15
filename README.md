# torrents_api
search and upload torrents to utorrent api within one quick step 

the torrents downloaded from https://torrentproject.se
and uploaded to utorrent web api (check how to configure web api in http://www.utorrent.com)

command line usage:
arguments (just run the commandline.py without arguments to get help)  
-n [Name of Show]  <br /> 
-f force download the show  (usually it will ask if the torrent correct)  
-c config file (used instead)  
-m [multiple download of Show eg. -m S01E10-12]


don't forget to update the config.cfg file (configuration):  
host = [host url of the utorrent web api]  
user = [utorrent web api user]  
password = [utorrent password]  

e.g. (using the commandline script)

commandline.py -n guardians+2014+hdtv  
Download Guardians of the Galaxy (2014) 720p HDTV XviD AC3 VAiN torrent Y/N: y   
(* It will prompt if you want add this link)  
Added Sucessfully





