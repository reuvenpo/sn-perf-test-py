import asyncio
import json
from datetime import datetime

import aiohttp


async def get(session, url, handler):
    async with session.get(url) as response:
        await handler(response)


async def handle_grpc(response):
    text = await response.text()
    parsed = json.loads(text)
    balance = parsed['balances'][0]['amount']
    # print(response.status, balance)


async def handle_rest(response):
    text = await response.text()
    parsed = json.loads(text)
    balance = parsed['result'][0]['amount']
    # print(response.status, balance)


async def main():
    start = datetime.now()

    async with aiohttp.ClientSession() as session:
        balance_url = 'http://52.170.156.1:1317/cosmos/bank/v1beta1/balances/secret1xvf02egq8tmngaft9xgcu0cdwk5623fua776p5'
        queries = [get(session, balance_url, handle_grpc) for _ in range(2000)]

        # balance_url = 'http://52.170.156.1:1317/bank/balances/secret1xvf02egq8tmngaft9xgcu0cdwk5623fua776p5'
        # queries = [get(session, balance_url, handle_rest) for _ in range(2000)]

        _, _ = await asyncio.wait(queries)

    end = datetime.now()
    print(f'took {(end - start).total_seconds()}s')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
