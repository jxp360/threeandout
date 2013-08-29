import mechanize
from BeautifulSoup import BeautifulSoup
import calendar
import datetime
import pytz

class ScheduleScraper(object):
  """ Scrape off statistics from nfl.com
  """

  URL = 'http://www.nfl.com/schedules/%(year)s/REG%(week)s'
  MONTH_MAP = dict((v,k) for k,v in enumerate(calendar.month_name))
  #someone made a typo
  print MONTH_MAP
  MONTH_MAP['septiembre'] = MONTH_MAP['September']
  KEYS = ('week', 'home', 'away', 'kickoff')
  EASTERN_TIME_ZONE= pytz.timezone('US/Eastern')
  #Lets keep the teams consistant from those used in the scrapers
  TEAM_MAP = {"Vikings"   :'MIN',
              "Dolphins"  :'MIA', 
              "Panthers"  :'CAR', 
              "Falcons"   :'ATL', 
              "Lions"     :'DET', 
              "Bengals"   :'CIN', 
              "Jets"      :'NYJ', 
              "Broncos"   :'DEN', 
              "Ravens"    :'BAL', 
              "Giants"    :'NYG', 
              "Raiders"   :'OAK', 
              "Titans"    :'TEN', 
              "Saints"    :'NO', 
              "Cowboys"   :'DAL', 
              "Patriots"  :'NE', 
              "Seahawks"  :'SEA', 
              "Browns"    :'CLE', 
              "Bills"     :'BUF', 
              "Steelers"  :'PIT', 
              "Rams"      :'STL', 
              "Bears"     :'CHI', 
              "Texans"    :'HOU', 
              "Packers"   :'GB', 
              "Redskins"  :'WAS', 
              "Jaguars"   :'JAC', 
              "Chiefs"    :'KC', 
              "Eagles"    :'PHI', 
              "Buccaneers":'TB', 
              "Colts"     :'IND', 
              "Cardinals" :'ARI', 
              "49ers"     :'SF', 
              "Chargers"  :'SD'}

  def __init__(self):  
      #MMM...Cookie
      self.cj = mechanize.CookieJar()
      self.week=None
      self.year=None
      self.games=[]

  def scrapeWeek(self, weekNum, year):
      #get predictions for the requested week
      self.week =weekNum
      self.year = year
      self.games=[]
      self._scrapeAll()    
      return self.games
  
  def _getUrl(self):
      #get the generic url we are using to scrape with given our current settings
      d = {'week':self.week,
           'year':self.year}
      return self.URL%d

  def _scrapeAll(self):
      #we scrape all the catagories we care about adding the players into the dictionary
      url = self._getUrl()
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
      #This thing is a beast

      # date/times and games are intersperced
      # The first thing should be a date
      # then all games following are on that date
      # So - we find all dates and games with our query and handle them
      # as they happen in order
      date=None
      tags = soup.findAll(**{'class':["schedules-list-date", 'schedules-list-hd pre', 'schedules-list-hd post']})
      print "found %s tags" %len(tags)
      for tag in tags:
        #we got a date!
        if tag['class']=='schedules-list-date':
          #we've found a new date
          gameDateStr = str(tag.find('span').text)
          monthStr, date = gameDateStr.split(',')[1].strip().split()
          monthNum = self.MONTH_MAP[str(monthStr)]
          if monthNum in (1,2):
            year = self.year+1
          else:
            year = self.year
          dateInt = int(''.join([x for x in date if x.isdigit()]))
          date = datetime.date(year, monthNum, dateInt) 
        else:
          #we've got a new game -parse out home and away team
          home = str(tag.find(**{'class':['team-name home ', 'team-name home lost']}).text)
          away = str(tag.find(**{'class':['team-name away ', 'team-name away lost']}).text)
          #need to get the time as well
          time = str(tag.find(**{'class':'time'}).text)
          if time=='FINAL':
            print "CANNOT GET VALID TIME FOR GAMES that are in the past" 
            hr=0
            minute=0
          else:
            hr, minute = time.split(':')
            amPm = str(tag.find(**{'class':['am', 'pm']}).text).strip()
            hr = int(hr)
            minute=int(minute)
            #adjust times to take into account am/pm  
            if amPm=="PM" and hr <12:      
              hr+=12
            if amPm=="AM" and hr==12:
              hr=0
          d={'week':self.week,
             'home':self.TEAM_MAP[home],
             'away':self.TEAM_MAP[away],
             'kickoff':datetime.datetime(date.year, date.month, date.day, hr, minute, tzinfo=self.EASTERN_TIME_ZONE)}
          self.games.append(d)

if __name__=="__main__":
    import sys
    s = ScheduleScraper()
    #predictions = s._scrapeUrl(s.SEASON%0)
    predictions = s.scrapeWeek(13,2013)
    #predictions =  s.scrapeSeason()
    print predictions
