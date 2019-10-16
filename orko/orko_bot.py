from flask import Flask, request
import requests
import json

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'Token'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = 'AAALLLcUdUHoBABxHBM8qqR3kN44DTFPju1amv54IGX7NrU506SQiWdZA5AZCczaIRS7S3M8TtVaQuerVDEQsbOu63b34E5zYYY4o2OcvDQ6tSRfJNPcJQlg66oeO4Dd3B8ld18LvY1zzzDKj1cJx5GYIzlkro0kMZBBtrDeTkBIfm66RnkZAGTaD3Nnmk0IZD'
start_quiz = False
first_name = ''
last_name = ''


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
    id = try_ex(lambda: data['entry'][0]['messaging'][0]['sender']['id'])
    text = try_ex(lambda: data['entry'][0]['messaging'][0]['message']['text'])
    # send_response(id)
    # quiz_start(id)
    ready_quiz(id, message="let's start")
    return "ok"


def send_response(id):
    print("in ID", id)
    name = get_name(id)
    message_text = "Hi" + " " + name
    requests.post("https://graph.facebook.com/v2.6/me/messages",

                  params={"access_token": PAGE_ACCESS_TOKEN},

                  headers={"Content-Type": "application/json"},

                  data=json.dumps({
                      "recipient": {"id": id},
                      "message": {"text": message_text}
                  }))
    return "ok"


def ready_quiz(id, message):
    message_text = message

    data = {
        "recipient": {"id": id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": message_text,
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": " Yes",
                                    "payload": "yes"
                                },
                                {
                                    "type": "postback",
                                    "title": " No",
                                    "payload": "no"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    data = json.dumps(data)
    url = 'https://graph.facebook.com/v4.0/me/messages?access_token=' + PAGE_ACCESS_TOKEN
    headers = {"Content-Type": "application/json"}
    response = requests.post(url=url, headers=headers, data=data)

    return response


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


def quiz_start(id):
    message = "Are you ready for the quiz"
    response = ready_quiz(id, message)
    return response


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


if __name__ == "__main__":
    app.run()
