import json
import copy

def value_is_not_empty(value) :
    return value not in ['', None, {}, []]

def remove_not_sign_properties(data) :
    if data == None :
        return None

    temp_data = dict()
    for key, value in data.items():
        if (key.find('@') == -1) and key != 'signature' :
            temp_data[key] = value
    return temp_data

def remove_empty_properties(data) :
    if isinstance(data, dict):
        temp_data = dict()
        for key, value in data.items():
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value) :
                    temp_data[key] = new_value
        return None if not temp_data else temp_data

    elif isinstance(data, list):
        temp_data = list()
        for value in data:
            if value_is_not_empty(value):
                new_value = remove_empty_properties(value)
                if value_is_not_empty(new_value) :
                    temp_data.append(new_value)
        return None if not temp_data else temp_data

    elif value_is_not_empty(data):
        return data

def sorted_irss_dict(data) :
    if isinstance(data, dict) :
        temp_data = dict()
        for key, value in data.items() :
            new_value = sorted_irss_dict(value)
            temp_data[key] = new_value
        return sorted(temp_data.items(), key=lambda d: d[0])

    elif isinstance(data, list) :
        temp_data = list()
        count = 0
        for value in data:
            new_value = sorted_irss_dict(value)
            temp_data.append([str(count), new_value])
            count = count + 1

        return None if not temp_data else temp_data

    elif value_is_not_empty(data) :
        return data

def irss3_data_dump_handle(irss3_data) :
    not_sign_irss3_data = copy.deepcopy(irss3_data)
    not_sign_irss3_data = remove_not_sign_properties(not_sign_irss3_data)
    not_sign_irss3_data = sorted_irss_dict(not_sign_irss3_data)

    return json.dumps(not_sign_irss3_data, separators=(',',':'), ensure_ascii = False)