# -*- coding: utf-8 -*-
"""
用于转MD5
"""
import hashlib


def ToMd5(text):
    md5_text = hashlib.md5()
    md5_text.update(text.encode(encoding='utf-8'))
    return md5_text.hexdigest()


# 测试
if __name__ == '__main__':
    testText = input('请输入转MD5的字符')
    print(ToMd5(testText))
