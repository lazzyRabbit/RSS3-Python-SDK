import sys
import json
import until
import config
import file_stroge
import urllib.request
from type import rss_type, inn_type

class RSS3Option() :
    def __init__(self, endpoint = None, private_key = None, fill_update_callback = None) :
        self.endpoint = endpoint
        self.private_key = private_key
        self.fill_update_callback = fill_update_callback
        
# 设定本地存储 
class RSS3 :
    def __init__(self, option = None) :
        self.__option = option
        self.__file_stroge = file_stroge.FileStroge()
        self.__address = None

    def init(self) :
        if self.__option == None or self.__option.endpoint == None :
            return False
        if self.__option.private_key != None :
            # self.__address = EthCrypto.publicKeyByPrivateKey
            # irss3 = IRSS3(id = self.__address)
            # self.getFile(self.__address)
            # fill_update_callback()
            pass
        else :
            # keys = EthCrypto.createIdentity();
            # self.__option.private_key = keys.privateKey
            # self.__address = key.address
            # now_date = date.string()
            # irss3 = IRSS3(id = self.__address, date_created = now_date, date_updated = now_date)
            # self.__file_stroge.updateFile(self.__address)
            # fill_update_callback()
            pass
        return True

    def profilePatch(self, profile) :
        file = self.__file_stroge.getFile(self.__address)
        file.profile = profile
        self.__file_stroge.patchFile(self.__address)
    
    def itemPost(self, inn_item) :
        date = until.get_datetime_isostring()
        irss3 = self.__file_stroge.getFile(self.__address)
        if irss3 == None :
            return False
        
        # 增加新的文件并存储到本地
        old_top_list_id = irss3.

        new_item_id = self.__address + '-item-' + 
        new_item = rss_type.IRSS3Item(id = new_item_id, authors = self.__address, date_published = date, date_modified = date)
        # item.signature = this.sign(item)



        irss3.date_updated = date
        self.__file_stroge.patchFile(self.__address)
        pass

    def itemsPatch(self, inn_item, file_id) :

        # 修改文件并存储到本地
        pass

    def getFile(self, file_id) :
        if file_id == None :
            return False
        fileGetUrl = self.option + '/files/' + file_id
        try:
            response = urllib.request.urlopen(fileGetUrlm, method='GET')
            # 校验拉取的文件
            # 将文件存储在本地
        except urllib.error.HTTPError as e:
            # 如果错误返回404
            if e.code == 404 :
                pass

    def delFile(self, file_id) :
        if file_id == None :
            return False
        l_file = self.fileStroge.getFile(file_id)
        if l_file == None :
            return False
        
        fileGetUrl = self.option + '/delete'
        signature = l_file.signature
        del_content[signature] = signature
        params = json.dump(del_content)

        try:
            response = urllib.request.urlopen(fileGetUrl, data=params, method='POST')
        except urllib.error.HTTPError as e:
            if e.code == 404 :
                pass
        
        pass
    
    def updateFile(self) :
        # 这里要加一些将内部类型转换成json的操作
        fileGetUrl = self.option + '/update'

        try:
            response = urllib.request.urlopen(fileGetUrl, data=params, method='POST')
        except urllib.error.HTTPError as e:
            if e.code == 404 :
                pass
        pass

    def sign(self, dict) :
        # message = json.dump(until.remove_not_sign_properties(dict))
        # EthCrypto.sign(privatekey, EthCrypto.hash.keccak256(message))
        pass