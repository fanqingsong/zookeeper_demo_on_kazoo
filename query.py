#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2018.2.27
@author: laofeng
@note: kazoo 访问  zookeeper
'''
import sys
from kazoo.client import KazooClient,KazooState
import logging
logging.basicConfig(
    level=logging.DEBUG
    ,stream=sys.stdout
    ,format='%(asctime)s %(pathname)s %(funcName)s%(lineno)d %(levelname)s: %(message)s')

#创建一个客户端，可以指定多台zookeeper，
zk = KazooClient(
    hosts='127.0.0.1:2181'
    ,timeout=10.0  #连接超时时间
    , logger=logging #传一个日志对象进行，方便 输出debug日志
    )
#开始心跳
zk.start()

#获取根节点数据和状态
data, stat = zk.get('/')

print data   #这行没有输出，‘/’根节点，并没有数据
print stat   
'''
这个是stat的输出：
ZnodeStat(czxid=0, mzxid=0, ctime=0, mtime=0, version=0, cversion=8448, aversion=0, ephemeralOwner=0, dataLength=0, numChildren=4, pzxid=4295036257L)
ZnodeState的属性列表:
czxid ： 创建这个节点时的zxid
mzxid : 修改这个节点时的zxid
ctime ： 创建时间
mtime : 修改时间
version : 数据被修改的次数
cversion: 子节点被修改的次数
aversion: acl被改变的次数
ephemeralOwner:临时节点创建的用户，如果不是临时节点值为0
dataLength:节点数据长度
numChildren:子节点的数量
pzxid:子节点被修改的zxid
'''

#获取根节点的所有子节点，返回的是一个列表，只有子节点的名称
children = zk.get_children("/");
print children
#下面是根节点的返回值
#[u'rmstore', u'kazoo', u'yarn-leader-election', u'zookeeper']

#执行stop后所有的临时节点都将失效
zk.stop()
zk.close()
