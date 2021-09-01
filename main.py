from src.modules.tg.tg import create_tg
import asyncio


async def main():
    await create_tg()


if __name__ == '__main__':
    asyncio.run(main())
