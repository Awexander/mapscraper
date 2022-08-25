
import aiohttp
from urllib.parse import urlparse

async def shorturl( url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(30)) as session:
        async with session.head(url, allow_redirects=False) as resp:
            longURL = resp.headers.get('Location')
    
            path = urlparse(longURL).path.split('/')
            coord = ''
            for p in path: 
                l = p.strip()
                if bool(l) is False: pass
                elif l[0] == '@': 
                    coord = p[1:-1].split(',')
                    return f'https://nominatim.openstreetmap.org/reverse?lat={float(coord[0])}&lon={float(coord[1])}&zoom={int(coord[2])}&format=jsonv2'
                    #return f'https://www.openstreetmap.org/#map={coord[2]}/{coord[0]}/{coord[1]}'