import giantbomb
import pprint
import config

pp = pprint.PrettyPrinter(indent=2)
api = giantbomb.Api(config.api_key, 'test_app/0.1')
'''
result = api.get("http://www.giantbomb.com/api/search/", params={'query': 'rollercoaster'})
pp.pprint(result['results'][2])
game = giantbomb.Game.from_dict(result['results'][7])
print(game.name)


result = api.get_game('300')
for platform in result.platforms:
    pp.pprint(platform)

result = api.get_accessory('1')
pp.pprint(result.__dict__)

result = api.get_character('1')
pp.pprint(result.__dict__)
'''
result = api.get_company('3010-22')
pp.pprint(result)

result = api.get_concept('1')
pp.pprint(result)

result = api.get_franchise('1')
pp.pprint(result)

result = api.get_game_rating('1')
pp.pprint(result)