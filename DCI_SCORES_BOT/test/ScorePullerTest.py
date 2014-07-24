'''
Created on Jul 18, 2014

@author: Liam
'''
import unittest
from DCI_SCORES_BOT import ScoreUtils
from collections import OrderedDict


class Test(unittest.TestCase):

    def setUp(self):
        self.sp = ScoreUtils.ScorePuller('http://www.dci.org/scores/index.cfm?year=2014&event=06b03625-0049-40ea-b040-8047ae6673dc')
        

    def testResults(self):
        self.setUp()
        od = OrderedDict([(u'Carolina Crown', u'88.350'), (u'Bluecoats', u'87.850'), (u'Santa Clara Vanguard', u'87.350'),\
                           (u'The Cavaliers', u'85.450'), (u'Oregon Crusaders', u'74.100'), (u'The Academy', u'74.100'), \
                           (u'Pacific Crest', u'73.900'), (u'Mandarins', u'72.250'), (u'Jersey Surf', u'69.000'), \
                           (u'Cascades', u'67.500'), (u'Pioneer', u'64.400')])
        results = self.sp.results
        self.assertEquals(results, od, 'OrderedDicts do not match' )
        
    def testTitle(self):
        self.setUp()
        title = '7/17/14 - Denton TX (DCI Denton presented by CoServ Electric for Red River Thunder)'
        self.assertEquals(title, self.sp.title)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()