'''
Module for Talking to serialized lists of DCI show url extensions
by Liam 
'''


import cerealizer

class ListHandler:
    def __init__(self, filename):
        self.filename = filename
        self.currentshowlist = self.getshowlist()
    def getshowlist(self):
        try:
            with open(self.filename, 'rb') as readfile:
                showlist = cerealizer.load(readfile)
        except:
            with open(self.filename, 'wb') as newfile:
                cerealizer.dump([], newfile)
                newfile.flush()
                showlist = []
        return showlist
    def add(self, url):
        self.currentshowlist.append(url)
        print "Adding " + url +" to list\n"
        self.dumplist()
    def dumplist(self):
        with open(self.filename, 'wb') as outfile:
            cerealizer.dump(self.currentshowlist, outfile)
    def wipe(self):
        print "wiping current showlist"
        self.currentshowlist = []
        self.dumplist()