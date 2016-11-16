import giantbomb
import pprint
import config

pp = pprint.PrettyPrinter(indent=2)
api = giantbomb.Api(config.api_key, 'test_app/0.1')

# result = api.get("http://www.giantbomb.com/api/game/3030-4625/", params={'api_key': api.api_key, 'format': 'json'})
# result['results'] = ''
result = api.get_game('3030-4625')
pp.pprint(result)

