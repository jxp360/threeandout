#!/usr/bin/env python

''' This file can be used to populate a local database with nfl players info, however it uses Mongo, which is not supported by threeandout at this point '''

import datetime

import pymongo

if __name__ == "__main__":

    client = pymongo.MongoClient('localhost', 27017)
    db = client['threeandout_test']
    ffl = db['ffl_players_test']
    nfl = db['nfl_players_test']

    #Populate the players
    nfl_players = [
               {'name': 'Tom Brady',
                'position': 'QB', 
                'stats' : [{ 'week': 1, 'yard': 300, 'tds': 2, 'score': 34},
                           { 'week': 2, 'yard': 200, 'tds': 1, 'score': 24},
                           { 'week': 3, 'yard': 100, 'tds': 0, 'score': 14}
                          ]
               },
               {'name': 'Peyton Manning',
                'position': 'QB', 
                'stats' : [{ 'week': 1, 'yard': 300, 'tds': 2, 'score': 34},
                           { 'week': 2, 'yard': 200, 'tds': 1, 'score': 24},
                           { 'week': 3, 'yard': 100, 'tds': 0, 'score': 14}
                          ]
               },
               {'name': 'Robert Griffin III',
                'position': 'QB', 
                'stats' : [{ 'week': 1, 'yard': 300, 'tds': 2, 'score': 74},
                           { 'week': 2, 'yard': 200, 'tds': 1, 'score': 64},
                           { 'week': 3, 'yard': 100, 'tds': 0, 'score': 54}
                          ]
               }
              ]

    ffl_players = [
                   {'name': 'Jeff Pfeiffenberger', 
                    'email': 'jxp360@gmail.com', 
                    'league': 1,
                    'picks': [{ 'week': 1, 'qb': 'Peyton Manning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 86, 'time': datetime.datetime.utcnow()},
                             { 'week': 2, 'qb': 'Meyton Panning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 86, 'time': datetime.datetime.utcnow()},
                             { 'week': 3, 'qb': 'Thomas Brady', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 86, 'time': datetime.datetime.utcnow()}]
                   },
                   {'name': 'Grant Faiks', 
                    'email': 'grant.faiks@gmail.com', 
                    'league': 1,
                    'picks': [{ 'week': 1, 'qb': 'Peyton Manning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 76, 'time': datetime.datetime.utcnow()},
                             { 'week': 2, 'qb': 'Meyton Panning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 76, 'time': datetime.datetime.utcnow()},
                             { 'week': 3, 'qb': 'Thomas Brady', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 76, 'time': datetime.datetime.utcnow()}]
                   },
                   {'name': 'Bryan Gregory', 
                    'email': 'bsg@gmail.com', 
                    'league': 1,
                    'picks': [{ 'week': 1, 'qb': 'Peyton Manning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 56, 'time': datetime.datetime.utcnow()},
                             { 'week': 2, 'qb': 'Meyton Panning', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 56, 'time': datetime.datetime.utcnow()},
                             { 'week': 3, 'qb': 'Thomas Brady', 'rb': 'Adrian Peterson', 'wr': 'Andre Johnson', 'score': 56, 'time': datetime.datetime.utcnow()}] 
                   }
                ]
    ffl.insert(ffl_players)
    nfl.insert(nfl_players)

     

                           
