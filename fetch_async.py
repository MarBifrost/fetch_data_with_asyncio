import aiohttp
import asyncio
import json
import aiofiles
import time


async def fetch(url, session):
    async with session.get(url) as resp:
        return await resp.json()


async def main():
    start_time = time.time()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for post_id in range(1, 78):
            url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
            tasks.append(fetch(url, session))

        result = await asyncio.gather(*tasks)

    async with aiofiles.open('data.json', 'w') as file:
        await file.write(json.dumps(result, indent=4))

    end_time = time.time()
    total_time = end_time - start_time
    print(f"total time with asyncio: {total_time}")
    threads_total_time = "total time with threading: 0.692657470703125"
    print(threads_total_time)

if __name__ == '__main__':
    asyncio.run(main())
