from pprint import pprint
import asyncio

from aiotdlib import Client
from aiotdlib.api import API, FileTypePhoto

import src.modules.tg as config
from src.modules import NewsModule

tg_list = {
    "竹新社": -1001353105961,
    "乌鸦观察": -1001485445411
}


class Tg(NewsModule):
    def __init__(self):
        super().__init__()
        self.client = Client(
            api_id=config.appid,
            api_hash=config.api_hash,
            phone_number=config.phone,
            database_encryption_key=config.database_encryption_key,
        )
        self.client.add_event_handler(self.parse_message, update_type=API.Types.UPDATE_NEW_MESSAGE)

    async def parse_message(self, update):
        message_content = update
        pprint(message_content)

    def save_to_db(self):
        pass

    async def download_file(self, file_id):
        result = await self.client.api.get_remote_file(
            remote_file_id=file_id,
            file_type=FileTypePhoto()
        )
        result = await self.client.api.download_file(
            file_id=result.id,
            offset=0,
            priority=10,
            limit=83921,
            synchronous=True
        )
        pprint(result)

    def update(self):
        pass


async def create_tg():
    tg = Tg()

    async with tg.client:
        await tg.client.idle()
        return tg
