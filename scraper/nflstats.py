import mechanize
from BeautifulSoup import BeautifulSoup

class NflScraper(object):
  """ Scrape off statistics from nfl.com
  """

  URL_A = 'http://fantasy.nfl.com/research/scoringleaders#researchScoringLeaders=researchScoringLeaders%2C%2Fresearch%2Fscoringleaders%253Foffset%253D'
  URL_B = '%2526position%253DO%2526sort%253Dpts%2526statCategory%253Dstats%2526statSeason%253D'
  URL_C = '%2526statType%253DweekStats%2526statWeek%253D'
  URL_D = '%2Creplace'

  URL = 'http://fantasy.nfl.com/research/scoringleaders?offset=%(index)s&position=O&sort=pts&statCategory=stats&statSeason=%(season)s&statType=weekStats&statWeek=%(week)s'

  def __init__(self):  
      #MMM...Cookie
      self.cj = mechanize.CookieJar()
      self.week=None
      self.year=None
      self.players=[]

  def scrapeWeek(self, weekNum, year):
      #get predictions for the requested week
      self.week =weekNum
      self.year = year
      self.players=[]
      self._scrapeAll()    
      return self.players
  
  def _getUrl(self, index):
      #get the generic url we are using to scrape with given our current settings
      d = {'index':index+1,
           'week':self.week,
           'season':self.year}
      return self.URL%d

  def _scrapeAll(self):
      #we scrape all the catagories we care about adding the players into the dictionary
      oldIndex =None
      index=0
      while oldIndex!=index:
          self._scrapeIndex(index)
          oldIndex= index
          index = len(self.players)

  def _scrapeIndex(self, index):
      """get the stats for a specific catagory
      """
      url = self._getUrl(index)
      print index
      print url
      return self._scrapeUrl(url)
  
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
              strVal = str(val)
              if strVal=='-':
                  return 0
              else:
                 return strVal
      
  def _scrapeUrl(self, url):
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
      if not rows:
          return False
      #the column headers are in the second row
      columns = [str(x.text) for x in rows[1]('th')]
      #uniquify Yds & TD since they are used for passing, rushing and receiving"
      hdrs = [str(x.text) for x in rows[0]('th')]
      hdrs = [x for x in hdrs if x !='&nbsp;']
      prefixes = hdrs[:3] # first 3 are the ones we care about
      for prefix in prefixes:
          for label in ("Yds", "TD"):
              index = columns.index(label)
              columns[index]=prefix+"_"+label
      #the rest of the rows have the player data
      for player in rows[2:]:
          playerData=  [x.text for x in player('td')] #grab all the player data here
          d={}
          for key, value in zip(columns, playerData):
              d[key]=self.convert(value)
          playerStr = d['Player']
          try:
              first, second = playerStr.split(' - ')
          except ValueError:
              first = playerStr
              second = None
          if first.endswith('K'):
              endIndex= -1
          else:
              endIndex = -2
          d['Name']= first[:endIndex]
          print d['Name']
          d['Position'] = first[endIndex:]
          if second:
              viewIndex = second.find('View')
              if viewIndex==-1:
                  d['Team'] = second
              else:
                  d['Team'] = second[:viewIndex]
          else:
              d['Team']="None"
          self.players.append(d)
      return True	 

if __name__=="__main__":
    import sys
    s = NflScraper()
    #predictions = s._scrapeUrl(s.SEASON%0)
    predictions = s.scrapeWeek(1,2012)
    #predictions =  s.scrapeSeason()
    print predictions
