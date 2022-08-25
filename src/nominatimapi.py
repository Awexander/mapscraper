import aiohttp

class nominatimapi():
    def __init__(self) -> None:
        pass

    async def response(self, url):
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(30)) as session:
            async with session.get(url) as response:
                return await response.json()
                #https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>&zoom=19