import os
import shutil


class CSDN(object):
    def __init__(self, args, info, config):
        self.args = args
        self.article_info = info
        self.config = config
        self.skip_list = {
            "entrypoint": True
        }
        self.is_login = False
        self.host = 'https://blog.csdn.net/'

    def login(self):
        self.cookie = ''

        self.is_login = True
        pass

    def format_info(self):
        pass

    def to_me(self):
        pass
