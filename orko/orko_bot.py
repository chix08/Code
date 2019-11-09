from flask import Flask, request
import requests
import json
from orko import resource_orko

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'Token'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = '******cUdUHoBAGGhb347heA3QWZAPiW2ZAHdzsAe89BwfFZArc89yvFqBGmkUZBxi68IvyFjH5lhSLoWjF2Bci8Ye4tTFZBwLZAKwRqTwwqmKdKnEq3epY4fqJIDw3NbVWAMJ55ZC5rZAtA08AOBjKuNEnzZCtm40CresWpiPB5IfpfZB9L8M0chFKPFND85zlmQsZD'
quiz = False
first_name = ''
last_name = ''
id = 0


@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"


@app.route('/', methods=['POST'])
def handle_message():
    '''
    Handle messages sent by facebook messenger to the applicaiton
    '''
    data = request.get_json()
    global id
    id = try_ex(lambda: data['entry'][0]['messaging'][0]['sender']['id'])
    text = try_ex(lambda: data['entry'][0]['messaging'][0]['message']['text'])
    print(text.lower())
    global quiz
    if text.lower() == "quiz" and quiz:
        quiz = True
        start_quiz()
    if text.lower() in resource_orko.WELCOME_MESSAGES_USER:
        if not quiz:
            welcome()
        else:
            resume_quiz()
    else:
        if not quiz:
            help_menu()
        else:
            resume_quiz()


def welcome():
    name = get_name(id)
    message_text = resource_orko.WELCOME.format(name)
    requests.post("https://graph.facebook.com/v2.6/me/messages",

                  params={"access_token": PAGE_ACCESS_TOKEN},

                  headers={"Content-Type": "application/json"},

                  data=json.dumps({
                      "recipient": {"id": id},
                      "message": {"text": message_text}
                  }))
    help_menu()


def start_quiz():
    print("start_quiz")


def help_menu():
    data = create_data(resource_orko.HELP_OPTIONS)

    requests.post("https://graph.facebook.com/v2.6/me/messages",

                  params={"access_token": PAGE_ACCESS_TOKEN},

                  headers={"Content-Type": "application/json"},

                  data=data
                  )

    return


def create_data(options):
    print(options)
    if len(options) <= 3:
        data = json.dumps({
            "recipient": {"id": id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "options",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[0]),
                                        "payload": try_ex(lambda: options[0])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[1]),
                                        "payload": try_ex(lambda: options[1])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[2]),
                                        "payload": try_ex(lambda: options[2])
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        })
        return data
    if 3 < len(options) <= 6:
        data = json.dumps({
            "recipient": {"id": id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Swipe left/right for more options.",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[0]),
                                        "payload": try_ex(lambda: options[0])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[1]),
                                        "payload": try_ex(lambda: options[1])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[2]),
                                        "payload": try_ex(lambda: options[2])
                                    }
                                ]
                            },
                            {
                                "title": "Swipe left/right for more options.",
                                "buttons": [
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[3]),
                                        "payload": try_ex(lambda: options[3])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[4]),
                                        "payload": try_ex(lambda: options[4])
                                    },
                                    {
                                        "type": "postback",
                                        "title": try_ex(lambda: options[5]),
                                        "payload": try_ex(lambda: options[5])
                                    }
                                ]
                            }
                        ]
                    }
                }
            }
        })
        return data


def resume_quiz():
    print("resume_quiz")


def get_name(id):
    print('Get Name', id)
    url = "https://graph.facebook.com/" + id
    print("url", url)
    response = requests.get(url=url,
                            params={
                                "fields": "first_name,last_name,profile_pic",
                                "access_token": PAGE_ACCESS_TOKEN
                            },
                            )

    data = json.loads(response.content.decode("utf-8"))
    global first_name
    first_name = data['first_name']
    global last_name
    last_name = data['last_name']
    name = first_name + " " + last_name
    return name


def try_ex(func):
    """
    Call passed in function in try block. If KeyError is encountered return None.
    This function is intended to be used to safely access dictionary.

    Note that this function would have negative impact on performance.
    """
    try:
        return func()
    except KeyError:
        return None
    except IndexError:
        return "-----"


if __name__ == "__main__":
    app.run()
