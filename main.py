
import asyncio
from src.googlemap import shorturl
from src.nominatimapi import nominatimapi
import json

nomimapi = nominatimapi()
url = 'https://goo.gl/maps/PYHu4WvkFbWn41R19'

async def main():
    coord = await shorturl(url)
    data = await nomimapi.response(coord)
    with open('data/response.json', 'w') as w:
        json.dump(data, w, indent=4, separators=[',',':'])


asyncio.get_event_loop().run_until_complete(main())