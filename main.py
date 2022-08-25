
import asyncio
from src.googlemap import shorturl
from src.nominatimapi import nominatimapi

nomimapi = nominatimapi()
url = 'https://goo.gl/maps/riWVtrtYbq8WG71e8'

async def main():
    coord = await shorturl(url)
    print(await nomimapi.response(coord))

asyncio.get_event_loop().run_until_complete(main())