import asyncio
import json
from datetime import datetime

import aioh2


async def main():
    start = datetime.now()

    client = await aioh2.open_connection('0.0.0.0', 9091, functional_timeout=0.1)

    end = datetime.now()
    print(f'took {(end - start).total_seconds()}s')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
