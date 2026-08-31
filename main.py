import asyncio

import httpx

from app.async_http import get_data

async def main():
    data = await get_data('https://httpbin.org/get')
    print(data)

