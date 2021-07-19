import json
import urllib3

from . import (
    base
)

from rss3_sdk.until import (
    sign_handle,
    time,
    exceptions,
    rss3_obj_handle
)

class File(base.BaseModule):
    def __init__(self, option):
        super().__init__(self, option)

    def get(self, file_id):
        if file_id == None:
            raise ValueError("File_id is invalid parameter")

        rss3_obj = self._option.file_stroge.get_file(file_id)
        if rss3_obj != None :
            return rss3_obj

        file_get_url = "https://" + self._option.endpoint + '/' + file_id
        try:
            response = self._option.http.request(method = 'GET', url = file_get_url)
            if response.data != None:
                resp_dict = json.loads(response.data.decode())
                if response.status == 200 :
                    return self._get_file_success_handler(resp_dict)
                else:
                    if resp_dict['code'] == 5001:
                        self._get_file_not_exist(file_id)
                    else:
                        raise exceptions.HttpError("Execute wrong network code : %d" % response.status)
        except urllib3.exceptions.HTTPError as e:
            raise exceptions.HttpError("Connect Error : %s" % e)

    def update(self):
        file_get_url = "https://" + self._endpoint
        content_json_str = self._get_update_file_json()

        try:
            response = self._option.http.request(method='PUT',
                                          url=file_get_url,
                                          body=content_json_str,
                                          headers={"Content-Type": "application/json"})
            if response.status == 200:
                self._option.file_update_tag.clear()
            elif response.data != None:
                resp_dict = json.loads(response.data.decode())
                if resp_dict != None:
                    raise exceptions.HttpError(
                        "Rss3 error code %r, Rss3 error result %r" % (resp_dict['code'], resp_dict['message']))
                else:
                    raise exceptions.HttpError("Execute wrong network code: %d" % response.status)
            else:
                raise exceptions.HttpError("Execute wrong network code: %d" % response.status)
        except urllib3.exceptions.HTTPError as e:
            raise exceptions.HttpError("Connect Error : %s" % e)

    def _get_file_success_handler(self, resp_dict):
        file_id = resp_dict['id']
        if file_id == None:
            raise ValueError("Can't find file_id : %s" % file_id)

        # Verify the pulled file
        check = sign_handle.check(resp_dict,
                                  file_id.split('-')[0])
        if check == False:
            raise ValueError("The file_id %s signature does not match " % file_id)

        rss3_obj = rss3_obj_handle.get_rss3_obj(file_id, resp_dict)
        self._option.file_stroge.save_file(file_id, rss3_obj)

        return rss3_obj

    def _get_file_not_exist(self, file_id):
        new_person_file = time.get_rss3_obj(file_id)
        super()._update_file_stroge(new_person_file)

    def _get_update_file_json(self):
        contents = list()
        for file_name in self._option.file_update_tag:
            file = self._option.file_stroge.get_file(file_name)
            if file != None:
                try:
                    file_dict = rss3_obj_handle.get_rss3_json_dict(file, 2)
                except TypeError as e:
                    continue
                file_dict = rss3_obj_handle.remove_empty_properties(file_dict)
                file.signature = sign_handle.sign(file_dict, self._option.account.private_key)
                file_dict['signature'] = file.signature
                contents.append(file_dict)

        contents_dict = {
            "contents": contents
        }
        return json.dumps(contents_dict, ensure_ascii=False).encode("utf-8")


