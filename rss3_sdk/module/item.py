import math

from . import (
    base
)

from rss3_sdk import (
    config
)

from rss3_sdk.until import (
    data_handle,
    sign_handle,
    time,
    id_handle
)

from rss3_sdk.type import (
    inn_type,
    rss3_type,
    converter
)

class Item(base.BaseModule):
    def __init__(self, option):
        base.BaseModule.__init__(self, option)

    def get(self, file_id):
        if file_id == None:
            raise ValueError("File_id is invalid parameter")

        item = None
        position = self._get_position(file_id)
        if position != None:
            item = position['file'].items[position['index']]
            if item != None:
                item_dict = converter.IRSS3ItemSchema().dump(item)
                item_dict = data_handle.remove_empty_properties(item_dict)
                item = converter.IInnItemSchema().load(item_dict)

        return item

    def patch(self, inn_data):
        if inn_data == None or \
            isinstance(inn_data, inn_type.IInnItem) == False or \
            len(inn_data.id) == 0:
            raise ValueError("Inn_item and items_id is invalid parameter")

        personl_file = self._option.stroge.get_file(self._option.account.address)
        if personl_file == None and isinstance(personl_file, rss3_type.IRSS3Index) == False and \
            isinstance(personl_file, rss3_type.IRSS3Items) :
            raise TypeError("Items_id %s find irss3 index is error" % self._option.account.address)

        now_date = time.get_datetime_isostring()
        position = self._get_position(inn_data.id)
        if position != None:
            inn_item_dict = converter.IInnItemSchema().dump(inn_data)
            inn_item_dict['date_modified'] = now_date
            inn_item_dict = data_handle.remove_empty_properties(inn_item_dict)
            signature = sign_handle.sign(inn_item_dict, self._option.account.private_key)
            inn_item_dict['signature'] = signature
            rss3_item = converter.IRSS3ItemSchema().load(inn_item_dict)
            position['file'].items[position['index']] = rss3_item
            super()._update_file_stroge(personl_file)

        return position['file'].items[position['index']]

    def post(self, inn_data):
        if isinstance(inn_data, inn_type.IInnItem) == False:
            raise ValueError("Inn_item is invalid parameter")

        now_date = time.get_datetime_isostring()
        personl_file = self._option.stroge.get_file(self._option.account.address)
        if personl_file == None:
            raise

        inn_item_dict = converter.IInnItemSchema().dump(inn_data)
        inn_item_dict['date_published'] = now_date
        inn_item_dict['date_modified'] = now_date

        id_suffix = 0
        if len(personl_file.items) != 0:
            prase_ele = id_handle.prase_id(personl_file.items[0].id)
            old_index = prase_ele['index']
            try:
                id_suffix = old_index + 1
            except Exception as e:
                raise ValueError("Inn_item conversion failed : %s " % e)

        new_item_id = self._option.account.address + '-item-' + str(id_suffix)
        inn_item_dict['id'] = new_item_id

        inn_item_dict = data_handle.remove_empty_properties(inn_item_dict)
        signature = sign_handle.sign(inn_item_dict, self._option.account.private_key)
        inn_item_dict['signature'] = signature

        new_item = converter.IRSS3ItemSchema().load(inn_item_dict)

        if len(personl_file.items) + 1 <= config.conf["itemPageSize"]:
            personl_file.items.insert(0, new_item)
        else:
            new_items_list = list()
            new_items_list.append(new_item)
            old_items_id_suffix = 0 if personl_file.items_next == None else id_handle.prase_id(personl_file.items_next)[
                                                                                'index'] + 1

            new_items_id = self._option.account.address + '-items-' + str(old_items_id_suffix)
            new_items = rss3_type.IRSS3Items(id=new_items_id,
                                             a_version='rss3.io/version/v0.1.0',
                                             date_created=now_date,
                                             signature='',
                                             items=new_items_list,
                                             items_next=personl_file.items_next)

            personl_file.items = new_items_list
            personl_file.items_next = new_items_id
            super()._update_file_stroge(new_items)

        super()._update_file_stroge(personl_file)
        self._option.file_update_tag.add(self._option.account.address)

        return new_item

    def _get_position(self, item_id):
        prase_ele = id_handle.prase_id(item_id)
        if prase_ele['address'] != self._option.account.address:
            raise ValueError("File_id is invalid parameter, address %s is error." % prase_ele['address'])

        personl_file = self._file_stroge_dict[self._option.account.address]
        if personl_file == None and isinstance(personl_file, rss3_type.IRSS3Index) and type(
                personl_file) != rss3_type.IRSS3Items:
            raise TypeError("Address [%s] find irss3 index is error" % self._option.account.address)

        items_file = self.get_file(self._option.account.address)
        item_filter_id_list = [item.id for item in personl_file.items]
        index = item_filter_id_list.index(item_id)

        if item_id not in item_filter_id_list:
            items_file_id = self._option.account.address + '-items-' + str(
                math.ceil(prase_ele['index'] / config.conf['itemPageSize']))
            items_file = self.get_file(items_file_id)
            if items_file != None:
                item_filter_id_list = [item.id for item in personl_file.items]
                index = item_filter_id_list.index(item_id)
            else:
                return None

        return {
            'file': items_file,
            'index': index
        }