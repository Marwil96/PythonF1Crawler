from wikitables import import_tables
import wikipedia
import json
import requests
print("Hello, world!")

allDriversTable = import_tables('List of Formula One drivers')

WIKI_REQUEST = 'http://en.wikipedia.org/w/api.php?action=query&prop=pageimages&format=json&piprop=original&titles='


def get_wiki_image(search_term):
    try:
        result = wikipedia.search(search_term, results=1)
        wikipedia.set_lang('en')
        wkpage = wikipedia.WikipediaPage(title=result[0])
        title = wkpage.title
        response = requests.get(WIKI_REQUEST+title)
        json_data = json.loads(response.text)
        img_link = list(json_data['query']['pages'].values())[
            0]['original']['source']
        return img_link
    except:
        return 0


drivers = []
def show_todo():
   for row in allDriversTable[1].rows:
      drivers.append(( {
        'name':'{Driver Name}'.format(**row).replace(' ~', '').replace(' ^','').replace(' *', ''),
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
  # driverData = wikipedia.page(wikipedia.search('{name}'.format(**driver))[0])
  try:
    # driverData = wikipedia.page(wikipedia.search('{name}'.format(**driver))[0])
    driverData = wikipedia.WikipediaPage('{name}'.format(**driver))
    print(driverData.images[0], '{name}'.format(**driver) )
    driverDetails = import_tables('{name}'.format(**driver))
    wiki_image = get_wiki_image('{name}'.format(**driver))
    driver['portrait_image'] = wiki_image
    driverSeason = []
    for detailsRow in driverDetails[0].rows:
      if '{Series}'.format(**detailsRow) == 'Formula One':
        driverSeason.append(({
          'season':'{Season}'.format(**detailsRow),
          'team':'{Team}'.format(**detailsRow),
          'races':'{Races}'.format(**detailsRow),
          'wins':'{Wins}'.format(**detailsRow),
          'poles':'{Poles}'.format(**detailsRow),
          'fastest_laps':'{FLaps}'.format(**detailsRow),
          'podiums':'{Podiums}'.format(**detailsRow),
          'points':'{Points}'.format(**detailsRow),
          'position':'{Position}'.format(**detailsRow),
          }))

    print(driverSeason)
    driver['driver_images'] = driverData.images
    driver['driver_seasons'] = driverSeason

  except:
      pass # doing nothing on exceptio

  # print('{name}'.format(**driver))
  # name = '{name}'.format(**driver)
  # driverDetails = import_tables(``)
  # for detailsRow in driverDetails[0].rows:
  #   try:
  #     print('{Team}'.format(**detailsRow))
  #   except:
  #     pass

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
