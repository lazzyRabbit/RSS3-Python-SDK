import resource
import sys
import json
import urllib3
from . import until
from . import config
from . import file_stroge
from . import converter
from .type import rss_type


class RSS3Option() :
    def __init__(self, endpoint = None, private_key = None, fill_update_callback = None) :
        self.endpoint = endpoint
        self.private_key = private_key
        self.fill_update_callback = fill_update_callback
        
# 设定本地存储 
class RSS3Handle :
    def __init__(self, option = None) :
        self.__option = option
        self.__file_stroge = file_stroge.FileStroge()
        self.__address = None
        self.__http = None

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
        self.__http = urllib3.PoolManager()
        return True

    def profilePatch(self, profile) :
        file = self.__file_stroge.getFile(self.__address)
        file.profile = profile
        self.__file_stroge.patchFile(self.__address)
    
    def itemPost(self, inn_item) :
        now_date = until.get_datetime_isostring()
        irss3 = self.__file_stroge.getFile(self.__address)
        if irss3 == None :
            return None

        new_item = rss_type.IRSS3()
        new_item.set_patch_date(inn_item)
        new_item.date_published = now_date
        new_item.date_modified = now_date
        # 这里要做个转换，转换成sign可处理的dict
        # 
        #new_item.signature = sign()

        id_suffix = 0
        if len(irss3.item) != 0 :
            old_top_id_suffix_str = irss3.items[0].id.split('-',2)
            try :
                id_suffix = int(old_top_id_suffix_str) + 1
            except Exception as e :
                # log(id_suffix is error)
                return None
        new_item_id = self.__address + '-item-' + str(id_suffix)
        new_item.id = new_item_id

        if irss3.items.length() + 1 <= config.conf["itemPageSize"] :
            irss3.items.insert(0, new_item)
        else :
            new_list = []
            new_list.append(new_item)
            old_iterms_id_suffix = 0
            if  irss3.items != None :
                try:
                    old_iterms_id_suffix = int(irss3.items[0].id.split('-',2))
                except Exception as e:
                    # log(id_suffix is error)
                    return None
            new_iterms_id = self.__address + '-iterms-' + str(old_iterms_id_suffix + 1)
            irss3_iterms = rss_type.IRSS3Items(id = new_iterms_id,
                                               a_version = 'rss3.io/version/v0.1.0',
                                               date_createds = now_date,
                                               signature = '',
                                               items = new_list,
                                               items_next = irss3.items_next)

            irss3.items = new_list
            irss3.items_next = new_item.id
            self.__file_stroge.strogeFile(new_item.id, irss3_iterms)

        irss3.date_updated = now_date
        self.__file_stroge.patchFile(self.__address)

        return new_item

    def itemsPatch(self, inn_item, file_id) :
        if inn_item == None or file_id == None :
            return None

        irss3 = self.__file_stroge.getFile(file_id)
        if irss3 == None or type(irss3) != rss_type.IRSS3 or type(irss3) != rss_type.IRSS3Items:
            return None

        try:
            index = irss3.items.index(inn_item.id)
        except IndexError :
            return None

        irss3.set_patch_date(inn_item)
        irss3.date_modified = until.get_datetime_isostring()
        self.__file_stroge.patchFile(file_id)

        return irss3.items[index]

    def getFile(self, file_id) :
        if file_id == None :
            print("file id is none")
            return
        file_get_url = self.__option.endpoint + file_id
        print("file_get_url : %s" % file_get_url)
        try:
            response = self.__http.request(method = 'GET', url = file_get_url)
            if response.status == 200 :
                resp_dict = json.loads(response.data.decode())
                print(resp_dict)
                # 校验拉取的文件
                
                # 将文件存储在本地
                irss3_index_schema = converter.IRSS3IndexSchema()
                irss3_index = irss3_index_schema.load(resp_dict)
                print("dict : %r" % irss3_index.__dict__)
            elif response.status == 404 :
                now_date = until.get_datetime_isostring()
                new_rss3obj = self.__getRSS3Obj(file_id)
                new_rss3obj.date_created = now_date
                new_rss3obj.date_updated = now_date
                new_rss3obj.signature = ''
            else :
                print('error code: %d' % response.status)
        except urllib3.exceptions.HTTPError as e:
            print ("error reason :%s" % e)

    def delPerson(self, privateKey) :
        if file_id == None :
            return False
        l_file = self.fileStroge.getFile(file_id)
        if l_file == None :
            return False
        
        file_get_url = self.option + '/delete'


        try:
            response = urllib.request.urlopen(file_get_url, data=params, method='POST')
        except urllib.error.HTTPError as e:
            if e.code == 404 :
                pass
            else :
                pass

    def updateFile(self) :
        # 这里要加一些将内部类型转换成json的操作
        file_get_url = self.option + '/put'

        try:
            response = urllib.request.urlopen(file_get_url, data=params, method='POST')
        except urllib.error.HTTPError as e:
            if e.code == 404 :
                pass
            else :
                pass

    def __getRSS3Obj(self, file_id) :
        if file_id.find('-items-') != -1 :
            return type.rss_type.IRSS3Items(id = file_id)
        elif file_id.find('-list-') != -1 :
            return type.rss_type.IRSS3List(id = file_id)
        else :
            return type.rss_type.IRSS3(id = file_id)