#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Yuande Liu <miraclecome (at) gmail.com>
# pip install python-markdown-math
# pip install markdown

import sys
import markdown
from mdx_math import MathExtension

exts = ['markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        MathExtension(enable_dollar_delimiter=True)]

html_head = """
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-MML-AM_CHTML-full,Safe' async></script>
<meta content="text/html; charset=utf-8" http-equiv="content-type" />
<link href="github.css" rel="stylesheet">
</head>

<body>
"""
html_tail = "\n</body>\n</html>"

if __name__ == '__main__':
    name, postfix = sys.argv[1].split('.')
    with open(name + '.' + postfix) as fd_r, open(name + '.html', 'w') as fd_w:
        content = fd_r.read()

        md = markdown.Markdown(extensions = exts)
        html_body = md.convert(content)

        fd_w.write(html_head + html_body + html_tail)
