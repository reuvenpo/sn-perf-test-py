import asyncio
import json
from datetime import datetime

# import aiohttp
import httpx


async def get(session, url, handler):
    response = await session.get(url)
    await handler(response)


async def handle_grpc(response):
    text = response.text
    print(response.http_version)
    print(text)
    # parsed = json.loads(text)
    # balance = parsed['balances'][0]['amount']
    # print(response.status, balance)


async def main():
    start = datetime.now()

    async with httpx.AsyncClient(http2=True) as session:
        balance_url = 'http://52.170.156.1:9091/cosmos/bank/v1beta1/balances/secret1xvf02egq8tmngaft9xgcu0cdwk5623fua776p5'
        queries = [get(session, balance_url, handle_grpc) for _ in range(1)]

        _, _ = await asyncio.wait(queries)

    end = datetime.now()
    print(f'took {(end - start).total_seconds()}s')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
