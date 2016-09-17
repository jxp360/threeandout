import mechanize
from BeautifulSoup import BeautifulSoup

class NflScraper(object):
  """ Scrape off statistics from nfl.com
  """
  
  #week should be 18 for wild card, 19 for divisional, 20 for Conference 
  #category should be {Passing,Rushing,Receiving}
  #season should be the year of the football season (fall).  NOT the year of the playoffs in january
  URL = 'http://www.nfl.com/stats/weeklyleaders?week=%(week)s&season=%(season)s&showCategory=%(category)s'
  CATEGORIES = ('Receiving','Rushing','Passing')
  PLAYER_MAP={'Name':'name',
              'Team':'team',
              'Position':'position'}

  STATS_MAP={'Receiving_TD': 'recTd', 
             'FUM': 'fumbles', 
             'Int': 'interceptions', 
             'Passing_TD': 'passTd',
             'Passing_Yds': 'passYds',
             'Points': 'score',
             'FumTD': 'fumbleRecoveryTDs',
             'Rushing_Yds': 'rushYds', 
             'Receiving_Yds': 'recYds', 
             'Rushing_TD': 'rushTd'}

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
      self.playerHash={}
      self._scrapeAll()    
      return self.players
  
  def _getUrl(self, category):
      #get the generic url we are using to scrape with given our current settings
      d = {'category':category,
           'week':self.week,
           'season':self.year}
      return self.URL%d

  def _scrapeAll(self):
    for category in self.CATEGORIES:
      url =self._getUrl(category)
      self._scrapeUrl(url,category)
    self.players = self.playerHash.values()
    #compute the score for each player
    for player in self.players:
      score = player.get('Passing_Yds',0)/25.0+ 4*player.get('Passing_TD',0)-2*player.get('Int',0)+player.get('Rushing_Yds',0)/10.0+6*player.get('Rushing_TD',0)+player.get('Receiving_Yds',0)/10.0+6*player.get('Receiving_TD',0)-2*player.get("FUM")
      player['Points']=score
 
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
      
  def _scrapeUrl(self, url, prefix):
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
      table = soup.find('table')
      rows = table.findAll('tr')
      #the column headers are in the second row
      columns = [str(x.text) for x in rows[0]('th')]
      #uniquify Yds & TD since they are used for passing, rushing and receiving"
#      hdrs = [str(x.text) for x in rows[0]('th')]
#      hdrs = [x for x in hdrs if x !='&nbsp;']
#      prefixes = hdrs[:3] # first 3 are the ones we care about
      #for prefix in prefixes:
      for label in ("Yds", "TD"):
          index = columns.index(label)
          columns[index]=prefix+"_"+label
      #the rest of the rows have the player data
      for player in rows[1:]:
          playerData=  [x.text for x in player('td')] #grab all the player data here
          d={}
          for key, value in zip(columns, playerData):
              d[key]=self.convert(value)
          #I don't know why some of these guys don't have teams!
          if d['Team']=="":
            print "no team for %s" %d['Name']
            d.pop('Team')
            key = d['Name']
          else:
            key = d['Name']+d['Team']
          if self.playerHash.has_key(key):
            #NFL.com is listing fumbles in multiple places but they are the same
            #as such - don't add them together like I first thought or it registers too many fumbles
            #d['FUM']=d["FUM"]+self.playerHash[key]["FUM"]
            self.playerHash[key].update(d)
          else:
            self.playerHash[key]=d  

      return True	 

if __name__=="__main__":
    import sys
    s = NflScraper()
    #predictions = s._scrapeUrl(s.SEASON%0)
    predictions = s.scrapeWeek(19,2012)
    #predictions =  s.scrapeSeason()
    print predictions
