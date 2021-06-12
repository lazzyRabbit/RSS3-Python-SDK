import sys
import json
import urllib3
import resource
from . import until
from . import config
from . import converter
from .type import rss_type
from eth_utils import crypto

# 设定本地存储 
class RSS3Handle :
    def __init__(self, endpoint, rss3_account, fill_update_callback = None) :
        self._endpoint = endpoint
        self._rss3_account = rss3_account
        self._fill_update_callback = fill_update_callback
        self._http = urllib3.PoolManager()

        # 把缓存部分做到这里了
        self._file_stroge_dict = {}
        self._file_update_tag = {}

        if self._rss3_account == None or self.endpoint == None :
           raise ValueError("Rss3_account or endpoint is invalid parameter")

        if self._rss3_account.new_account_tag == False :
            self.get_file(self._rss3_account.address)
        else :
            now_date = until.get_datetime_isostring()
            irss3_index = rss_type.IRSS3Index(id = self._rss3_account.address,
                                              date_created = now_date,
                                              date_updated = now_date)
            self._file_stroge_dict[self._rss3_account.address] = irss3_index
            self._file_update_tag.add(self._rss3_account.address)

    def profile_patch(self, inn_profile) :
        if type(inn_profile) != rss_type.IRSS3Profile:
           raise ValueError("Inn_profile is invalid parameter")

        file = self._file_stroge_dict[self._rss3_account.address]
        file.profile.__dict__.update(inn_profile.__dict__)
        file.profile.signature = until.sign(file.profile.__dict__, self._rss3_account.private_key)
        self._file_update_tag.add(self._rss3_account.address)

    def item_post(self, inn_item) :
        if type(inn_item) != rss_type.IRSS3Item :
            raise ValueError("Inn_item is invalid parameter")

        now_date = until.get_datetime_isostring()
        irss3_index = self._file_stroge_dict[self._rss3_account.address]
        if irss3_index == None :
            raise

        new_item = rss_type.IRSS3Item()
        new_item.__dict__.update(inn_item.__dict__)
        new_item.date_published = now_date
        new_item.date_modified = now_date
        new_item.signature = until.sign(new_item.__dict__, self._rss3_account.private_key)

        id_suffix = 0
        if len(irss3_index.item) != 0 :
            old_top_id_suffix_str = irss3_index.items[0].id.split('-',2)
            try :
                id_suffix = int(old_top_id_suffix_str) + 1
            except Exception as e :
                raise ValueError("Inn_item conversion failed : %s " % e)

        new_item_id = self._rss3_account.address + '-item-' + str(id_suffix)
        new_item.id = new_item_id

        if irss3_index.items.length() + 1 <= config.conf["itemPageSize"] :
            irss3_index.items.insert(0, new_item)
        else :
            new_item_list = []
            new_item_list.append(new_item)
            old_iterms_id_suffix = 0
            if  irss3_index.items != None :
                try:
                    old_iterms_id_suffix = int(irss3_index.items[0].id.split('-',2))
                except Exception as e:
                    # log(id_suffix is error)
                    return None
            new_iterms_id = self._rss3_account.address + '-iterms-' + str(old_iterms_id_suffix + 1)
            irss3_iterms = rss_type.IRSS3Items(id = new_iterms_id,
                                               a_version = 'rss3.io/version/v0.1.0',
                                               date_createds = now_date,
                                               signature = '',
                                               items = new_item_list,
                                               items_next = irss3_index.items_next)

            irss3_index.items = new_item_list
            irss3_index.items_next = new_item.id
            self._file_stroge_dict[new_item.id] = irss3_iterms
            self._file_update_tag.add(new_item.id)

        irss3_index.date_updated = now_date
        self._file_update_tag.add(self._rss3_account.address)

        return new_item

    def items_patch(self, inn_item, file_id) :
        if inn_item == None or file_id == None :
            raise ValueError("Inn_item and file_id is invalid parameter")

        irss3 = self._file_stroge_dict[file_id]
        if irss3 == None or type(irss3) != rss_type.IRSS3Index or type(irss3) != rss_type.IRSS3Items :
            return None

        try:
            index = irss3.items.index(inn_item.id)
        except IndexError :
            return None

        irss3.__dict__.update(inn_item.__dict__)
        irss3.date_modified = until.get_datetime_isostring()
        self._file_update_tag(file_id)

        return irss3.items[index]

    def get_file(self, file_id) :
        if file_id == None:
            raise ValueError("File_id is invalid parameter")

        file_get_url = self.endpoint + file_id
        print("file_get_url : %s" % file_get_url)
        try:
            response = self._http.request(method = 'GET', url = file_get_url)
            if response.status == 200 :
                resp_dict = json.loads(response.data.decode())
                # test
                print(resp_dict)
                file_id = resp_dict['id']
                if file_id == None :
                    raise ValueError("Can't find file_id : %s" % file_id)
                # 校验拉取的文件
                irss3_content = until.get_rss3_obj(file_id)
                check = until.check(irss3_content.__dict__,
                                    file_id.split('-', 0))
                if check == True :
                    self._file_stroge_dict[file_id] = irss3_content
                    print(file_id)
                    return True
                else :
                    
                    print("is error")

                # 将文件存储在本地
                irss3_index_schema = converter.IRSS3IndexSchema()
                irss3_index = irss3_index_schema.load(resp_dict)
                self._file_stroge_dict[self._rss3_account.addresss] = irss3_index
                print("dict : %r" % irss3_index.__dict__)
                return True
            elif response.status == 404 :
                now_date = until.get_datetime_isostring()
                new_rss3obj = until.get_rss3_obj(file_id)
                new_rss3obj.date_created = now_date
                new_rss3obj.date_updated = now_date
                new_rss3obj.signature = ''
                return False
            else :
                print('error code: %d' % response.status)
                return False
        except urllib3.exceptions.HTTPError as e:
            print ("error reason :%s" % e)

    def del_person(self) :
        now_date = until.get_datetime_isostring()
        del_test = "Delete my RSS3 persona at" + str(now_date)
        del_signature = until.sign(self._rss3_account.private_key,
                                   crypto.keccak(text = del_test))
        file_get_url = self._endpoint + '/delete'
        del_fields = {
            "signature": del_signature,
            "date": now_date
        }
        # 这里要测一下需不需要转成json

        try:
            response = self._http.request(method = 'POST',
                                           url = file_get_url,
                                           fields = del_fields)
            if response.status == 200:
                return True
            else :
                print("i am not know the status: %d" % response.status)
                return False
        except urllib3.exceptions.HTTPError as e:
            raise TypeError("Connect Error : %s" % e)

    def update_file(self) :
        file_get_url = self.option + '/put'
        contents = []

        for file_name in self._file_update_tag :
            file = self._file_stroge_dict.get(file_name)
            if file != None :
                file.signature = until.sign(file, self._rss3_account.private_key)
                contents.append(file.__dict__)
                
        content_json_str = json.dumps(contents)
        # 这里要测试一下能否正常使用

        try:
            response = self._http.request(method = 'POST',
                                           url = file_get_url,
                                           fields = content_json_str)
            if response.status == 200:
                self._file_update_tag.clear()
                return True
            else:
                print("i am not know the status: %d" % response.status)
                return False
        except urllib3.exceptions.HTTPError as e:
            print("error reason :%s" % e)
