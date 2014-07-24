'''
Created on Jul 17, 2014

@author: Liam
'''
import unittest
from DCI_SCORES_BOT import ListHandler

class Test(unittest.TestCase):
    
    
    def setUp(self):
        self.lh = ListHandler.ListHandler('ListHandlerTest1.txt')
        self.lh.wipe()
        self.rlh = ListHandler.ListHandler('ListHandlerTest2.txt')
        self.rlh.wipe()
        self.rlh.add('test')
        
        

    def testgetshowlist(self):
        self.setUp()
        showlist = self.lh.getshowlist()
        self.assertEquals(showlist, [], "List should be empty" + str(showlist))
        
    def testloadedfile(self):
        self.setUp()
        res = self.rlh.getshowlist()
        self.assertEquals(res, ['test'])
        
    def testadd(self):
        self.setUp()
        strings = ['test1', 'test2']
        for string in strings:
            self.lh.add(string)
        showlist = self.lh.getshowlist()
        self.assertEquals(strings, showlist)
        
        
    def testwipe(self):
        strings = ['test1', 'test2']
        for string in strings:
            self.lh.add(string)
        self.lh.wipe()
        self.assertEquals(self.lh.getshowlist(), [], "File was not wiped")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()