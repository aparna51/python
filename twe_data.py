import tweepy
consumer_key='1erbqpn4UMNhZ1GpjhTWITlS4'
consumer_secret='zxt0tqoNOLvkHETpMrP9lCYTxQfxTguVn9A7mOn1BHP8XZpXyO'

#creating access key and access consumer_secret
access_key='3143970515-74i98NnON7UHm7lHbDD21LDqTjaV1T7xwxRjQn6'
access_secret='zbCDzyumC9A9Gp27CfP5kx4a7kefiXheu1YXPZWQfyiJp'

#connecting for authentcation
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)

connect=tweepy.API(auth)

get_data=connect.search('trump')

for i in get_data:
    print(i.text)
