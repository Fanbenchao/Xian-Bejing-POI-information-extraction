from urllib import request
from urllib.request import urlopen
import json
def urls(itemy, loc):
    #baidu_api = "你的秘钥"
    urls=[]
    for page in range(0,20):
        url = "http://api.map.baidu.com/place/v2/search?query=" + request.quote(itemy) + "&bounds=" + loc 
        url = url + "&page_size=20&page_num=" + str(page) + "&output=json&ak=YourKey"
        urls.append(url)

    return urls

def baidu_search(urls,loc_origin,sic):
    try:
        json_sel = []   
        for url in urls:
            req = request.Request(url)
            json_obj = urlopen(req)
            data = json.load(json_obj)

            for item in data['results']:
                ids = item["uid"]
                name = item["name"]
                lat = item["location"]["lat"]
                lng = item["location"]["lng"]
                if 'address' in item:
                    address = item['address']
                else:
                    address = ''
                if 'province' in item:
                    province = item['province']
                else:
                    province = ''    
                if 'city' in item:
                    city = item['city']
                else:
                    city = ''
                if "street_id" in item:
                    street_id = item["street_id"]
                else:
                    street_id = ''
                if "telephone" in item:
                    tel = item["telephone"].replace(',',' ')
                else:
                    tel = ''
                js_sel = [ids,name,address,city,province,"CN",tel,str(loc_origin[0]),str(loc_origin[1]),str(lat),str(lng)]
                json_sel.append(js_sel)
    except:
        pass

    return json_sel
