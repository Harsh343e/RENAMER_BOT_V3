import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5894152836:AAG2nRjIOrIK4Pv2lXWhOh-kXNamW6-yX9k")

API_ID = int(os.environ.get("API_ID", "21941890"))

API_HASH = os.environ.get("API_HASH", "a192de10945cf3685dbe8ae711b238d8")

STRING = os.environ.get("STRING", "BQFOzoIAZb6WIaRABxeIfyXO1YHW2-3l-a9EIxzsAO8CVNHM8vIHFpKKpNcoc3a5txLJdGYMHmoroV7_bKinqhKDzJ2HeYDc3g7s23HZVpI-Y-HNQIA_uxpeDAlSSw1LagpUNGjW0OHq3UfxVlfCxnlK5xaUIaJIIQ540g1qos_9qQAW6hxYLzIpPNxpVl4Sq9xlJvNGIRVu75Lx_hP4nF3XfbCqV9NB_BciwDke9qS0GAssmzRMM7_i4U4TQ01nXccboFPjNjiTUI4I6ssH9LaPhpcG3ju7iIaJReEmYvKQnOyVlpLpsOEiSPd4dL2maxygrJL5BPKtdqTs8n-mFuMBo5urxgAAAABRcF5sAA")


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
