#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>

# not support math, please use vscode to convert
import sys
import markdown

if __name__ == '__main__':
    name, postfix = sys.argv[1].split('.')
    with open(name + '.' + postfix) as fd_r, open(name + '.html', 'w') as fd_w:
        content = fd_r.read()
        html = markdown.markdown(content)
        fd_w.write(html)
