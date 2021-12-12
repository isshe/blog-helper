import os
import sys
import getopt
from hugo import HUGO
from csdn import CSDN
import json


def help():
    print(
        """
usage: python3 hblog.py -p [article-path] [option]
Options:
-p      : specify the article path.
        """)


def is_valid_article_path(article_path):
    if not os.path.exists(article_path):
        return False

    if not os.path.exists(article_path + "/info.json"):
        return False

    return True


def is_valid_entry_point(file):
    if not file or not os.path.exists(file):
        return False

    return True


def main():

    argv = sys.argv[1:]
    try:
        opts, _ = getopt.getopt(argv, "p:h")  # 短选项模式
    except:
        help()
        exit(1)

    args = {}
    print("opts = ", opts)
    for opt, arg in opts:
        if opt in ['-p']:
            if not is_valid_article_path(arg):
                print("Error: bad article path")
                exit(1)

            args['article_path'] = arg

    print("args = ", args)

    # TODO: read config
    config = {}

    # TODO: read article config
    with open(args['article_path'] + '/info.json') as json_file:
        article_info = json.load(json_file)

    if is_valid_entry_point(article_info['entrypoint']):
        print("Error: bad article entry point")
        exit(1)

    hugo = HUGO(args, article_info, config)
    hugo.to_me()

    # csdn = CSDN(args, article_info, config)
    # csdn.to_me()


if __name__ == "__main__":
    exit(main())
