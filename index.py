from wikitables import import_tables
import json
print("Hello, world!")

allDriversTable = import_tables('List of Formula One drivers')

drivers = []
def show_todo():
   for row in allDriversTable[1].rows:
    drivers.append(( {
      'name':'{Driver Name}'.format(**row),
      'nationality': '{Nationality}'.format(**row),
      'seasons_completed': '{Seasons Competed}'.format(**row),
      'drivers_championships':"{Drivers' Championships}".format(**row),
      'race_entries': '{Race Entries}'.format(**row),
      'race_starts': '{Race Starts}'.format(**row),
      'pole_positions': '{Pole Positions}'.format(**row),
      'race_wins': '{Race Wins}'.format(**row),
      'podiums': '{Podiums}'.format(**row),
      'fastest_laps': '{Fastest laps}'.format(**row),
      'points': '{Points}'.format(**row),
    }))

a = show_todo()

for driver in drivers:
  print('{name}'.format(**driver))
  name = '{name}'.format(**driver)
  driverDetails = import_tables('Alex Albon')
  for detailsRow in driverDetails[0].rows:
    try:
      print('{Team}'.format(**detailsRow))
    except:
      pass

# print(drivers)

# for row in allDriversTable[1].rows:
#     print(
#       '{Driver Name}'.format(**row),
#       '{Nationality}'.format(**row),
#       '{Seasons Competed}'.format(**row),
#       "{Drivers' Championships}".format(**row),
#       '{Race Entries}'.format(**row),
#       '{Race Starts}'.format(**row),
#       '{Pole Positions}'.format(**row),
#       '{Race Wins}'.format(**row),
#       '{Podiums}'.format(**row),
#       '{Fastest laps}'.format(**row),
#       '{Points}'.format(**row),
#       )

# driverTable = import_tables('Michael Schumacher')  # returns a list of WikiTable objects
# # print(tables[0].Season)

# for row in driverTable[0].rows:
#     print('{Team}'.format(**row), '{Series}'.format(**row))

# print(tables[0].json())


with open('data.json', 'w') as outfile:
    json.dump(drivers, outfile)
