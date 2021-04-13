#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import os
import tempfile
import argparse


class Properties:
    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find(':') > 0 and not line.startswith('#'):
                    strs = line.split(':')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception :
            raise e
        else:
            fopen.close()

    def has_key(self, key):
        return key in self.properties

    def get(self, key, default_value=''):
        if key in self.properties:
            return self.properties[key]
        return default_value

    def set(self, key, value):
        self.properties[key] = value
        replace(self.file_name, key + ':.*', key + ':' + value, True)


def replace(file_name, from_regex, to_str, append_on_not_exists=True):
    tmpfile = tempfile.TemporaryFile()

    if os.path.exists(file_name):
        r_open = open(file_name, 'r')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open:
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            tmpfile.write(line.encode())
        if not found and append_on_not_exists:
            tmpfile.write((to_str+'\n').encode())
        r_open.close()
        tmpfile.seek(0)

        content = tmpfile.read()

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name, 'wb')
        w_open.write(content)
        w_open.close()

        tmpfile.close()
    else:
        print ("file %s not found" % file_name)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--test',help="this is a test")
    parser.add_argument('-f','--filename',help="file name")
    parser.add_argument('-m','--Method',help="指定Method链接")
    args = parser.parse_args()
    print(args.filename)

    file_path = 'updates'
    props = Properties(file_path)  # 读取文件
    props.set('jdbc.url', 'value_a')  # 修改/添加key=value
    print (props.get('key_a'))  # 根据key读取value

if __name__ == "__main__":
    main()
