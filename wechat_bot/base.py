#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
连接微信：易被封web登录功能
@Time    : 18-7-12
@Author  : leemiracle
"""
import itchat
import time
from itchat.core import Core
from itchat import instanceList, originInstance
from itchat.content import *

# import sys
# sys.path.append('.')
# sys.path.append('..')

instance = originInstance


@instance.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    '''
    回复消息
    :param msg:
    :return:
    '''
    msg.user.send('%s: %s' % (msg.type, msg.text))


@instance.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    '''
    下载文件
    :param msg:
    :return:
    '''
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@instance.msg_register(FRIENDS)
def add_friend(msg):
    '''
    添加朋友
    :param msg:
    :return:
    '''
    msg.user.verify()
    msg.user.send('Nice to meet you!')


@instance.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    '''
    群聊
    :param msg:
    :return:
    '''
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


def main():
    instance.auto_login(enableCmdQR=2)
    instance.run(True)

    # # 获取自己的用户信息，返回自己的属性字典
    # itchat.search_friends()
    # # 获取特定UserName的用户信息
    # itchat.search_friends(userName='@abcdefg1234567')
    # # 获取任何一项等于name键值的用户
    # itchat.search_friends(name='littlecodersh')
    # # 获取分别对应相应键值的用户
    # itchat.search_friends(wechatAccount='littlecodersh')
    # # 三、四项功能可以一同使用
    # itchat.search_friends(name='LittleCoder机器人', wechatAccount='littlecodersh')


if __name__ == '__main__':
    main()
