import sys
from rss3_sdk import rss3_opr

def fill_update_new_callback() :
    print("this is call back")

if __name__ == '__main__':
    # item = rss_type.IRSS3Item()
    # item.title = "sada"
    # print(item.title)

    # index.test_main.test()

    # test for interface

        potion = rss3_opr.RSS3Option(endpoint = 'https://rss3-hub-playground-6raed.ondigitalocean.app/',
                                     private_key = '0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba',
                                     fill_update_callback = fill_update_new_callback)

        rss3_handle = rss3_opr.RSS3Handle(potion)
        file_id = '0x6338ee94fB85e157D117d681E808a34a9aC21f31'
        if rss3_handle.init() == False :
            print("you are SB")
            exit(-1)
        rss3_handle.getFile(file_id)


    # print (test_dict)