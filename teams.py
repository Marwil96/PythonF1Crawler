
from wikitables import import_tables
import wikipedia
import json
import requests

allTeamsTable = import_tables('List_of_Formula_One_constructors')

teams = []
for row in allTeamsTable[0].rows:
	print(row)
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
   }))


	

print(teams[0])