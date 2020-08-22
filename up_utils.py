import requests

NGROK_HOST = '<YOUR_NGROK_HOST>'  # i.e. https://cae843f1ec06.ngrok.io

UP_HOST = 'https://api.up.com.au/api/v1'
UP_TOKEN = '<YOUR_UP_TOKEN>'  # i.e. up:demo:KXPLEkrOF8jWaGfX


def create_webhook():
    data = {"data": {"attributes": {'url': f"{NGROK_HOST}/webhook", 'description': 'Up Lightning'}}}
    headers = {"Authorization": f"Bearer {UP_TOKEN}"}
    request = requests.post(f"{UP_HOST}/webhooks", json=data, headers=headers)
    return request


def retrieve_transaction(link):
    headers = {"Authorization": f"Bearer {UP_TOKEN}"}
    request = requests.get(link, headers=headers)
    return request


if __name__ == '__main__':
    create_webhook()
