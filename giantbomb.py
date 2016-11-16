import requests
import datetime


class ApiError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return str(self.error)


class Request:
    class RequestSingleton:
        def __init__(self, delay):
            self.last_time = None
            self.delay = delay

        @staticmethod
        def curr_time():
            time = datetime.datetime.now().time()
            return (time.hour * 3600000) + (time.minute * 60000) + (time.second * 1000) + int((time.microsecond / 1000))

        def get(self, url, user_agent, params=None):
            while self.last_time is not None and (self.curr_time() - self.last_time) < self.delay:
                pass
            self.last_time = self.curr_time()
            res = requests.get(url, params=params, headers={"user-agent": user_agent})
            try:
                res_json = res.json()
            except ValueError:
                raise ApiError("Check your url")
            return res_json

    instance = None

    def __init__(self, delay=1000):
        if not Request.instance:
            Request.instance = Request.RequestSingleton(delay)
        else:
            Request.instance.delay = delay

    def __getattr__(self, name):
        return getattr(self.instance, name)


class Api:
    def __init__(self, api_key, user_agent):
        self.base_url = "http://www.giantbomb.com/api/"
        self.api_key = api_key
        self.user_agent = user_agent

    @staticmethod
    def verify_response(response):
        return True if response['status_code'] == 1 else False

    def get(self, url, params=None):
        params['api_key'] = self.api_key
        params['format'] = 'json'
        requester = Request(1000)
        response = requester.get(url, self.user_agent, params)
        if Api.verify_response(response):
            return response
        else:
            return "Failed"

    def get_game(self, id):
        url = self.base_url + 'game/{}'.format(id)
        params = {

        }
        return self.get(url, params)


class Accessory:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 id_=None,
                 image=None,
                 name=None,
                 site_detail_url=None):

        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.id = id_
        self.image = image
        self.name = name
        self.site_detail_url = site_detail_url

    def __str__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Character:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 birthday=None,
                 concepts=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 enemies=None,
                 first_appeared_in_game=None,
                 franchises=None,
                 friends=None,
                 games=None,
                 gender=None,
                 id_=None,
                 image=None,
                 last_name=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 real_name=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.birthday = birthday
        self.concepts = concepts
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.enemies = enemies
        self.first_appeared_in_game = first_appeared_in_game
        self.franchises = franchises
        self.friends = friends
        self.games = games
        self.gender = gender
        self.id = id_
        self.image = image
        self.last_name = last_name
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.real_name = real_name
        self.site_detail_url = site_detail_url

    def __str__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Chat:
    def __init__(self,
                 api_detail_url=None,
                 channel_name=None,
                 deck=None,
                 image=None,
                 password=None,
                 site_detail_url=None,
                 title=None):
        self.api_detail_url = api_detail_url
        self.channel_name = channel_name
        self.deck = deck
        self.image = image
        self.password = password
        self.site_detail_url = site_detail_url
        self.title = title

    def __str__(self):
        return "{} {{{}}}".format(self.channel_name, self.title)


class Company:
    def __init__(self,
                 abbreviation=None,
                 aliases=None,
                 api_detail_url=None,
                 characters=None,
                 concepts=None,
                 date_added=None,
                 date_founded=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 developed_games=None,
                 developer_releases=None,
                 distributor_releases=None,
                 id_=None,
                 image=None,
                 location_address=None,
                 location_city=None,
                 location_country=None,
                 location_state=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 phone=None,
                 published_games=None,
                 publisher_releases=None,
                 site_detail_url=None,
                 website=None
                 ):
        self.abbreviation = abbreviation
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.characters = characters
        self.concepts = concepts
        self.date_added = date_added
        self.date_founded = date_founded
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.developed_games = developed_games
        self.developer_releases = developer_releases
        self.distributor_releases = distributor_releases
        self.id = id_
        self.image = image
        self.location_address = location_address
        self.location_city = location_city
        self.location_country = location_country
        self.location_state = location_state
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.phone = phone
        self.published_games = published_games
        self.published_releases = publisher_releases
        self.site_detail_url = site_detail_url
        self.website = website

    def __str__(self):
        return "{} {{{}}}".format(self.name, self.id)
