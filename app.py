from aiohttp import ClientSession
import asyncio


async def main():
    url = "https://m.104.com.tw/search/joblist?jobsource=index_s&keyword=python&mode=s&page=1"
    async with ClientSession() as session:
        async with session.get(url) as response:
            print(f"{response.status = }")
            print(f"{response.headers['content-type'] = }")

            html = await response.text()

            print(f"{html[500:600] = }")


asyncio.run(main())
