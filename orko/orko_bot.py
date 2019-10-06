from flask import Flask, request
import requests
import json

app = Flask(__name__)

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'Token'  # <paste your verify token here>
PAGE_ACCESS_TOKEN = 'EAAiLqcUdUHoBABxHBM8qqR3kN44DTFPju1amv54IGX7NrU506SQiWdZA5AZCczaIRS7S3M8TtVaQuerVDEQsbOu63b34E5zYYY4o2OcvDQ6tSRfJNPcJQlg66oeO4Dd3B8ld18LvY1zzzDKj1cJx5GYIzlkro0kMZBBtrDeTkBIfm66RnkZAGTaD3Nnmk0IZD'


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
    try:
        data = request.get_json()
        print(data)
        id = data['entry'][0]['messaging'][0]['sender']['id']
        print(id)
        text = data['entry'][0]['messaging'][0]['message']['text']
        print(text)
        send_response(id)
    except KeyError:
        print("Key Error")
    return "ok"
def send_response(id):
    print("in ID",id)
    name = get_name(id)
    message_text = "Hi"+" "+name
    requests.post("https://graph.facebook.com/v2.6/me/messages",

                  params={"access_token": PAGE_ACCESS_TOKEN},

                  headers={"Content-Type": "application/json"},

                  data=json.dumps({
                      "recipient": {"id": id},
                      "message": {"text": message_text}
                  }))
    return "ok"
def get_name(id):
    print('Get Name',id)
    url = "https://graph.facebook.com/"+id
    print("url",url)
    response = requests.get(url=url,
                 params={
                 "fields":"first_name,last_name,profile_pic",
                 "access_token": PAGE_ACCESS_TOKEN
                 },
    )

    data =json.loads(response.content.decode("utf-8"))
    name = data['first_name']+" "+data['last_name']
    return name

if __name__ == "__main__":
    app.run()