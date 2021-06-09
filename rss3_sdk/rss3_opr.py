import sys
import json
import urllib3
import resource
import hexbytes
from . import until
from . import config
from . import file_stroge
from . import converter
from .type import rss_type
from eth_keys import keys

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
        self.__http = urllib3.PoolManager()

    def init(self) :
        if self.__option == None or self.__option.endpoint == None :
            return False
        if self.__option.private_key != None :
            pk = keys.PrivateKey(hexbytes.HexBytes(self.__option.private_key))
            self.__address = pk.public_key.to_checksum_address()
            self.getFile(self.__address)
            self.__option.fill_update_callback()
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

    # test
    def get_inner_stroge(self):
        return self.__file_stroge

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
                # test
                print(resp_dict)
                file_id = resp_dict['id']
                if file_id == None :
                    print("can not find irss3 id")
                    return
                # 校验拉取的文件
                irss3_content = self.__getRSS3Obj(file_id)

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

    def delPerson(self) :
        now_date = until.get_datetime_isostring()
        del_signature = until.sign()
        file_get_url = self.option + '/delete'
        del_fields = {
            "signature": del_signature,
            "date": now_date
        }
        # 这里要测一下需不需要转成json

        try:
            response = self.__http.request(method = 'POST',
                                           url = file_get_url,
                                           fields = del_fields)
            if response.status == 200:
                return True
            else :
                print("i am not know the status: %d" % response.status)
                return False
        except urllib3.exceptions.HTTPError as e:
            print("error reason :%s" % e)

    def updateFile(self) :
        now_date = until.get_datetime_isostring()
        del_signature = until.sign()
        file_get_url = self.option + '/put'
        content_files_dict = self.__file_stroge.getAllUpdateFiles()

        content_files_json_str = s

        update_fields = {

        }

        try:
            response = self.__http.request(method = 'POST',
                                           url = file_get_url,
                                           fields = update_fields)
            if response.status == 200:
                return True
            else:
                print("i am not know the status: %d" % response.status)
                return False
        except urllib3.exceptions.HTTPError as e:
            print("error reason :%s" % e)

    def __getRSS3Obj(self, file_id) :
        if file_id == None :
            return None
        if file_id.find('-items-') != -1 :
            return rss_type.IRSS3Items(id = file_id)
        elif file_id.find('-list-') != -1 :
            return rss_type.IRSS3List(id = file_id)
        else :
            return rss_type.IRSS3Index(id = file_id)