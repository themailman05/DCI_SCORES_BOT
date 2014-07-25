from BeautifulSoup import BeautifulSoup
from urllib import urlopen

class SiteScraper:
    def __init__(self, listhandler):
        self.lh = listhandler
    def scrape(self):
        soup = BeautifulSoup(urlopen('http://www.dci.org/scores/'))
        results = soup.findAll('option')
        results_tags = []
        oldshows = self.lh.currentshowlist
        for show in results:
            results_tags.append(show['value'])
        newshows  = set(results_tags) - set(oldshows)
        print newshows
        return list(newshows)
        
