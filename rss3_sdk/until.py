from datetime import datetime

def get_datetime_isostring() :
    try:
        utc = dt + dt.utcoffset()
    except TypeError as e:
        utc = dt
    isostring = datetime.strftime(utc, '%Y-%m-%dT%H:%M:%S.{0}Z')
    return isostring.format(int(round(utc.microsecond/1000.0)))

def remove_not_sign_properties(data) :
    # new_data = data() # 深拷贝一组
    # for key in data : 
    #     if key.first[0] == '@' or key == 'signature' :
    #         del key
    # return new_data
    pass


