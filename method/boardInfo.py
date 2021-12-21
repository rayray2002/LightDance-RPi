import os

from .baseMethod import BaseMethod


class BoardInfo(BaseMethod):
    def method(self, payload):
        info = [
            "boardInfo",
            {"name": os.name, "type": "dancer", "OK": True, "msg": "Success"},
        ]
        return info
