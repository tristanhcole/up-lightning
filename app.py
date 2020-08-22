from flask import Flask, request
import up_utils
import lnd_utils

app = Flask(__name__)


@app.route('/')
def webapp():
    up_utils.create_webhook()
    return 'Created Up Bank Webhook!'


@app.route('/webhook', methods = ['POST'])
def webhook():
    if request.method == 'POST':
        if request.json['data']['attributes']['eventType'] == 'TRANSACTION_CREATED':
            link = request.json['data']['relationships']['transaction']['links']['related']

            # Get the Up Bank transaction
            transaction = up_utils.retrieve_transaction(link)

            attributes = transaction.json()['data']['attributes']
            if attributes['amount']['currencyCode'] == 'AUD':
                value = attributes['amount']['valueInBaseUnits']
                desc = attributes['description']

                # Generate a Lightning Invoice
                invoice = lnd_utils.generate_lightning_invoice(desc, value)

                # Pay the Lightning Invoice
                lnd_utils.pay_lightning_invoice(invoice)

        return ''


if __name__ == '__main__':
    app.run()
