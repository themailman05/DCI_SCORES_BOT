'''
Created on Jul 17, 2014
Module for pulling scores from a DCI.org score page
@author: Liam
'''

from BeautifulSoup import BeautifulSoup
from urllib import urlopen
from collections import OrderedDict
import praw



class ScorePuller:
    def __init__(self, id):
        self.id = id
        self.url = "http://www.dci.org/scores/index.cfm?event=%s&year=2014" % self.id
        self.pagesoup = BeautifulSoup(urlopen(self.url))
        self.title = self.scrapetitle()
        self.results =  self.scrapescores()
    def scrapescores(self):
        print "Scraping scores from " + self.url
        corpsnames = self.pagesoup.findAll("td", width = "400")
        corpsscores = self.pagesoup.findAll("td", width = "75", )
        participating_corps = []
        corps_scores = []
        for name in corpsnames:
            participating_corps.append(name.text)
            for score in corpsscores:
                if len(score.text) > 2:
                    corps_scores.append(score.text)
        results = OrderedDict(zip(participating_corps, corps_scores))
        return results
    def scrapetitle(self):
        print "Scraping title from " + self.url
        showtitle = self.pagesoup.find("title").text[12:]
        return showtitle
    
    
    
'''
Created on Jul 17, 2014
Module for posting scores to reddit
@author: Liam
'''

class ScorePoster:
    def __init__(self, uname, pword, subreddit, ScorePuller, ListHandler):
        self.subreddit = subreddit
        self.id = ScorePuller.id
        self.title = ScorePuller.title
        self.results = ScorePuller.results
        self.ListHandler = ListHandler
        self.UAString = 'DCI_SCORES_BOT v0.1 by u/drum_code'
        self.score_permalink = "http://www.dci.org/scores/index.cfm?event=%s&year=2014" % self.id
        self.recap_permalink = "http://www.dci.org/scores/recap/recap_window.cfm?event=%s" % self.id
        self.uname = uname
        self.pword = pword
        self.redditsession = self.reddit_login()
        self.postString = "###" + self.title + "\n"
    def __unicode__(self):
        return self.postString
    def reddit_login(self):
        reddit = praw.Reddit(self.UAString)
        reddit.login(self.uname, self.pword)
        print reddit
        return reddit
    def populatepost(self):
        counter = 1
        for result in self.results:
            self.postString += str(counter) + ". **" + result + "** : " + self.results.get(result) + "\n"
            counter += 1
        self.postString += "\n\n\n\n *Please note: World and Open class corps are judged on the same sheets.* \n\n\n\n - [DCI.org permalink](" \
            +self.score_permalink +") \n\n - [RECAP]("+self.recap_permalink + ") \n\n - *THIS BOT IS IN BETA - send thoughts, concerns, suggestions " \
            "to [/u/drum_code](http://www.reddit.com/u/drum_code)*\n\n - *Check out the source code @ [Github](https://github.com/themailman05/DCI_SCORES_BOT) *\n\n "
    def post(self):
        self.redditsession.submit(self.subreddit, "DCI RESULTS: " + self.title, text = self.postString)
        self.ListHandler.add(self.id)
