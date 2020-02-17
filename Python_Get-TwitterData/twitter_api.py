import oauth2
import json
import urllib.parse

api_key = 'zghyhbLKBLXiqmkxDUKbKBz1r'
api_secret_key = 'HdDSC7obpb7WvrWbf4EJco9DteG8ERUeKU2pDD7pP4XTZ9TEtC'

access_token = '1226296019975122944-6T0NocXaRhXWLW9D5ZdeEwnoRovgBU'
access_token_secret = 's60w8XXRArXGfK7VSCGVJ2GHJkroSCBNqzY4PCQVoLN1V'

consumer = oauth2.Consumer(api_key,api_secret_key)
token = oauth2.Token(access_token, access_token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_codificada = urllib.parse.quote(query, safe='')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=en')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']


for twit in twittes: 
    print(twit['user']['screen_name'])
    print(twit['text']) 
    print(twit['created_at'])
  
    
    print()

