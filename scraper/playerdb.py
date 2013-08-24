#Things having to do with nfl players and databases

import sqlite3

class NflPlayerDb(object):
  STRUCTURE = (('id','integer primary key autoincrement'), ('Name', 'text'),('Team', 'text'), ('Position', 'text')) 
  KEYS = [x[0] for x in STRUCTURE]
  TABLE = 'Player'
  def __init__(self, dbName,open=True):
    self.dbName = dbName
    if open:
      self.open()
    else:
      self.conn = None
  def open(self): 

    self.conn = sqlite3.connect(self.dbName)
    c = self.conn.cursor()
    s = ','.join(["%s %s"%x for x in self.STRUCTURE])
    c.execute('''CREATE TABLE if not exists %s
             (%s)'''%(self.TABLE, s))  
    self.conn.commit()  
 
  def close(self):
    if self.conn:
      self.conn.close()
      self.conn = None

  def __del__(self):
    self.close()

  def insertPlayers(self, l):
    if not self.conn:
      self.open()
    c = self.conn.cursor()
    tuples =[]
    insertVals = [key for key in  self.KEYS if key!='id']
    for d in l:
      tuples.append(tuple(d[key] for key in insertVals))
    keyString = ','.join(insertVals)
    questionStr = ','.join("?"*len(insertVals))
    executeStr= "INSERT INTO %s (%s) VALUES (%s) "%(self.TABLE, keyString, questionStr)
    c.executemany(executeStr, tuples)
    self.conn.commit()

  def getPlayers(self, **args):
    if not self.conn:
      self.open()
    c = self.conn.cursor()
    if args:
        selectStr = " and ".join(["%s=:%s" %(x,x) for x in args.keys()])
        queryStr = 'SELECT *  FROM %s WHERE %s' %(self.TABLE,selectStr)
    else:
        queryStr = 'SELECT *  FROM %s' %self.TABLE
    
    c.execute(queryStr, args)
    res = c.fetchall()
    out = []
    for row in res:
      d={}
      for key, value in zip(self.KEYS, row):
        d[key]=value
      out.append(d)
      
    return out

if __name__=='__main__':
  import nflstats
  scrapePlayers = True #for initial scraping to create the player table
  playerDb = NflPlayerDb('players.db')
  if scrapePlayers:
    s = nflstats.NflScraper()  
    stats = s.scrapeWeek(1,2013)
    playerDb.insertPlayers(stats)
    playerDb.close()
  else:
   players = playerDb.getPlayers(Team='GB')
   for row in players:
     print row


