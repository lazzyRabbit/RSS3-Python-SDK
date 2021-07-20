from rss3_sdk.module.rss3 import base

from rss3_sdk.type import (
    inn_type,
    rss3_type,
    converter
)

from rss3_sdk.until import (
    data_handle,
    sign_handle
)

class Profile(base.BaseModule):
    def __init__(self, option):
        base.BaseModule.__init__(self, option)
        pass

    def get(self):
        personl_file = self._option.stroge.get_file(self._option.account.address)
        if personl_file == None:
            raise ValueError("can not find %s in stroge" % self._option.account.address)

        curr_profile = personl_file.profile
        if curr_profile == None:
            return inn_type.IInnProfile()
        else:
            profile_dict = converter.IRSS3ProfileSchema().dump(curr_profile)
            profile_dict = data_handle.remove_empty_properties(profile_dict)
            inn_profile = converter.IInnProfileSchema().load(profile_dict)

        return inn_profile

    def patch(self, inn_data):
        if isinstance(inn_data, inn_type.IInnProfile) == False and inn_data != None:
            raise ValueError("Inn_profile is invalid parameter")

        personl_file = self._option.stroge.get_file(self._option.account.address)
        if personl_file == None:
            raise ValueError("can not find %s in stroge" % self._option.account.address)

        if personl_file.profile == None:
            personl_file.profile = rss3_type.IRSS3Profile()

        inn_profile_dict = converter.IInnProfileSchema().dump(inn_data)
        inn_profile_dict = data_handle.remove_empty_properties(inn_profile_dict)
        signature = sign_handle.sign(inn_profile_dict, self._option.account.private_key)
        inn_profile_dict['signature'] = signature
        personl_file.profile = converter.IRSS3ProfileSchema().load(inn_profile_dict)
        super()._update_file_stroge(personl_file)