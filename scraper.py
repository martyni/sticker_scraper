import os
from requests import get

proxies = {
              "http"  : os.environ.get('HTTP_PROXY'),
              "https" : os.environ.get('HTTPS_PROXY')
            }

awesome_stuff = [
        "power rangers",
        "python",
        "linux",
        "skateboards",
        "metal",
        "arduino",
        "raspberry pi"
        ]
for awesome_thing in awesome_stuff:
    url = "http://{}/sticker".format(awesome_thing.replace(" ", ""))
    if  200 <= get(url, proxies=proxies).status_code <=203:
        print("{} is real. Run before its too late".format( url ))
    else:
        print("Sorry no {awesome} stickers".format(awesome=awesome_thing))

