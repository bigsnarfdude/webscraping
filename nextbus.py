import requests
from lxml import etree
from flask import Flask
from twilio import twiml
import os
from random import choice
from twilio.rest import TwilioRestClient


port = int(os.environ.get('PORT', 5000))
app = Flask(__name__)
@app.route('/<bus_stop_number>', methods=['GET','POST'])
def sms_out(bus_stop_number):
    #r = twiml.Response()
    #if request.form['Body'].upper() == "HELP":
    if bus_stop_number == "HELP":
        return ("Welcome to FunBus.  Text Bus Stop Number " \
            "to get next bus time and a fortune cookie!")
    elif bus_stop_number == "favicon.ico":
        pass
    else:
        bus_stop_number = int(bus_stop_number)
        result = str(next_bus_by_stop_request(bus_stop_number))
        fortune_cookie = choice(affirmations2)
        body = fortune_cookie + result
        # r.sms(body) # dunno if this will work
    message = client.sms.messages.create(body=body,to="+1604xxxyyyy", from_="+1604xxxyyyy")
    return  str(body)


def next_bus_by_stop_request(bus_stop_number):
    api_request = "http://api.translink.ca/RTTIAPI/V1/stops/%s/estimates?apikey=putYourKeyHere" % bus_stop_number
    api_response = requests.get(api_request)
    root = etree.fromstring(api_response.text)
    first_bus = root.find('NextBus').find('Schedules').find('Schedule').find('ExpectedLeaveTime').text
    location = root.find('NextBus').find('Schedules').find('Schedule').find('Destination').text
    return location, first_bus
 
def test_translink_api():
    return next_bus_by_stop_request(52057)    

def test_sms_out():
    message = client.sms.messages.create(body="test of sms",to="+1604xxxyyyy", from_="+1604xxxyyyy")
    return  message.sid

if __name__ == "__main__":
    if port == 5000:
        app.debug = True
    account_sid = "asdfasdfasdf80asf898fa09fs987sf908"
    auth_token  = "asdf90sf8sf908asf09sf9sdf09ads9sf907"
    client = TwilioRestClient(account_sid, auth_token)
    affirmations = [
        'You are awesome! ',
        'You have a great sense of humor! ',
        'Your brain is is awesome! ',
        'You are a good listener! ',
        'You can smile and creep people out! ',
        'You are a good person! ',
        'People love you',
        ]
    affirmations2 = '''
You only need look to your own reflection for inspiration. Because you are Beautiful!
Rivers need springs.
Good news from afar may bring you a welcome visitor.
When all else seems to fail, smile for today and just love someone.
When you look down, all you see is dirt, so keep looking up.
If you are afraid to shake the dice, you will never throw a six.
A single conversation with a wise man is better than ten years of study.
Happiness is often a rebound from hard work. 
The world may be your oyster, but that doesn't mean you'll get it's pearl.
You're true love will show himself to you under the moonlight.
Do not follow where the path may lead. Go where there is no path...and leave a trail
Do not fear what you don't know.
The object of your desire comes closer.
If you wish to know the mind of a man, listen to his words.
The most useless energy is trying to change what and who God so carefully created.
Do not be covered in sadness or be fooled in happiness they both must exist
You will have unexpected great good luck.
You will have a pleasant surprise.
All progress occurs because people dare to be different.
Your ability for accomplishment will be followed by success.
We can't help everyone. But everyone can help someone.
Express yourself: Don't hold back!
You have a deep appreciation of the arts and music.
Human evolution: "wider freeway" but narrower viewpoints.
Back away from individuals who are impulsive.
Enjoyed the meal? Buy one to go too.
You believe in the goodness of mankind.
A big fortune will descend upon you this year.
Now these three remain, faith, hope, and love. The greatest of these is love.
For success today look first to yourself.
Determination is the wake-up call to the human will.
There are no limitations to the mind except those we aknowledge.
A merry heart does good like a medicine.
Whenever possible, keep it simple.
Your dearest wish will come true.
Poverty is no disgrace.
If you don't do it excellently, don't do it at all.
You have an unusual equipment for success, use it properly.
Emotion is energy in motion.
You will soon be honored by someone you respect.
Punctuality is the politeness of kings and the duty of gentle people everywhere.
Your happiness is intertwined with your outlook on life.
Elegant surroundings will soon be yours.
If you feel you are right, stand firmly by your convictions.
Your smile brings happiness to everyone you meet.
Instead of worrying and agonizing, move ahead constructively.
Do you believe? Endurance and persistence will be rewarded.
A new business venture is on the horizon.
Never underestimate the power of the human touch.
Hold on to the past but eventually, let the times go and keep the memories into the present.
Truth is an unpopular subject. Because it is unquestionably correct.
The most important thing in communication is to hear what isn't being said.
You are broad minded and socially active.
Your dearest dream is coming true. God looks after you especially.
You will recieve some high prize or award.
Your present question marks are going to succeed.
You have a fine capacity for the enjoyment of life.
You will live long and enjoy life.
An admirer is concealing his/her affection for you.
A wish is what makes life happen when you dream of rose petals.
Love can turn cottage into a golden palace.
Lend your money and lose your freind.
You will kiss your crush ohhh lalahh
You will be rewarded for being a good listener in the next week.
If you never give up on love, It will never give up on you.
Unleash your life force.
Your wish will come true.
There is a prospect of a thrilling time ahead for you.
No distance is too far, if two hearts are tied together.
Land is always in the mind of the flying birds.
Try? No! Do or do not, there is no try.
Do not worry, you will have great peace.
It's about time you asked that special someone on a date.
You create your own stage ... the audience is waiting.
It is never too late. Just as it is never too early.
Discover the power within yourself.
Good things take time.
You can still love what you can not have in life.
Make a wise choice everyday.
Circumstance does not make the man; it reveals him to himself.
The man who waits till tomorrow, misses the opportunities of today.
Life does not get better by chance. It gets better by change.
If you never expect anything you can never be disappointed.
People in your surroundings will be more cooperative than usual.
True wisdom is found in happiness.
Ones always regrets what could have done. Remember for next time.
Find a peaceful place where you can make plans for the future.
All the water in the world can't sink a ship unless it gets inside.
The earth is a school learn in it.
In music, one must think with his heart and feel with his brain.
If you speak honestly, everyone will listen.
Ganerosity will repay itself sooner than you imagine.
Good things take time
Do what is right, not what you should.
To effect the quality of the day is no small achievement.'''.split('\n')
    app.run(host="0.0.0.0", port=port, debug=True)
