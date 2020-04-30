#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018.2.27
@author: laofeng
@note: kazoo 访问  zookeeper
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from kazoo.client import KazooClient,KazooState
'''
import logging
logging.basicConfig(
    level=logging.DEBUG
    ,stream=sys.stdout
    ,format='%(asctime)s %(pathname)s %(funcName)s%(lineno)d %(levelname)s: %(message)s')
'''
#递归遍历所有节点的子节点函数,_zk是KazooClient的对象，node是节点名称字符串，func是回调函数
def zk_walk(_zk, node, func):
    data, stat = _zk.get(node)
    children = _zk.get_children(node)
    func(node, data, stat, children);
    if len(children) > 0:
        for sub in children:
            sub_node = ''
            if node != '/':
                sub_node = node + '/' + sub
            else:
                sub_node = '/' + sub
            zk_walk(_zk, sub_node, func)
            
#测试zk_walk的打印回调函数，只是把所有数据都打印出来
def printZNode(node,  data, stat, children):
    print("node  : " + node)
    print("data  : " + str(data))
    print("stat  : " + str(stat))
    print("child : " + str(children))
    print '\n'
    
#创建一个客户端，可以指定多台zookeeper，
zk = KazooClient(
    hosts='127.0.0.1:2181'
    ,timeout=10.0  #连接超时间
    )
#开始心跳
zk.start()

#遍历谋个节点的所有子节点
zk_walk(zk, '/', printZNode)

#执行stop后所有的临时节点都将失效
zk.stop()
zk.close()

