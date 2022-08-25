
import aiohttp
import asyncio
from urllib.parse import urlparse

url = 'https://goo.gl/maps/Bxe2SrQEDZHZVo6s7'
async def main():
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(30)) as session:
        async with session.head(url, allow_redirects=False) as resp:
            longURL = resp.headers.get('Location')
    
            path = urlparse(longURL).path.split('/')
            coord = ''
            for p in path: 
                l = p.strip()
                if bool(l) is False: pass
                elif l[0] == '@': 
                    coord = p[1:]
                    break
            
            print(coord)
            

asyncio.get_event_loop().run_until_complete(main())