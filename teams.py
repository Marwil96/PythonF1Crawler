
from wikitables import import_tables
import wikipedia
import json
import requests

allTeamsTable = import_tables('List_of_Formula_One_constructors')

teams = []
for row in allTeamsTable[0].rows:
	teams.append(( {
    "name": '{Constructor}'.format(**row), 
    "engine": '{Engine}'.format(**row), 
    "from": '{Based in}'.format(**row), 
    "seasons": '{Seasons}'.format(**row),    
    "race_entries": '{Races Entered}'.format(**row),
    "race_start": '{Races Started}'.format(**row),
    "drivers": '{Drivers}'.format(**row),
    "total_entries": '{Total Entries}'.format(**row),
    "wins": '{Wins}'.format(**row),
    "points": '{Points}'.format(**row),
    "poles": '{Poles}'.format(**row),
    "fastest_laps": '{FL}'.format(**row),    
    "wcc": '{WCC}'.format(**row),
    "wdc": '{WDC}'.format(**row),
    "related_teams": '{Antecedent teams}'.format(**row),
    "active": True,
   }))

for row in allTeamsTable[1].rows:
  teams.append(( {
  "name": '{Constructor}'.format(**row), 
  "engine": 'undefined', 
  "from": '{Licensed in}'.format(**row), 
  "seasons": '{Seasons}'.format(**row),    
  "race_entries": '{Races Entered}'.format(**row),
  "race_start": '{Races Started}'.format(**row),
  "drivers": '{Drivers}'.format(**row),
  "total_entries": '{Total Entries}'.format(**row),
  "wins": '{Wins}'.format(**row),
  "points": '{Points}'.format(**row),
  "poles": '{Poles}'.format(**row),
  "fastest_laps": '{FL}'.format(**row),    
  "wcc": '{WCC}'.format(**row),
  "wdc": '{WDC}'.format(**row),
  "first_grand_prix": '{First Grand Prix}'.format(**row),
  "last_grand_prix": '{Last Grand Prix}'.format(**row),
  "active": False
  }))

for team in teams:
  try:
    # driverData = wikipedia.page(wikipedia.search('{name}'.format(**driver))[0])
    teamData = wikipedia.WikipediaPage('{name}'.format(**team))
    print(teamData)

  except:
      pass  # doing nothing on exceptio


	

# print(teams)
# with open('teams.json', 'w') as outfile:
#     json.dump(teams, outfile)
