# https://zhuanlan.zhihu.com/p/69142198
import sys
import re
import contextlib

def replace(content):
    dollar_double = '\n<img src="https://www.zhihu.com/equation?tex=\1\\\\" alt="\1\\\\" class="ee_img tr_noresize" eeimg="1">\n'
    r_double = re.compile('\$\$\n*(.*?)\n*\$\$', re.DOTALL)

    dollar = '\n<img src="https://www.zhihu.com/equation?tex=\1" alt="\1" class="ee_img tr_noresize" eeimg="1">\n'
    r = re.compile('\$\n*(.*?)\n*\$', re.DOTALL)

    content_new = r_double.sub(dollar_double, content)
    return r.sub(dollar, content_new)


if __name__ == '__main__':
    name, postfix = sys.argv[1].split('.')
    with open(sys.argv[1]) as fd_r, open(name + '_zhihu.' + postfix, 'w') as fd_w:
        content = fd_r.read()
        result = replace(content)
        fd_w.write(result)
