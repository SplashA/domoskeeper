# Module d'envoi de SMS par le biais de Twilio
from twilio.rest import Client

def sendSms(fromNum,toNum,mess):
    # Votre SID de compte (twilio.com/console)
    account_sid = "ACfc4a8710964ebcc48f2b0acd8ac4c7f6"
    # Votre token d'autorisation (twilio.com/console)
    auth_token  = "4faf134c2579679d3f8fe24e04d2f006"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=toNum, 
        from_=fromNum,
        body=mess)


