from flask import Flask, request


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
    data = request.get_json()
    print(data)
    return "ok"

if __name__ == "__main__":
    app.run()