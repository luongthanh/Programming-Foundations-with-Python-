#from twilio import rest 
from twilio.rest import TwilioRestClient

account_sid = "AC2bbd49f54632e17d14a3ce7612aaa3f2" # Your Account SID from www.twilio.com/console
auth_token  = "7a773754b00d6fcc61be36637fe9c8a4"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="This is the first try for Twilio message sending.",
    to="+841634523936",    # Replace with your phone number
    from_="+841629905937") # Replace with your Twilio number

print(message.sid)

#the phone number should be from the countries which Twilio supports. In that case, it excludes Vietnam. 

