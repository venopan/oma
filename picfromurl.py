import urllib.request
from viter import viter

opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

ids = viter()
for i in range(len(ids)):
    print(str(i+1)+":", ids[i])

    url = "http://html.doku.pub/01/2019/07/11/mqej718kgyl5/bg" + ids[i] + ".jpg"
    local= "BuchA2/pg" + str(i+1) + ".jpg"
    urllib.request.urlretrieve(url,local)