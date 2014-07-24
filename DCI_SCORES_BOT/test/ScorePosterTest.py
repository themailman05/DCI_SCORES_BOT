'''
Created on Jul 17, 2014

@author: Liam
'''
import unittest
from DCI_SCORES_BOT import ScoreUtils
from DCI_SCORES_BOT import ListHandler

reddituname = raw_input('Enter reddit username: ')
redditpword = raw_input('Enter reddit password: ')


class Test(unittest.TestCase):
    
    def setUp(self):
        self.listh = ListHandler.ListHandler('scoreposttest')
        self.sp = ScoreUtils.ScorePuller('http://www.dci.org/scores/index.cfm?year=2014&event=06b03625-0049-40ea-b040-8047ae6673dc')
        self.spp = ScoreUtils.ScorePoster(reddituname, redditpword, 'dciscores', self.sp, self.listh)
        
        
    def testBuildPost(self):
        self.setUp()
        self.spp.populatepost()
        ansstring = '###7/17/14 - Denton TX (DCI Denton presented by CoServ Electric for Red River Thunder)\n1. **Carolina Crown** : 88.350'\
        '\n2. **Bluecoats** : 87.850\n3. **Santa Clara Vanguard** : 87.350\n4. **The Cavaliers** : 85.450\n5. **Oregon Crusaders** : 74.100\n6.'\
        ' **The Academy** : 74.100\n7. **Pacific Crest** : 73.900\n8. **Mandarins** : 72.250\n9. **Jersey Surf** : 69.000\n10. **Cascades** : 67.500'\
        '\n11. **Pioneer** : 64.400\n\n\n\n\n *Please note: World and Open class corps are judged on the same sheets.* \n\n\n\n - '\
        '[DCI.org permalink](http://www.dci.org/scores/index.cfm?event=http://www.dci.org/scores/index.cfm?year=2014&event=06b03625-'\
        '0049-40ea-b040-8047ae6673dc&year=2014) \n\n - [RECAP](http://www.dci.org/scores/recap/recap_window.cfm?event=http://www.dci.org'\
        '/scores/index.cfm?year=2014&event=06b03625-0049-40ea-b040-8047ae6673dc) \n\n - *THIS BOT IS IN BETA - send thoughts, concerns, '\
        'suggestions to [/u/drum_code](http://www.reddit.com/u/drum_code)*'

        string = self.spp.postString
        self.assertEquals(string, ansstring)


if __name__ == "__main__":
    import sys;sys.argv = ['', 'Test.testName']
    unittest.main()