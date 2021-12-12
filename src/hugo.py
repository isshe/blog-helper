import os
import shutil


class HUGO(object):
    def __init__(self, args, info, config):
        self.args = args
        self.article_info = info
        self.config = config
        self.skip_list = {
            "entrypoint": True
        }

    def format_info(self):
        res = ""
        info = self.article_info
        skip_list = self.skip_list
        for k, v in info.items():
            if skip_list.get(k, False):
                continue
            if isinstance(v, list):
                if len(v) > 0:
                    v = '[ "' + '", "'.join(v) + '" ]'
                else:
                    # next one
                    continue
            else:
                v = '"' + str(v) + '"'
            res = "{}{} = {}\n".format(res, k, v)

        return res

    def to_me(self):
        args = self.args
        info = self.article_info
        src_path = args['article_path']
        entrypoint = info['entrypoint']

        # TODO: support specify output root directory: root/hugo
        dst_path = "hugo"

        # create output dir
        # os.mkdir("hugo")
        if os.path.exists(dst_path):
            shutil.rmtree(dst_path)
        shutil.copytree(src_path, dst_path)

        info_path = dst_path + "/info.json"
        if os.path.exists(info_path):
            os.remove(info_path)

        # output
        index_file = dst_path + "/index.md"
        with open(index_file, "w+") as f:
            f.write("+++\n")
            f.write(self.format_info())
            f.write("+++\n\n")

            content_file = "{}/{}".format(src_path, entrypoint)
            with open(content_file, "r") as cf:
                f.write(cf.read())

        return dst_path
