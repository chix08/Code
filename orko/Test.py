from flask import Flask, request


app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'Token'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = 'AAALLLcUdUHoBABxHBM8qqR3kN44DTFPju1amv54IGX7NrU506SQiWdZA5AZCczaIRS7S3M8TtVaQuerVDEQsbOu63b34E5zYYY4o2OcvDQ6tSRfJNPcJQlg66oeO4Dd3B8ld18LvY1zzzDKj1cJx5GYIzlkro0kMZBBtrDeTkBIfm66RnkZAGTaD3Nnmk0IZD'


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
                    print('sender_id',sender_id)
                    print('r_id',recipient_id)
                    print('message',message_text)
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

#
# curl -X POST -H "Content-Type: application/json" -d '{
#   "messaging_type": "Response", #RESPONSE, UPDATE, MESSAGE_TAG
#   "recipient": {
#     "id": "2099678400137828" #Sender ID
#   },
#   "message": {
#     "text": "hello, world!"
#   }
# }' "https://graph.facebook.com/v4.0/me/messages?access_token=AAAAAAcUdUHoBAGGhb347heA3QWZAPiW2ZAHdzsAe89BwfFZArc89yvFqBGmkUZBxi68IvyFjH5lhSLoWjF2Bci8Ye4tTFZBwLZAKwRqTwwqmKdKnEq3epY4fqJIDw3NbVWAMJ55ZC5rZAtA08AOBjKuNEnzZCtm40CresWpiPB5IfpfZB9L8M0chFKPFND85zlmQsZD"


#
# curl -X POST -H "Content-Type: application/json" -d '{
#   "recipient":{
#     "id":"2099678400137828"
#   },
#   "message":{
#     "attachment":{
#       "type":"template",
#       "payload":{
#         "template_type":"button",
#         "text":"Try the postback button!",
#         "buttons":[
#           {
#             "type":"postback",
#             "title":"Postback",
#             "payload":"DEVELOPER_DEFINED_PAYLOAD"
#           },
#           {
#             "type":"postback",
#             "title":"Postback1",
#             "payload":"DEVELOPER_DEFINED_PAYLOAD"
#           },
#           {
#             "type":"postback",
#             "title":"Postback2",
#             "payload":"DEVELOPER_DEFINED_PAYLOAD"
#           }
#         ]
#       }
#     }
#   }
# }' "https://graph.facebook.com/v4.0/me/messages?access_token=AAAAAAcUdUHoBAGGhb347heA3QWZAPiW2ZAHdzsAe89BwfFZArc89yvFqBGmkUZBxi68IvyFjH5lhSLoWjF2Bci8Ye4tTFZBwLZAKwRqTwwqmKdKnEq3epY4fqJIDw3NbVWAMJ55ZC5rZAtA08AOBjKuNEnzZCtm40CresWpiPB5IfpfZB9L8M0chFKPFND85zlmQsZD"
# -------------------------------------------------------
# O
# R
# K