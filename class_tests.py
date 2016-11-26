import giantbomb

accessory_dict = {
        'api_detail_url': 'www.test.com',
        'date_added': '2016',
        'date_last_updated': '2016',
        'deck': 'Test deck',
        'description': 'Test description',
        'id': '12',
        'image': 'Test image',
        'name': 'Test name',
        'site_detail_url': 'www.test.com'
}

acc = giantbomb.Accessory.from_dict(accessory_dict)

assert acc.api_detail_url == accessory_dict['api_detail_url']
assert acc.date_added == accessory_dict['date_added']
assert acc.date_last_updated == accessory_dict['date_last_updated']
assert acc.deck == accessory_dict['deck']
assert acc.description == accessory_dict['description']
assert acc.id == accessory_dict['id']
assert acc.image == accessory_dict['image']
assert acc.name == accessory_dict['name']
assert acc.site_detail_url == accessory_dict['site_detail_url']
