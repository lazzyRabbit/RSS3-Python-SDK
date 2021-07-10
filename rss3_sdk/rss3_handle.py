import sys
import json
import urllib3
from . import until
from . import config
from . import converter
from . import exceptions
from .type import rss3_type
from .type import inn_type
from eth_utils import crypto

import logging
logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
logger = logging.getLogger(__name__)

class RSS3Handle :
    def __init__(self, endpoint, rss3_account, fill_update_callback = None) :
        self._endpoint = endpoint
        self._rss3_account = rss3_account
        self._fill_update_callback = fill_update_callback

        if 'proxy' in config.conf :
            logger.info(config.conf['proxy'])
            self._http = urllib3.ProxyManager(config.conf['proxy'])
        else :
            self._http = urllib3.PoolManager()

        self._file_stroge_dict = {}
        self._file_update_tag = set()

        if self._rss3_account == None or self._endpoint == None :
           raise ValueError("Rss3_account or endpoint is invalid parameter")


        if self._rss3_account.new_account_tag == False :
            self.get_file(self._rss3_account.address)
        else :
            now_date = until.get_datetime_isostring()
            irss3_index = rss3_type.IRSS3Index(id = self._rss3_account.address,
                                               date_created = now_date,
                                               date_updated = now_date)
            self._file_stroge_dict[self._rss3_account.address] = irss3_index
            self._file_update_tag.add(self._rss3_account.address)

    def profile_get(self):
        file = self._file_stroge_dict[self._rss3_account.address]
        if file == None:
            raise ValueError("can not find %s in stroge" % self._rss3_account.address)

        curr_profile = file.profile
        if curr_profile == None :
            return inn_type.IInnProfile()
        else :
            profile_dict = converter.IRSS3ProfileSchema().dump(curr_profile)
            profile_dict = until.remove_empty_properties(profile_dict)
            inn_profile = converter.IInnProfileSchema().load(profile_dict)

        return inn_profile

    def profile_patch(self, inn_profile) :
        if isinstance(inn_profile, inn_type.IInnProfile) == False and inn_profile != None :
            logger.info(type(inn_profile))
            raise ValueError("Inn_profile is invalid parameter")

        file = self._file_stroge_dict[self._rss3_account.address]
        if file == None :
            raise ValueError("can not find %s in stroge" % self._rss3_account.address)

        if file.profile == None :
            file.profile = rss3_type.IRSS3Profile()

        inn_profile_dict = converter.IInnProfileSchema().dump(inn_profile)
        logger.info(inn_profile_dict)
        inn_profile_dict = until.remove_empty_properties(inn_profile_dict)
        signature = until.sign(inn_profile_dict, self._rss3_account.private_key)
        inn_profile_dict['signature'] = signature
        logger.info("file.profile.signature:%s" % signature)
        logger.info(inn_profile_dict)
        file.profile = converter.IRSS3ProfileSchema().load(inn_profile_dict)
        file = self._update(file)

    def item_post(self, inn_item) :
        if isinstance(inn_item, inn_type.IInnItem) == False :
            raise ValueError("Inn_item is invalid parameter")

        now_date = until.get_datetime_isostring()
        irss3_index = self._file_stroge_dict[self._rss3_account.address]
        if irss3_index == None :
            raise

        new_item = rss3_type.IRSS3Item()
        new_item.__dict__.update(inn_item.__dict__)
        new_item.date_published = now_date
        new_item.date_modified = now_date
        new_item_dict = converter.IRSS3ItemSchema().dump(new_item)
        new_item_dict = until.remove_empty_properties(new_item_dict)
        new_item.signature = until.sign(new_item_dict, self._rss3_account.private_key)

        id_suffix = 0
        if len(irss3_index.items) != 0 :
            old_top_id_suffix_str = irss3_index.items[0].id.split('-',2)
            try :
                id_suffix = int(old_top_id_suffix_str) + 1
            except Exception as e :
                raise ValueError("Inn_item conversion failed : %s " % e)

        new_item_id = self._rss3_account.address + '-item-' + str(id_suffix)
        new_item.id = new_item_id

        if len(irss3_index.items) + 1 <= config.conf["itemPageSize"] :
            irss3_index.items.insert(0, new_item)
        else :
            new_items = []
            new_items.append(new_item)
            old_iterms_id_suffix = 0

            if irss3_index.items != None :
                try:
                    old_iterms_id_suffix = int(irss3_index.items[0].id.split('-',2))
                except Exception as e:
                     raise TypeError("iterms first id %s is error" % irss3_index.items[0].id)

            new_iterms_id = self._rss3_account.address + '-iterms-' + str(old_iterms_id_suffix + 1)
            irss3_iterms = rss3_type.IRSS3Items(id = new_iterms_id,
                                                a_version = 'rss3.io/version/v0.1.0',
                                                date_createds = now_date,
                                                signature = '',
                                                items = new_items,
                                                items_next = irss3_index.items_next)

            irss3_index.items = new_items
            irss3_index.items_next = new_item.id
            self._file_stroge_dict[new_item.id] = irss3_iterms
            self._file_update_tag.add(new_item.id)

        irss3_index.date_updated = now_date
        self._file_update_tag.add(self._rss3_account.address)

        return new_item

    def item_get(self, item_id) :
        if item_id == None :
            raise ValueError("File_id is invalid parameter")

        irss3 = self._file_stroge_dict[self._rss3_account.address]
        if irss3 == None and isinstance(irss3, rss3_type.IRSS3Index) and type(irss3) != rss3_type.IRSS3Items:
            return TypeError("Items_id %s find irss3 index is error" % self._rss3_account.address)

        try:
            index = irss3.items.index(item_id)
        except IndexError as e:
            raise IndexError("Irss3 index error: %s" % e)

        irss3_item_json = converter.IRSS3ItemSchema().dumps(irss3.items[index])
        inn_item = converter.IInnItemSchema.load(irss3_item_json)
        return inn_item

    def item_patch(self, inn_item) :
        if inn_item == None :
            raise ValueError("Inn_item and items_id is invalid parameter")

        irss3 = self._file_stroge_dict[self._rss3_account.address]
        if irss3 == None and isinstance(irss3, rss3_type.IRSS3Index) == False and isinstance(irss3, rss3_type.IRSS3Items) :
            return TypeError("Items_id %s find irss3 index is error" % self._rss3_account.address)

        try:
            index = irss3.items.index(inn_item.id)
        except IndexError as e:
            raise IndexError("Irss3 index error: %s" % e)

        irss3.items[index].__dict__.update(inn_item.__dict__)
        irss3.items[index].date_modified = until.get_datetime_isostring()
        self._file_update_tag.add(self._rss3_account.address)

        return irss3.items[index]

    def get_file(self, file_id) :
        if file_id == None:
            raise ValueError("File_id is invalid parameter")

        file_get_url = "https://" + self._endpoint + '/' + file_id
        logger.info(file_get_url)
        try:
            response = self._http.request(method = 'GET', url = file_get_url)
            if response.status == 200 :
                resp_dict = json.loads(response.data.decode())
                file_id = resp_dict['id']
                if file_id == None :
                    raise ValueError("Can't find file_id : %s" % file_id)

                # Verify the pulled file
                check = until.check(resp_dict,
                                    file_id.split('-')[0])
                if check == False :
                    raise ValueError("The file_id %s signature does not match " % file_id)

                # Store files locally
                irss3_index_schema = converter.IRSS3IndexSchema()
                irss3_index = irss3_index_schema.load(resp_dict)
                self._file_stroge_dict[self._rss3_account.address] = irss3_index

                return True
            elif response.status == 400 :
                now_date = until.get_datetime_isostring()
                new_rss3obj = until.get_rss3_obj(file_id)
                new_rss3obj.date_created = now_date
                new_rss3obj.date_updated = now_date
                new_rss3obj.signature = ''
                self._file_stroge_dict[self._rss3_account.address] = new_rss3obj
                self._file_update_tag.add(self._rss3_account.address)
            else :
                raise exceptions.HttpError("Execute wrong network code : %d" % response.status)
        except urllib3.exceptions.HTTPError as e:
            raise exceptions.HttpError("Connect Error : %s" % e)

    def update_file(self) :
        file_get_url = "https://" + self._endpoint
        contents = []

        for file_name in self._file_update_tag :
            file = self._file_stroge_dict.get(file_name)
            if file != None :
                try :
                    file_dict = until.get_rss3_json_dict(file, 2)
                    logger.info(file_dict)
                except TypeError as e :
                    continue
                file_dict = until.remove_empty_properties(file_dict)
                file.signature = until.sign(file_dict, self._rss3_account.private_key)
                file_dict['signature'] = file.signature
                contents.append(file_dict)

        contents_dict = {
            "contents" : contents
        }
        logger.info(contents_dict)
        content_json_str = json.dumps(contents_dict, ensure_ascii = False).encode("utf-8")
        logger.info(content_json_str)

        try:
            response = self._http.request(method = 'PUT',
                                          url = file_get_url,
                                          body = content_json_str,
                                          headers={"Content-Type": "application/json"})
            if response.status == 200:
                self._file_update_tag.clear()
            elif response.data != None :
                resp_dict = json.loads(response.data.decode())
                if resp_dict != None :
                    raise exceptions.HttpError("Rss3 error code %r, Rss3 error result %r" % (resp_dict['code'], resp_dict['message']))
                else :
                    raise exceptions.HttpError("Execute wrong network code: %d" % response.status)
            else :
                raise exceptions.HttpError("Execute wrong network code: %d" % response.status)
        except urllib3.exceptions.HTTPError as e:
            raise exceptions.HttpError("Connect Error : %s" % e)

    def _update(self, irss3_base) :
        if isinstance(irss3_base, rss3_type.IRSS3Base) == False :
            raise ValueError("irss3_base is invalid parameter")

        logger.info("irss3_base.date_updated: %s " % irss3_base.date_updated)
        irss3_base.date_updated = until.get_datetime_isostring()
        logger.info("irss3_base.date_updated: %s " % irss3_base.date_updated)
        self._file_stroge_dict[self._rss3_account.address]
        self._file_update_tag.add(self._rss3_account.address)
