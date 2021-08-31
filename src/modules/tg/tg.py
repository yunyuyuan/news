from telegram.client import Telegram
from src.modules import NewsModule
import src.modules.tg as config
from pprint import pprint

tg_list = {
    "竹新社": -1001353105961,
    "乌鸦观察": -1001485445411
}


class Tg(NewsModule):
    def __init__(self):
        super().__init__()
        self.tg = Telegram(
            api_id=config.appid,
            api_hash=config.api_hash,
            phone=config.phone,
            database_encryption_key=config.database_encryption_key,
        )
        # you must call login method before others
        self.tg.login()
        self.tg.add_message_handler(self.parse_message)
        self.tg.idle()
        result = self.tg.call_method("getRemoteFile", {
            'remote_file_id_': 'AgACAgUAAx0CUKbCKQACQLRhLhf6BmUe3TZm3Lj425mLBZGfnwACwrAxG9QlcFWEHPGqe4RYEGyrVXN0AAMBAAMCAAN4AAN7hAQAAR4E',
            'file_type_ ': -1718914651,
        })
        print(result)
        # self.tg.call_method("downloadFile", {
        #     'file_id_': 'AgACAgUAAx0CUKbCKQACQLRhLhf6BmUe3TZm3Lj425mLBZGfnwACwrAxG9QlcFWEHPGqe4RYEGyrVXN0AAMBAAMCAAN4AAN7hAQAAR4E',
        #     'priority_': 10,
        #     'offset_': 0,
        #     'limit_': 83921,
        #     'synchronous_': True
        # })

    def parse_message(self, update):
        message_content = update
        pprint(message_content)

    def save_to_db(self):
        pass

    def update(self):
        pass
