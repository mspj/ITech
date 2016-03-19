import oauth2
import json
import urllib

class APITwitter(object):
    BASE_URL = "https://api.twitter.com/1.1/search/tweets.json"
    TWITTER_OAUTH_TOKEN = '4925320361-NfqsXqimaoh1w47oRkhLMTfsyMTY5wKVoOJC9KI'
    TWITTER_OAUTH_SECRET = 'sYwMWdy0HYYt0suHi7lAqGWBzg5iT0YGx3vXOdfZq9Mub'
    TWITTER_CONSUMER_KEY = 'jzaX3FpCkrjVLox9WCxdRSeuK'
    TWITTER_CONSUMER_SECRET = 'NxRDUo7zKXPVmmK6vKUpHEwxwpmbCg3vx3Nyp0ocr4M4L62QrR'

    def oauth_req(self, url, key, secret, http_method="GET", post_body="", http_headers=None):
        consumer = oauth2.Consumer(key=self.TWITTER_CONSUMER_KEY, secret=self.TWITTER_CONSUMER_SECRET)
        token = oauth2.Token(key=key, secret=secret)
        client = oauth2.Client(consumer, token)
        resp, response = client.request(url, method=http_method, body=post_body, headers=http_headers )

        return response

    def search_twitter_hashtag(self, keywords):
        url = "%s?q=%s&count=20" % (self.BASE_URL, urllib.quote(keywords, safe=''))
        # print url
        response = self.oauth_req(url, self.TWITTER_OAUTH_TOKEN, self.TWITTER_OAUTH_SECRET)
        jsonData = json.loads(response)
        if response is None:
            return response
        results = []
        for result in jsonData.get('statuses'):
            text = result.get('text')
            created_at = result.get('created_at')
            profile_username = result.get('user').get('name')
            profile_image_url = result.get('user').get('profile_image_url')
            media = None
            if(result.get('entities').get('media')is not None):
                media = result.get('entities').get('media')[0].get('media_url')
            results.append({'text': text, 'created_at': created_at, 'profile_username': profile_username, 'profile_image_url': profile_image_url, 'media':media})

        return results