# Module d'envoi de la photo changée dans la base Mongo
import requests

def postEvent(keeper_id,keeper_token,image,date):
    payload = {'keeper_id':keeper_id, 'keeper_token':keeper_token,'image':image,'date':date}

    r = requests.post('http://localhost:3000/v1/event', data=payload)

    print(r.text)