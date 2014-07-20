import json
import click
import requests


@click.group()
def cli():
    """Main entry point."""


@cli.group()
def notify():
    """Simulate URL notifications"""


@notify.command()
@click.argument('url')
@click.option('--dtag', type=int, default=None, help="use destination tag")
@click.option('--amount', type=str, default=None, help="set amount (format: 10/USD)")
def payment(url, dtag, amount):
    """Send a payment notification.
    """

    # TODO: Ask a test server for a formatted notification, so we always
    # get it right, and make that test server support validation of these
    # fakes.

    true = True; false = False
    template = {
        "transaction": {
          "hash": "A667534FBE95827EBBF4B7027D4C6405550FC281DC176D40613AC4EE937E11F0",
          "Sequence": 7,
          "TransactionType": "Payment",
          "SigningPubKey": "03E2B079E9B09AE8916DA8F5EE40CBDA9578DBE7C820553FE4D5F872EEC7B1FDD4",
          "Flags": 0,
          "Fee": "12",
          "Amount": "1000000",
          "Account": "rhq549rEtUrJowuxQC2WsHNGLjAjBQdAe8",
          "Destination": "rD7khdZL58PyhujLwM1Kx7yHBmoxPJ7vPw",
          "TxnSignature": "304602210084C36B1A1016ABBD8ADDE37EE7C4FD45C3FC9FE53845D24C2BCE93B9A3A8D5F6022100A1CCAD1245D6DD37B77BF4165AB36213D75FF012423DA9ED3D3D841FC57E8C42",
          "metaData": {
            "TransactionResult": "tesSUCCESS",
            "AffectedNodes": [
              {
                "ModifiedNode": {
                  "LedgerIndex": "6260DA55EBD73936F8DD792557B8E50BEBF2FED9D661F08711283F8B63CB0DD2",
                  "PreviousTxnLgrSeq": 4304680,
                  "PreviousFields": {
                    "Sequence": 7,
                    "Balance": "39999928"
                  },
                  "LedgerEntryType": "AccountRoot",
                  "FinalFields": {
                    "Flags": 0,
                    "Balance": "38999916",
                    "Sequence": 8,
                    "Account": "rhq549rEtUrJowuxQC2WsHNGLjAjBQdAe8",
                    "OwnerCount": 2
                  },
                  "PreviousTxnID": "4F8954A3617C3104DF9FAD81B70E794A2441DF1FC9411F524600A04BBB8C26C6"
                }
              },
              {
                "ModifiedNode": {
                  "LedgerIndex": "CCE2D80C6762BA3591AB7F16DEB819CDF30EA1D1F28ED0DB486F75F2E09AE390",
                  "PreviousTxnLgrSeq": 4304447,
                  "PreviousFields": {
                    "Balance": "16229610429"
                  },
                  "LedgerEntryType": "AccountRoot",
                  "FinalFields": {
                    "Flags": 0,
                    "Balance": "16230610429",
                    "Sequence": 48,
                    "Account": "rD7khdZL58PyhujLwM1Kx7yHBmoxPJ7vPw",
                    "OwnerCount": 5
                  },
                  "PreviousTxnID": "9AEB7E1A8655CB0BF44532C0CE3D0871F32CD77121181B7227765EA5D7D03009"
                }
              }
            ],
            "TransactionIndex": 2
          }
        },

        "ledger": {
          "close_time_resolution": 10,
          "ledger_hash": "D5775756E3DEE8574D8BF3E9BA3EBF2E6DCD0F705D0D737D5561E24C8839B327",
          "close_time": 442523930,
          "hash": "D5775756E3DEE8574D8BF3E9BA3EBF2E6DCD0F705D0D737D5561E24C8839B327",
          "ledger_index": "4318707",
          "transactions": 1,
          "seqNum": "4318707",
          "transaction_hash": "032D29F7B1A1E37E264867028E7736D889682BECB9E2ACC679EFBAF1091869FD",
          "closed": true,
          "parent_hash": "176B2B0AB2B687C25804962FEAB705F57C99FE2F4D5C4F77ED35DF6C1B951D35",
          "totalCoins": "99999998169004873",
          "accepted": true,
          "account_hash": "10D1FC9E0146AF22AB63CA5DD98271B5D3CBB845A6E7E532AE18B1EA5C4F36AD",
          "total_coins": "99999998169004873",
          "close_time_human": "2014-Jan-08 19:18:50"
        },

        "data": {
            'type': 'payment',
            'sender': "rhq549rEtUrJowuxQC2WsHNGLjAjBQdAe8",
            'destination': "rD7khdZL58PyhujLwM1Kx7yHBmoxPJ7vPw",
            'amount': '1',
            'currency': 'XRP'
        }
    }

    if dtag:
        template['data']['tag'] = dtag
        template['transaction']['DestinationTag'] = dtag

    if amount:
        parts = amount.split('/', 2)
        if len(parts) == 1:
            amount = parts[0]
            currency = 'XRP'
        elif len(parts) == 2:
            amount = parts[0]
            currency = parts[1]
        template['data']['amount'] = amount
        template['data']['currency'] = currency


    response = requests.post(
        url,
        json.dumps(template),
        headers = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        })
    print('Response: %s' % response.status_code)
    print(response.text)



if __name__ == '__main__':
    cli()
