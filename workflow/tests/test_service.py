import os

import emoji as emoji

from .test_base import TestBase
from Service.runner import json_reader, json_printer


class Service(TestBase):
    def test_json_reader(self):
        print(emoji.emojize("Start Testing for json_reader :snowflake:"))
        json_reader(os.getcwd() + "/tests/mock/mock_data.json")
        print(emoji.emojize('json_reader Test :thumbs_up:'))

    def test_json_printer(self):
        print(emoji.emojize("Start Testing for json_printer :snowflake:"))
        data = json_reader(os.getcwd() + "/tests/mock/mock_data.json")
        json_printer(data)
        print(emoji.emojize('json_printer Test :thumbs_up:'))