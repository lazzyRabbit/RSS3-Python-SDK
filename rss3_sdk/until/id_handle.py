def prase_id(id) :
    split_list = id.split('-')
    address = split_list[0]
    type = split_list[1]
    index = None
    if len(split_list) >= 3 :
        index = int(split_list[2])
    return {'address':address,
            'type':type,
            'index':index}