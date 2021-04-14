import certifi
import urllib3
import re
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second

while True:
    # try:
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        # Sort by price
        r = http.request('GET', 'https://www.ebay.com/sch/i.html?_fsrp=1&LH_PrefLoc=3&_sop=15&_sacat=0&_nkw=rtx+2080+ti&LH_ItemCondition=1000%7C1500%7C2500%7C3000&LH_BIN=1&_from=R40&rt=nc')

        # print(r.data)
        html_content = r.data.decode('utf-8')
        # print(html_content)
        # <span class=s-item__price>\$\d\d\d.\d\d</span>
        x = re.findall("<span class=s-item__price>\$\d\d\d.\d\d</span>", html_content)
        x_strip = []
        # print(x)
        for string in x:
            x_strip.append(int(string[27:30]))
        x_strip.sort()
        # print(x_strip)
        if x_strip == []:
            print("No matches found!")

        # Remove outliers
        try:
            x_strip.remove(400)
            print("Exception numbers removed")
            print(time.time())
        except:
            pass
        # print(x_strip)

        if  500 < x_strip[0] < 700:
            winsound.Beep(frequency, x_strip[0])
            print(time.time())
            print(x_strip)

    # except:
    #     print("Try has failed!")
    #     pass
    # # break
