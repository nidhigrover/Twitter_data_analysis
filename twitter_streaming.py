#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "905865497081548800-YZbmsy2vBoS5jWET0HaIt0AF6PLJVB2"
access_token_secret = "r2Z9QUtlkKrVXZsoxEkWOR47WHNyRB4izoNStM6bJCBNY"
consumer_key = "wr3e10djJQC9gp4Pfg8J6OByX"
consumer_secret = "aBR74xUjm5Yrx19HsoYVeLCw1VENPyfMPMGGykIdpHzQVIew12"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['narendra modi', 'arvind kejriwal'])
