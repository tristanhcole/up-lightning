# Up Lightning ⚡
> Stop Saving Dollars, Start Stacking Sats

Round up your Up Bank transactions into Bitcoin via the Lightning Network (lnd). This is very much a prototype.

> Problem: all exchanges have a minimum purchase order of $10+ meaning dollar cost averaging in for the average person is hard

## How it Works
This is a _proof of concept_. It only works on a localhost bitcoin network (simnet).

1. A local Bitcoin network with a lnd channel open between two parties (Alice & Bob)
3. Web app accepts webhook from Up Bank
3. Round up transaction to the dollar amount
4. Create a lnd invoice for Bob of the round up amount
5. Pay the lnd invoice from Alice's account
6. ⚡

The idea is in the future to offer a micro-exchange solution for Bitcoin round-ups once Up Bank allows push payments and third-party apps.

## Setup
- Install [Lnd](https://dev.lightning.community/guides/installation/#installing-lnd) with [btcd backend](https://dev.lightning.community/guides/installation/#installing-btcd)
- Follow [LND tutorial to setup a local cluster](https://dev.lightning.community/tutorial/01-lncli/index.html). Don't disconnect the Alice<->Bob channel.
- If you followed the tutorial, simply add your username to the paths in `lnd_utils.py` (macOS only)
- Install requirements `pip install requirements.txt`
- Get your [Up Bank Token](https://api.up.com.au/getting_started) and add it to `up_utils.py` `UP_TOKEN`
- Run `python app.py`
- Run `ngrok http 5000` to expose localhost to up bank
- Go to `http://localhost:5000/` home for the app to automatically setup your webhook
- Create a real transaction in Up Bank (i.e. send 1c to a friends bank account)

## Todo/Ideas
- Turn hack code into prod code lol 
- Workerise webhook response according to [Up Bank API spec](https://developer.up.com.au/#callback_post_webhookURL)
- Dockerise [Bitcoin Node](https://github.com/LN-Zap/docker-btcd), [Lightning Node](https://github.com/LN-Zap/docker-lnd) and web app for easy deployment
- Push Payments to an exchange bank account
- Mobile App to see your balance
- Exchange Rates/Multi-Currency Roundups
- Provider/Micro-Exchange Service
- Hosted (custodial) and non-custodial solution
