import asyncio
import json  # noqa: F401
import time

import httpx  # noqa: F401
from http_client import get_data


async def main():
    start = time.perf_counter()
    
    info1, info2 = await asyncio.gather( get_data('https://httpbin.org/get'), get_data('https://httpbin.org/uuid'))
    print(info1, info2)
    print(f'{time.perf_counter() - start}: end')
    
asyncio.run(main())

#sleep - 3.3
#gather - 0.7