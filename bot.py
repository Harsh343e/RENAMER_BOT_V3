import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5894152836:AAG2nRjIOrIK4Pv2lXWhOh-kXNamW6-yX9k")

API_ID = int(os.environ.get("API_ID", "21941890"))

API_HASH = os.environ.get("API_HASH", "a192de10945cf3685dbe8ae711b238d8")

STRING = os.environ.get("STRING", "BQFOzoIAjjdfaWs-fnZqimHT8InmW8zOG97rRJN_IbStlnTjogeWsjLIWxORUjMq4mcEMRwVoLfAFCszzpM5Bai7aBrihX_YNfIJGvAG4VOfUXSwzzHPt5zH7sALBEY4hgq5KmCVXhSrBEnrpUKb3iQlwWHSe2nPpz0Rx3KGwK4W52vUrj8gjNRT5vb6cLGY2miO37kJwpeot-Wbuf3urH6tbZW3nFZ901qVfskkOWkq0BBEDg1zR6Dp75yCqJyH5Fgj22jTVAlZY0ZqHZ5TON6aEa3OsnIspnEOlupUXo0ynXr9xfwxkKAwQxmFyDGd7_-D1pKBvI1HwRHvVltW6kl_EzC82wAAAABRcF5sAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
