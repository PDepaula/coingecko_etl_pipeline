import requests
import json

#Coingecko API and request urls for categories of 1): smart contract platforms 2): meme-tokens and 3): GameFi
cg_api = 'https://api.coingecko.com/api/v3/'
scp = 'coins/markets?vs_currency=usd&category=smart-contract-platform&order=market_cap_desc&per_page=50&page=1&sparkline=false'
meme = 'coins/markets?vs_currency=usd&category=meme-token&order=market_cap_desc&per_page=50&page=1&sparkline=false'
gamefi = 'coins/markets?vs_currency=usd&category=gaming&order=market_cap_desc&per_page=50&page=1&sparkline=false'

# API requests
response_scp = requests.get(cg_api + scp)
response_meme = requests.get(cg_api + meme)
response_gamefi = requests.get(cg_api + gamefi)

# Turn responses into json format
scp_response_to_json = response_scp.json()
meme_response_to_json = response_meme.json()
gamefi_response_to_json = response_gamefi.json()

# List buckets for the Json files
scp_json=[]
meme_json=[]
gamefi_json=[]

# Request urls to deal with pagination, global

cg_scp_api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=smart-contract-platform&order=market_cap_desc&per_page=50&'
cg_meme_api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=meme-token&order=market_cap_desc&per_page=50&'
gamefi_api = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&category=gaming&order=market_cap_desc&per_page=50&'

# Create a loop that will give back the response for all pages for smart contract platforms
def undo_pagination():

    for x in range(1,4):
        scp_page= f'{cg_scp_api}page={x}&sparkline=false'
        scp_multiresponse= requests.get(scp_page).json()
        for i in scp_multiresponse:
            scp_json.append(i)


    # Create a loop that will give back the response for all pages for meme tokens
    for x in range(1,3):
        meme_page = f'{cg_meme_api}page={x}&sparkline=false'
        meme_multiresponse= requests.get(meme_page).json()
        for i in meme_multiresponse:
            meme_json.append(i)


    # Create a loop that will give back the response for all gamefi pages
    for x in range(1,7):
        gamefi_page = f'{gamefi_api}page={x}&sparkline=false'
        gamefi_multiresponse= requests.get(gamefi_page).json()
        for i in gamefi_multiresponse:
            gamefi_json.append(i)