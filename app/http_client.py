import asyncio  # noqa: F401

import httpx


async def get_data(url:str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        
    return response.json()

