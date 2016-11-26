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
                raise ApiError("URL provided returned invalid results:\nurl: {}\nparams: {}".format(url, params))
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
    def __init__(self, api_key, user_agent, delay=1000):
        self.base_url = "http://www.giantbomb.com/api/"
        self.api_key = api_key
        self.user_agent = user_agent
        self.delay = delay

    @staticmethod
    def verify_response(response):
        try:
            if not response['status_code'] == 1:
                raise ApiError('Status code returned not 1')
        except KeyError as e:
            raise ApiError("JSON error: {}".format(e))

    @staticmethod
    def trim_attributes(instance):
        fields = instance.__dict__
        for field in fields:
            try:
                if len(fields[field]) == 1:
                    setattr(instance, field, fields[field][0])
            except TypeError:
                pass

    def get(self, url, params={}):
        params['api_key'] = self.api_key
        params['format'] = 'json'
        requester = Request(self.delay)
        response = requester.get(url, self.user_agent, params)

        Api.verify_response(response)
        return response

    def get_accessory(self, id_):
        url = self.base_url + 'accessory/{}'.format(id_)
        res = self.get(url)['results']
        return Accessory.from_dict(res)

    def get_character(self, id_):
        url = self.base_url + 'character/{}'.format(id_)
        res = self.get(url)['results']
        return Character.from_dict(res)

    def get_chat(self, id_):
        url = self.base_url + 'chat/{}'.format(id_)
        res = self.get(url)['results']
        return Chat.from_dict(res)

    def get_company(self, id_):
        url = self.base_url + 'company/{}'.format(id_)
        res = self.get(url)['results']
        return Company.from_dict(res)

    def get_concept(self, id_):
        url = self.base_url + 'concept/{}'.format(id_)
        res = self.get(url)['results']
        return Concept.from_dict(res)

    def get_franchise(self, id_):
        url = self.base_url + 'franchise/{}'.format(id_)
        res = self.get(url)['results']
        return Franchise.from_dict(res)

    def get_game(self, id_):
        url = self.base_url + 'game/{}'.format(id_)
        res = self.get(url)['results']
        return Game.from_dict(res)

    def get_game_rating(self, id_):
        url = self.base_url + 'game_rating/{}'.format(id_)
        res = self.get(url)['results']
        return GameRating.from_dict(res)

    def get_game_genre(self, id_):
        url = self.base_url + 'genre/{}'.format(id_)
        res = self.get(url)['results']
        return Genre.from_dict(res)

    def get_location(self, id_):
        url = self.base_url + 'location/{}'.format(id_)
        res = self.get(url)['results']
        return Location.from_dict(res)

    def get_object(self, id_):
        url = self.base_url + 'object/{}'.format(id_)
        res = self.get(url)['results']
        return Object.from_dict(res)

    def get_person(self, id_):
        url = self.base_url + 'person/{}'.format(id_)
        res = self.get(url)['results']
        return Person.from_dict(res)

    def get_platform(self, id_):
        url = self.base_url + 'platform/{}'.format(id_)
        res = self.get(url)['results']
        return Platform.from_dict(res)

    def get_promo(self, id_):
        url = self.base_url + 'promo/{}'.format(id_)
        res = self.get(url)['results']
        return Promo.from_dict(res)

    def get_rating_board(self, id_):
        url = self.base_url + 'rating_board/{}'.format(id_)
        res = self.get(url)['results']
        return RatingBoard.from_dict(res)

    def get_region(self, id_):
        url = self.base_url + 'region/{}'.format(id_)
        res = self.get(url)['results']
        return Region.from_dict(res)

    def get_release(self, id_):
        url = self.base_url + 'release/{}'.format(id_)
        res = self.get(url)['results']
        return Release.from_dict(res)

    def get_review(self, id_):
        url = self.base_url + 'review/{}'.format(id_)
        res = self.get(url)['results']
        return Review.from_dict(res)

    def get_theme(self, id_):
        url = self.base_url + 'theme/{}'.format(id_)
        res = self.get(url)['results']
        return Theme.from_dict(res)

    def get_types(self, id_):
        url = self.base_url + 'types/{}'.format(id_)
        res = self.get(url)['results']
        return Types.from_dict(res)

    def get_user_review(self, id_):
        url = self.base_url + 'user_review/{}'.format(id_)
        res = self.get(url)['results']
        return UserReview.from_dict(res)

    def get_video(self, id_):
        url = self.base_url + 'video/{}'.format(id_)
        res = self.get(url)['results']
        return Video.from_dict(res)

    def get_video_type(self, id_):
        url = self.base_url + 'video_type/{}'.format(id_)
        res = self.get(url)['results']
        return VideoType.from_dict(res)

    def get_video_category(self, id_):
        url = self.base_url + 'video_category/{}'.format(id_)
        res = self.get(url)['results']
        return VideoCategory.from_dict(res)

    def get_video_show(self, id_):
        url = self.base_url + 'video_show/{}'.format(id_)
        res = self.get(url)['results']
        return VideoShow.from_dict(res)

    def search(self, query, resources=[]):
        url = self.base_url + 'search/'
        res = self.get(url, params={'query': query,
                                    'resources': ",".join(resource for resource in resources)
                                    })['results']
        games = []
        franchises = []
        characters = []
        concepts = []
        objects = []
        locations = []
        people = []
        companies = []
        videos = []

        for result in res:
            if result['resource_type'] == 'game':
                games.append(Game.from_dict(result))
            elif result['resource_type'] == 'franchise':
                franchises.append(Franchise.from_dict(result))
            elif result['resource_type'] == 'character':
                characters.append(Character.from_dict(result))
            elif result['resource_type'] == 'concept':
                concepts.append(Concept.from_dict(result))
            elif result['resource_type'] == 'object':
                objects.append(Object.from_dict(result))
            elif result['resource_type'] == 'location':
                locations.append(Location.from_dict(result))
            elif result['resource_type'] == 'person':
                people.append(Person.from_dict(result))
            elif result['resource_type'] == 'company':
                companies.append(Company.from_dict(result))
            elif result['resource_type'] == 'video':
                videos.append(Video.from_dict(result))

        return SearchResults(games=games,
                             franchises=franchises,
                             characters=characters,
                             concepts=concepts,
                             objects=objects,
                             locations=locations,
                             people=people,
                             companies=companies,
                             videos=videos)


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

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('site_detail_url', None),)

    def __repr__(self):
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

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('birthday', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('enemies', None),
                   data.get('first_appeared_in_game', None),
                   data.get('franchises', None),
                   data.get('friends', None),
                   data.get('games', None),
                   data.get('gender', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('last_name', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('real_name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
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

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('channel_name', None),
                   data.get('deck', None),
                   data.get('image', None),
                   data.get('password', None),
                   data.get('site_detail_url', None),
                   data.get('title', None))

    def __repr__(self):
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

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('abbreviation', None),
                   data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_founded', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('developed_games', None),
                   data.get('developer_releases', None),
                   data.get('distributor_releases', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('location_address', None),
                   data.get('location_city', None),
                   data.get('location_country', None),
                   data.get('location_state', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('phone', None),
                   data.get('published_games', None),
                   data.get('published_releases', None),
                   data.get('site_detail_url', None),
                   data.get('website', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Concept:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 characters=None,
                 concepts=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 first_appeared_in_franchise=None,
                 first_appeared_in_game=None,
                 franchises=None,
                 games=None,
                 id_=None,
                 image=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 related_concepts=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.characters = characters
        self.concepts = concepts
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.first_appeared_in_franchise = first_appeared_in_franchise
        self.first_appeared_in_game = first_appeared_in_game
        self.franchises = franchises
        self.games = games
        self.id = id_
        self.image = image
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.related_concepts = related_concepts
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('first_appeared_in_franchise', None),
                   data.get('first_appeared_in_game', None),
                   data.get('franchises', None),
                   data.get('games', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('related_concepts', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Franchise:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 characters=None,
                 concepts=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 games=None,
                 id_=None,
                 image=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.characters = characters
        self.concepts = concepts
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.games = games
        self.id = id_
        self.image = image
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('games', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Game:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 characters=None,
                 concepts=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 developers=None,
                 expected_release_day=None,
                 expected_release_month=None,
                 expected_release_quarter=None,
                 expected_release_year=None,
                 first_appearance_characters=None,
                 first_appearance_concepts=None,
                 first_appearance_locations=None,
                 first_appearance_objects=None,
                 first_appearance_people=None,
                 franchises=None,
                 genres=None,
                 id_=None,
                 image=None,
                 images=None,
                 killed_characters=None,
                 locations=None,
                 name=None,
                 number_of_user_reviews=None,
                 objects=None,
                 original_game_rating=None,
                 original_release_date=None,
                 people=None,
                 platforms=None,
                 publishers=None,
                 releases=None,
                 reviews=None,
                 similar_games=None,
                 site_detail_url=None,
                 themes=None,
                 videos=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.characters = characters
        self.concepts = concepts
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.developers = developers
        self.expected_release_day = expected_release_day
        self.expected_release_month = expected_release_month
        self.expected_release_quarter = expected_release_quarter
        self.expected_release_year = expected_release_year
        self.first_appearance_characters = first_appearance_characters
        self.first_appearance_concepts = first_appearance_concepts
        self.first_appearance_locations = first_appearance_locations
        self.first_appearance_objects = first_appearance_objects
        self.first_appearance_people = first_appearance_people
        self.franchises = franchises
        self.genres = genres
        self.id = id_
        self.image = image
        self.images = images
        self.killed_characters = killed_characters
        self.locations = locations
        self.name = name
        self.number_of_user_reviews = number_of_user_reviews
        self.objects = objects
        self.original_game_rating = original_game_rating
        self.original_release_date = original_release_date
        self.people = people
        self.platforms = platforms
        self.publishers = publishers
        self.releases = releases
        self.reviews = reviews
        self.similar_games = similar_games
        self.site_detail_url = site_detail_url
        self.themes = themes
        self.videos = videos

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('developers', None),
                   data.get('expected_release_day', None),
                   data.get('expected_release_month', None),
                   data.get('expected_release_quarter', None),
                   data.get('expected_release_year', None),
                   data.get('first_appearance_characters', None),
                   data.get('first_appearance_concepts', None),
                   data.get('first_appearance_locations', None),
                   data.get('first_appearance_objects', None),
                   data.get('first_appearance_people', None),
                   data.get('franchises', None),
                   data.get('genres', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('images', None),
                   data.get('killed_characters', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('number_of_user_reviews', None),
                   data.get('objects', None),
                   data.get('original_game_rating', None),
                   data.get('original_release_date', None),
                   data.get('people', None),
                   data.get('platforms', None),
                   data.get('publishers', None),
                   data.get('releases', None),
                   data.get('reviews', None),
                   data.get('similar_games', None),
                   data.get('site_detail_url', None),
                   data.get('themes', None),
                   data.get('videos', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class GameRating:
    def __init__(self,
                 api_detail_url=None,
                 id_=None,
                 image=None,
                 name=None,
                 rating_board=None):
        self.api_detail_url = api_detail_url
        self.id = id_
        self.image = image
        self.name = name
        self.rating_board = rating_board

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('rating_board', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Genre:
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

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Location:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 first_appeared_in_game=None,
                 id_=None,
                 image=None,
                 name=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.first_appeared_in_game = first_appeared_in_game
        self.id = id_
        self.image = image
        self.name = name
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('first_appeared_in_game', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Object:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 characters=None,
                 companies=None,
                 concepts=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 first_appeared_in_game=None,
                 franchises=None,
                 games=None,
                 id_=None,
                 image=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.characters = characters
        self.companies = companies
        self.concepts = concepts
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.first_appeared_in_game = first_appeared_in_game
        self.franchises = franchises
        self.games = games
        self.id = id_
        self.image = image
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('characters', None),
                   data.get('companies', None),
                   data.get('concepts', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('first_appeared_in_game', None),
                   data.get('franchises', None),
                   data.get('games', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Person:
    def __init__(self,
                 aliases=None,
                 api_detail_url=None,
                 birth_date=None,
                 characters=None,
                 concepts=None,
                 country=None,
                 date_added=None,
                 date_last_updated=None,
                 death_date=None,
                 deck=None,
                 description=None,
                 first_credited_game=None,
                 franchises=None,
                 games=None,
                 gender=None,
                 hometown=None,
                 id_=None,
                 image=None,
                 locations=None,
                 name=None,
                 objects=None,
                 people=None,
                 site_detail_url=None):
        self.aliases = aliases
        self.api_detail_url = api_detail_url
        self.birth_date = birth_date
        self.characters = characters
        self.concepts = concepts
        self.country = country
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.death_date = death_date
        self.deck = deck
        self.description = description
        self.first_credited_game = first_credited_game
        self.franchises = franchises
        self.games = games
        self.gender = gender
        self.hometown = hometown
        self.id = id_
        self.image = image
        self.locations = locations
        self.name = name
        self.objects = objects
        self.people = people
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('aliases', None),
                   data.get('api_detail_url', None),
                   data.get('birth_date', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('country', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('death_date', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('first_credited_game', None),
                   data.get('franchises', None),
                   data.get('games', None),
                   data.get('gender', None),
                   data.get('hometown', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('locations', None),
                   data.get('name', None),
                   data.get('objects', None),
                   data.get('people', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Platform:
    def __init__(self,
                 abbreviation=None,
                 api_detail_url=None,
                 company=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 id_=None,
                 image=None,
                 install_base=None,
                 name=None,
                 online_support=None,
                 original_price=None,
                 release_date=None,
                 site_detail_url=None):
        self.abbreviation = abbreviation
        self.api_detail_url = api_detail_url
        self.company = company
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.id = id_
        self.image = image
        self.install_base = install_base
        self.name = name
        self.online_support = online_support
        self.original_price = original_price
        self.release_date = release_date
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('abbreviation', None),
                   data.get('api_detail_url', None),
                   data.get('company', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('install_base', None),
                   data.get('name', None),
                   data.get('online_support', None),
                   data.get('original_price', None),
                   data.get('release_date', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Promo:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 deck=None,
                 id_=None,
                 image=None,
                 link=None,
                 name=None,
                 resource_type=None,
                 user=None):
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.deck = deck
        self.id = id_
        self.image = image
        self.link = link
        self.name = name
        self.resource_type = resource_type
        self.user = user

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('deck', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('link', None),
                   data.get('name', None),
                   data.get('resource_type', None),
                   data.get('user', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class RatingBoard:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 id_=None,
                 image=None,
                 name=None,
                 region=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.id = id_
        self.image = image
        self.name = name
        self.region = region
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('region', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Region:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 id_=None,
                 image=None,
                 name=None,
                 rating_boards=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.id = id_
        self.image = image
        self.name = name
        self.rating_boards = rating_boards
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('name', None),
                   data.get('rating_boards', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Release:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 developers=None,
                 expected_release_day=None,
                 expected_release_month=None,
                 expected_release_quarter=None,
                 expected_release_year=None,
                 game=None,
                 game_rating=None,
                 id_=None,
                 image=None,
                 images=None,
                 maximum_players=None,
                 minimum_players=None,
                 name=None,
                 platform=None,
                 product_code_type=None,
                 product_code_value=None,
                 publishers=None,
                 region=None,
                 release_date=None,
                 resolutions=None,
                 singleplayer_features=None,
                 sound_systems=None,
                 site_detail_url=None,
                 widescreen_support=None):
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.developers = developers
        self.expected_release_day = expected_release_day
        self.expected_release_month = expected_release_month
        self.expected_release_quarter = expected_release_quarter
        self.expected_release_year = expected_release_year
        self.game = game
        self.game_rating = game_rating
        self.id = id_
        self.image = image
        self.images = images
        self.maximum_players = maximum_players
        self.minimum_players = minimum_players
        self.name = name
        self.platform = platform
        self.product_code_type = product_code_type
        self.product_code_value = product_code_value
        self.publishers = publishers
        self.region = region
        self.release_date = release_date
        self.resolutions = resolutions
        self.singleplayer_features = singleplayer_features
        self.sound_systems = sound_systems
        self.site_detail_url = site_detail_url
        self.widescreen_support = widescreen_support

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('developers', None),
                   data.get('expected_release_day', None),
                   data.get('expected_release_month', None),
                   data.get('expected_release_quarter', None),
                   data.get('expected_release_year', None),
                   data.get('game', None),
                   data.get('game_rating', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('images', None),
                   data.get('maximum_players', None),
                   data.get('minimum_players', None),
                   data.get('name', None),
                   data.get('platform', None),
                   data.get('product_code_type', None),
                   data.get('product_code_value', None),
                   data.get('publishers', None),
                   data.get('region', None),
                   data.get('release_date', None),
                   data.get('resolutions', None),
                   data.get('singleplayer_features', None),
                   data.get('sound_systems', None),
                   data.get('site_detail_url', None),
                   data.get('widescreen_support', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Review:
    def __init__(self,
                 api_detail_url=None,
                 deck=None,
                 description=None,
                 dlc_name=None,
                 game=None,
                 platforms=None,
                 publish_date=None,
                 release=None,
                 reviewer=None,
                 score=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.deck = deck
        self.description = description
        self.dlc_name = dlc_name
        self.game = game
        self.platforms = platforms
        self.publish_date = publish_date
        self.release = release
        self.reviewer = reviewer
        self.score = score
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('dlc_name', None),
                   data.get('game', None),
                   data.get('platforms', None),
                   data.get('publish_date', None),
                   data.get('release', None),
                   data.get('reviewer', None),
                   data.get('score', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} Review by {}: {}".format(self.game, self.reviewer, self.score)


class SearchResults:
    def __init__(self,
                 games=[],
                 franchises=[],
                 characters=[],
                 concepts=[],
                 objects=[],
                 locations=[],
                 people=[],
                 companies=[],
                 videos=[]):

        self.games = games
        self.franchises = franchises
        self.characters = characters
        self.concepts = concepts
        self.objects = objects
        self.locations = locations
        self.people = people
        self.companies = companies
        self.videos = videos

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('games', None),
                   data.get('franchises', None),
                   data.get('characters', None),
                   data.get('concepts', None),
                   data.get('objects', None),
                   data.get('locations', None),
                   data.get('people', None),
                   data.get('companies', None),
                   data.get('videos', None))

    def __repr__(self):
        return "Games: {}, Franchises: {}, Characters: {}, Concepts: {}, " \
               "Objects: {}, Locations: {}, People: {}, Companies: {}, Videos: {}".format(len(self.games),
                                                                                          len(self.franchises),
                                                                                          len(self.characters),
                                                                                          len(self.concepts),
                                                                                          len(self.objects),
                                                                                          len(self.locations),
                                                                                          len(self.people),
                                                                                          len(self.companies),
                                                                                          len(self.videos))


class Theme:
    def __init__(self,
                 api_detail_url=None,
                 id_=None,
                 name=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.id = id_
        self.name = name
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('id', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class Types:
    def __init__(self,
                 detail_resource_name=None,
                 id_=None,
                 list_resource_name=None):
        self.detail_resource_name = detail_resource_name
        self.id = id_
        self.list_resource_name = list_resource_name

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('detail_resource_name', None),
                   data.get('id', None),
                   data.get('list_resource_name', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.list_resource_name, self.id)


class UserReview:
    def __init__(self,
                 api_detail_url=None,
                 date_added=None,
                 date_last_updated=None,
                 deck=None,
                 description=None,
                 game=None,
                 reviewer=None,
                 score=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.date_added = date_added
        self.date_last_updated = date_last_updated
        self.deck = deck
        self.description = description
        self.game = game
        self.reviewer = reviewer
        self.score = score
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('date_added', None),
                   data.get('date_last_updated', None),
                   data.get('deck', None),
                   data.get('description', None),
                   data.get('wikiObject', None),
                   data.get('reviewer', None),
                   data.get('score', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} Review by {}: {}".format(self.game, self.reviewer, self.score)


class Video:
    def __init__(self,
                 api_detail_url=None,
                 deck=None,
                 hd_url=None,
                 high_url=None,
                 low_url=None,
                 embed_player=None,
                 id_=None,
                 image=None,
                 length_seconds=None,
                 name=None,
                 publish_date=None,
                 site_detail_url=None,
                 url=None,
                 user=None,
                 youtube_id=None):
        self.api_detail_url = api_detail_url
        self.deck = deck
        self.hd_url = hd_url
        self.high_url = high_url
        self.low_url = low_url
        self.embed_player = embed_player
        self.id = id_
        self.image = image
        self.length_seconds = length_seconds
        self.name = name
        self.publish_date = publish_date
        self.site_detail_url = site_detail_url
        self.url = url
        self.user = user
        self.youtube_id = youtube_id

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('deck', None),
                   data.get('hd_url', None),
                   data.get('high_url', None),
                   data.get('low_url', None),
                   data.get('embed_player', None),
                   data.get('id', None),
                   data.get('image', None),
                   data.get('length_seconds', None),
                   data.get('name', None),
                   data.get('publish_date', None),
                   data.get('site_detail_url', None),
                   data.get('url', None),
                   data.get('user', None),
                   data.get('youtube_id', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class VideoType:
    def __init__(self,
                 api_detail_url=None,
                 deck=None,
                 id_=None,
                 name=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.deck = deck
        self.id = id_
        self.name = name
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('deck', None),
                   data.get('id', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class VideoCategory:
    def __init__(self,
                 api_detail_url=None,
                 deck=None,
                 id_=None,
                 name=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.deck = deck
        self.id = id_
        self.name = name
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('deck', None),
                   data.get('id', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)


class VideoShow:
    def __init__(self,
                 api_detail_url=None,
                 deck=None,
                 id_=None,
                 name=None,
                 site_detail_url=None):
        self.api_detail_url = api_detail_url
        self.deck = deck
        self.id = id_
        self.name = name
        self.site_detail_url = site_detail_url

        Api.trim_attributes(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data.get('api_detail_url', None),
                   data.get('deck', None),
                   data.get('id', None),
                   data.get('name', None),
                   data.get('site_detail_url', None))

    def __repr__(self):
        return "{} {{{}}}".format(self.name, self.id)
