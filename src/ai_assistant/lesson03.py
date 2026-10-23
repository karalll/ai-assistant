import asyncio
import httpx


async def get_data(client: httpx.AsyncClient, url: str) -> None:
    response = await client.get(url)
    print(response.status_code, url)

async def main() -> None:
    async with httpx.AsyncClient() as client:
        await asyncio.gather(
            get_data(client, "https://httpbin.org/get"),
            get_data(client, "https://httpbin.org/json")
        )
if __name__ == "__main__":
    asyncio.run(main()) 

