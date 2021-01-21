# https://zhuanlan.zhihu.com/p/69142198
import sys
import os
import re
import contextlib

def replace(content):
    dollar_double = r'\n<img src="https://www.zhihu.com/equation?tex=\1\\\\" alt="\1\\\\" class="ee_img tr_noresize" eeimg="1">\n'
    r_double = re.compile(r'\$\$\n*(.*?)\n*\$\$', re.DOTALL)

    dollar = r'<img src="https://www.zhihu.com/equation?tex=\1" alt="\1" class="ee_img tr_noresize" eeimg="1">\n'
    r = re.compile(r'\$\n*(.*?)\n*\$', re.DOTALL)

    content_new = r_double.sub(dollar_double, content)
    return r.sub(dollar, content_new)


if __name__ == '__main__':
    """Usage: python3 to_zhihu_md.py generalized_linear_model.ipynb
    """
    name, postfix = sys.argv[1].split('.')
    if postfix == 'ipynb':
        os.system(f'jupyter nbconvert --to markdown {sys.argv[1]}')
    with open(name + '.md') as fd_r, open(name + '_zhihu.md', 'w') as fd_w:
        content = fd_r.read()
        result = replace(content)
        fd_w.write(result)
