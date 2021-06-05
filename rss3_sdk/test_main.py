import sys
from rss3_sdk import rss3_opr
from . import converter
sys.path.append('.')

test_dict = {
    "id": "0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944",
    "@version": "rss3.io/version/v0.1.0-rc.0",
    "date_created": "2009-05-01T00:00:00.000Z",
    "date_updated": "2021-05-08T16:56:35.529Z",

    "profile": {
        "name": "DIYgod",
        "avatar": ["dweb://diygod.jpg", "https://example.com/diygod.jpg"],
        "bio": "写代码是热爱，写到世界充满爱！",
        "tags": ["demo", "lovely", "technology"]
    },

    "items": [{
        "id": "0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944-item-1",
        "authors": ["0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944"],
        "summary": "Yes!!",
        "date_published": "2021-05-09T16:56:35.529Z",
        "date_modified": "2021-05-09T16:56:35.529Z",

        "type": "comment",
        "upstream": "0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944-item-0"
    }, {
        "id": "0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944-item-0",
        "authors": ["0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944"],
        "title": "Hello World",
        "summary": "Hello, this is the first item of RSS3.",
        "date_published": "2021-05-08T16:56:35.529Z",
        "date_modified": "2021-05-08T16:56:35.529Z",

        "contents": [{
            "file": ["dweb://never.html", "https://example.com/never.html"],
            "mime_type": "text/html"
        }, {
            "file": ["dweb://never.jpg"],
            "mime_type": "image/jpeg"
        }],

        "@contexts": [{
            "type": "comment",
            "list": ["0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944-item-1"]
        }, {
            "type": "like",
            "list": ["0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
        }]
    }],
    "items_next": "0xC8b960D09C0078c18Dcbe7eB9AB9d816BcCa8944-items-0",

    "links": [{
        "type": "follow",
        "list": ["0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
    }, {
        "type": "superfollow",
        "list": ["0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
    }],
    "@backlinks": [{
        "type": "follow",
        "list": ["0xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"]
    }],

    "assets": [{
        "type": "some experience point",
        "content": "100"
    }]
}

def fill_update_new_callback() :
    print("this is call back")

if __name__ == '__main__':
    # item = rss_type.IRSS3Item()
    # item.title = "sada"
    # print(item.title)

    # index.test_main.test()

    # test for interface
    '''
        potion = rss3_opr.RSS3Option(endpoint = 'https://rss3-hub-playground-6raed.ondigitalocean.app/',
                                     private_key = '0x47e18d6c386898b424025cd9db446f779ef24ad33a26c499c87bb3d9372540ba',
                                     fill_update_callback = fill_update_new_callback)
    
        rss3_handle = rss3_opr.RSS3Handle(potion)
        file_id = '0x6338ee94fB85e157D117d681E808a34a9aC21f31'
        if rss3_handle.init() == False :
            print("you are SB")
            exit(-1)
        rss3_handle.getFile(file_id)
    '''

    print (test_dict)