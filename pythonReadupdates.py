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
                    #分割时考虑到Method字段对应的value中是httpd地址，会包含分割符:,因此指定只分割未两部分
                    strs = line.split(':',1)
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception :
            print("文件不存在，先创建updates文件")
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
        replace(self.file_name, key + ':.*', key + ': ' + value, True)


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

def checkppa:


def updateppa:

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f','--filename',help="指定需要操作的文件,默认为当前目录下的updates文件",default='updates')
    parser.add_argument('-N','--Name',help="指定Name,默认为update_from_crp",default='update_from_crp')
    parser.add_argument('-S','--Suite',help="指定Suite",default='unstable')
    parser.add_argument('-A','--Architectures',help="指定Architectures",default='i386 amd64')
    parser.add_argument('-C','--Components',help="指定Components",default='main')
    parser.add_argument('-M','--Method',help="指定Method链接",required=True)
    parser.add_argument('-V','--VerifyRelease',help="指定VerifyRelease",default='blindtrust')

    #初始化参数
    args = parser.parse_args()
    print(args.Name)
    
    #读取文件
    props = Properties(args.filename)  # 读取文件
    #根据配置生成文件
    props.set('Name',args.Name)
    props.set('Suite',args.Suite)
    props.set('Architectures',args.Architectures)
    props.set('Components',args.Components)
    props.set('Method',args.Method)
    props.set('VerifyRelease',args.VerifyRelease)

    print(props.properties)
    
    #更新ppa仓库


if __name__ == "__main__":
    main()
