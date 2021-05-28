import sys
from types import rss_type
from stroge import *

# 设定本地存储 
class RSS3 :
    def __init_(self) :
        pass

    def profilePatch(profile) :
        # 从本地存储中找到合适的profile并修改
        pass
    
    def itemPost() :
        # 增加新的文件并存储到本地
        pass

    def itemsPatch() :
        # 修改文件并存储到本地
        pass

    def getFile() :
        # curl ${this.endpoint}/files/${fileID}
        # 校验拉取的文件
        # 将文件存储在本地
        # 如果错误返回404
        pass

    def delFile() :
        # curl ${this.endpoint}/del
        pass

    def sign() :
        # 实际上是他妈的EthCrypto.sign一个封装
        pass