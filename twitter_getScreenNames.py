import urllib
import twurl
import json

#base URL from Twitter API documentation
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    
    #call the augment function from twurl file.
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '5'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    
    #body in json
    data = connection.read()

    #headers in dictionary format
    headers = connection.info().dict

    
    #deserialize the json
    js = json.loads(data)
    
    #for pretty printing, use indentation
    print json.dumps(js, indent=4)

    for u in js['users'] :
        print u['screen_name']
        s = u['status']['text']
        print '  ',s[:50]
        #x-rate-limit-remaining is from the API documenation telling me...
        #...how many times I can call this API.
        print 'Remaining', headers['x-rate-limit-remaining']