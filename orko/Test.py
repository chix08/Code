from flask import Flask, request

# import logging

app = Flask(__name__)
# logging.basicConfig(filename="newfile.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'Token'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = 'EAAiLqcUdUHoBABxHBM8qqR3kN44DTFPju1amv54IGX7NrU506SQiWdZA5AZCczaIRS7S3M8TtVaQuerVDEQsbOu63b34E5zYYY4o2OcvDQ6tSRfJNPcJQlg66oeO4Dd3B8ld18LvY1zzzDKj1cJx5GYIzlkro0kMZBBtrDeTkBIfm66RnkZAGTaD3Nnmk0IZD'


# logger = logging.getLogger()

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
    print(data)
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    print("In Handle Message")
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    message_text = messaging_event["message"]["text"]
                    send_message_response(sender_id, "Hello")

    return "ok"


def send_message(sender_id, message_text):
    '''
    Sending response back to the user using facebook graph API
    '''

    print("send message")
    # r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    #
    #                   params={"access_token": PAGE_ACCESS_TOKEN},
    #
    #                   headers={"Content-Type": "application/json"},
    #
    #                   data=json.dumps({
    #                       "recipient": {"id": sender_id},
    #                       "message": {"text": message_text}
    #                   }))
    return "Ok"


def send_message_response(sender_id, message_text):
    print("send_message_response")
    sentenceDelimiter = ". "
    messages = message_text.split(sentenceDelimiter)

    for message in messages:
        send_message(sender_id, message)


if __name__ == "__main__":
    app.run()
