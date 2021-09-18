#!/usr/bin/env python3

"""
这个项目是干嘛的？
防止自己注册的小网站被黑了，我的全网账户密码全炸了。
"""

import hashlib, sys, getopt

def md5_passwd(mask, sitename, sitevalue):
    m = hashlib.md5()
    m.update(mask.encode('utf8'))
    m.update(sitevalue.encode('utf8'))

    # 首字母务必大写
    res = m.hexdigest()[:12]
    print(sitename + '\t -> \t' +\
          res[:1].title() +\
          res[1:])

if __name__ == '__main__':

    opts, args = getopt.getopt(sys.argv[1:], "hp:s:")

    if opts is None or len(opts) == 0:
        print("usage: ./FindMyPassword.py -p yourpasswordmask")
        sys.exit()

    for op, value in opts:

        if op == "-p":
            mask = value

        if op == "-h":
            print("usage: ./FindMyPassword.py -p yourpasswordmask")
            sys.exit()

    sites = {
        "qq": "qq.com",
        "weixin": "wechat.com",
        "zhihu": "zhihu.com",
        "apple": "apple.com",
        "google": "google.com",
        "fb": "facebook.com",
        "github": "github.com",
        "社保": "zwdtuser.sh.gov.cn",
        "网盘": "pan.baidu.com",
    }

    for k, v in sites.items():
        md5_passwd(mask, k, v)
