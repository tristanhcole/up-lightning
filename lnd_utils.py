import lnd_grpc


def aud_to_satoshi(aud):
    """
    As of 22nd August 2020.

    # 1.00 AUD = 6174 Satoshi
    :param aud: Integer, AUD in cents 1.00 = 100
    :return:
    """
    satoshi_rate = 61.74  # one AUD cent to Satoshi
    return round(aud*satoshi_rate)


def generate_lightning_invoice(desc, value):
    """

    :param desc: string, description
    :param value: integer, in base units -107.92 is -10792
    :return:
    """
    round_up_in_cents = abs((abs(value) % 100) - 100)
    invoice_value = aud_to_satoshi(round_up_in_cents)

    bob_lnd_rpc = lnd_grpc.Client(
        lnd_dir="/Users/[username]/Library/Application Support/Lnd/",
        macaroon_path='/Users/[username]/go/dev/bob/data/chain/bitcoin/simnet/admin.macaroon',
        tls_cert_path='/Users/[username]/Library/Application Support/Lnd/tls.cert',
        network='simnet', grpc_host='localhost', grpc_port='10002')

    print(bob_lnd_rpc.get_info())

    invoice = bob_lnd_rpc.add_invoice(desc, value=invoice_value)

    print(invoice)

    return invoice


def pay_lightning_invoice(invoice):
    alice_lnd_rpc = lnd_grpc.Client(
        lnd_dir="/Users/[username]/Library/Application Support/Lnd/",
        macaroon_path='/Users/[username]/go/dev/alice/data/chain/bitcoin/simnet/admin.macaroon',
        tls_cert_path='/Users/[username]/Library/Application Support/Lnd/tls.cert',
        network='simnet', grpc_host='localhost', grpc_port='10001'
    )
    print(alice_lnd_rpc.get_info())

    send_payment = alice_lnd_rpc.pay_invoice(payment_request=invoice.payment_request)

    print(send_payment)
