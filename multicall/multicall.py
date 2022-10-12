import asyncio
import httpx
import random

async def download_url(url):
    """
    - Na standardní výstup vypište text "Downloading url {url}"
    - Pomocí asynchronního volání knihovny httpx.AsyncClient.get načtěte obsah url ve formě jsonu
    - Vypište text "Url {url} downloaded"
    - Z funkce vraťte atribut "alt" ze získaného jsonu
    """
    pass


async def main():
    """
    - Pomocí asyncio.gather spusťte najednou minimálně 3 úlohy download_url.
    - Každá úloha bude náhodně stahovat data z xkcd api:
      "https://xkcd.com/{<0,600>}/info.0.json"
    - Na standardní výstup vypište proměnnou `data`
    """
    data = await asyncio.gather(...)
    print(data)

if __name__ == "__main__":
    asyncio.run(main())
