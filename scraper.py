import os
from requests import get

timeout = 5

proxies = {
              "http"  : os.environ.get('HTTP_PROXY'),
              "https" : os.environ.get('HTTPS_PROXY')
            }

awesome_stuff = [
        "run bsd",
        "power rangers",
        "python",
        "linux",
        "skateboards",
        "metal",
        "arduino",
        "raspberry pi"
        ]
for awesome_thing in awesome_stuff:
    sticker=None
    for dom in "info", "com", "co.uk":
       for prefix in "http", "https":
          url = "{prefix}://{awesome_thing}.{dom}/sticker/".format(
                  prefix=prefix,
                  awesome_thing=awesome_thing.replace(" ", ""),
                  dom=dom
                  )
          try:
             req = get(url, proxies=proxies, timeout=timeout, allow_redirects=False)
             if  200 <= req.status_code <=203 and 'this domain' not in req.text.lower():
                 sticker=True
                 print("{} is real. Run before its too late".format( url ))
             elif 'this domain' in req.text.lower():
                 print("{} is real. But theres probably no stickers there...".format(url))
          except:
             pass 
    if sticker == None :
        print("Sorry no {awesome} stickers".format(awesome=awesome_thing))

