import mechanize
from BeautifulSoup import BeautifulSoup

class NflScraper(object):
  """ Scrape off statistics from nfl.com
  """
  URL = 'http://www.nfl.com/stats/weeklyleaders?week=%(week)s&season=%(season)s&showCategory=%(category)s'
  #here are the three catagories we care about
  CATEGORIES = ('Passing','Rushing','Receiving')
  #here are the guys which are duplicate across some catagories
  DUPS = ('Att', 'Yds', 'TD', 'Avg')
  def __init__(self):  
      #MMM...Cookie
      self.cj = mechanize.CookieJar()
      self.week=None
      self.year=None
      self.players={}

  def scrapeWeek(self, weekNum, year):
      #get predictions for the requested week
      self.week =weekNum
      self.year = year
      self.players={}
      self._scrapeAll()    
      return self.players
  
  def _getUrl(self, pos):
      #get the generic url we are using to scrape with given our current settings
      d = {'category' : pos,
           'week'     : self.week,
           'season'   : self.year}
      return self.URL %d

  def _scrapeAll(self):
      #we scrape all the catagories we care about adding the players into the dictionary
      for key in self.CATEGORIES:
          self._scrapeCategory(key)

  def _scrapeCategory(self, pos):
      """get the stats for a specific catagory
      """
      url = self._getUrl(pos)
      self._scrapeUrl(url, pos)
  
  def convert(self, val):
      """ convert a unicode string 
      """
      try:
          #first try int
          return int(val)
      except ValueError:  
          try:
              #then try float
              return float(val)
          except ValueError:
              #settle on a string
              return str(val)	  
      
  def _scrapeUrl(self, url, pos):
      """scrape a generic url
      """
      #grab the data -- go internets!
      request3 = mechanize.Request(url)
      self.cj.add_cookie_header(request3)
      response3 = mechanize.urlopen(request3)
      maincontent = response3.read()
      #make the soup
      soup = BeautifulSoup(maincontent)
      
      #parse the soup
      #get all the rows from the table
      rows = soup.findAll('tr')
      #the first row has the columns
      columns= [str(x.text) for x in rows[0]('th')]
      #the rest of the rows have the player data
      for player in rows[1:]:
          playerData=  [x.text for x in player('td')] #grab all the player data here
          d={}
          for key, value in zip(columns, playerData):
              if key in self.DUPS:
                  #make the key unique if we need to by prepending the position
                  key = "%s_%s" %(pos,key)
              d[key]=self.convert(value)
              old = self.players.setdefault(d['Name'],{})
              if old.has_key('FUM') and d.has_key('FUM'):
                  #i'm 99% sure fumbles are scored in both rushing and passing and 
                  #they are duplicate so the values should be the same
                  assert(old['FUM']==d['FUM'])
              #update our new info
              old.update(d)          
	 

if __name__=="__main__":
    import sys
    s = NflScraper()
    #predictions = s._scrapeUrl(s.SEASON%0)
    for i in xrange(1,23):
        predictions = s.scrapeWeek(i,2012)
        #predictions =  s.scrapeSeason()
        print predictions
