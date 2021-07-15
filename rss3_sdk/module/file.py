import json
import urllib3

from . import (
    base
)

from rss3_sdk.type import (
    inn_type,
    rss3_type
)

from rss3_sdk.until2 import (
    sign,
    time,
    exceptions,
    data_handle,
    rss3_obj_handle
)

class File(base.BaseModule):
    def __init__(self, option):
        base.BaseModule.__init__(self, option)
        self._file_stroge_dict = {}
        self._file_update_tag = set()
        pass

    def get(self, file_id):
        if file_id == None:
            raise ValueError("File_id is invalid parameter")

        if self._file_stroge_dict.get(file_id) != None :
            return self._file_stroge_dict[file_id]

        file_get_url = "https://" + self._endpoint + '/' + file_id
        try:
            response = self._http.request(method = 'GET', url = file_get_url)
            if response.status == 200 :
                resp_dict = json.loads(response.data.decode())
                file_id = resp_dict['id']
                if file_id == None :
                    raise ValueError("Can't find file_id : %s" % file_id)

                # Verify the pulled file
                check = sign.check(resp_dict,
                                     file_id.split('-')[0])
                if check == False :
                    raise ValueError("The file_id %s signature does not match " % file_id)

                rss3_obj = rss3_obj_handle.get_rss3_obj(file_id, resp_dict)
                self._file_stroge_dict[file_id] = rss3_obj

                return rss3_obj

            # 这里要再检验一下
            elif response.status == 400 :
                now_date = time.get_datetime_isostring()
                new_rss3obj = rss3_obj_handle.get_rss3_obj(file_id)
                new_rss3obj.date_created = now_date
                new_rss3obj.date_updated = now_date
                new_rss3obj.signature = ''
                self._file_stroge_dict[self._rss3_account.address] = new_rss3obj
                self._file_update_tag.add(self._rss3_account.address)
            else :
                raise exceptions.HttpError("Execute wrong network code : %d" % response.status)
        except urllib3.exceptions.HTTPError as e:
            raise exceptions.HttpError("Connect Error : %s" % e)


    def update(self):

        pass

    # Most patches are used more
    def update_obj(self, rss3_base):
        if isinstance(rss3_base, rss3_type.IRSS3Base) == False:
            raise ("Rss3_base type is error")

        rss3_base.date_updated = time.get_datetime_isostring()
        self._file_stroge_dict[rss3_base.id] = rss3_base
        self._file_update_tag.add(self._rss3_account.address)


