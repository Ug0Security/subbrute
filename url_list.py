

my_list = """
http://www.sermepa.es
http://www.piratebay.red
http://www.offers.com
http://www.esmplus.com
http://www.twister.porn
http://www.hewitt.com
http://www.codeforces.com
http://www.tubidy.mobi
http://www.google.com.mt
http://www.theih1w.top
http://www.vanillagaming.org
"""

url_list = my_list.split('\n')[1:-1]
url_list = set(url_list)                    # eleminate ducplicate in case of
url_ltuple = list()

i = 0
for url in url_list:
    url_ltuple.append((i, url))
    i += 1
