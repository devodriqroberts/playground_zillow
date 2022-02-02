#%%
import json
from urllib.parse import urlparse, parse_qs, urlencode
 

URL = 'https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState={"pagination":{"currentPage":1},"usersSearchTerm":"Atlanta,%20GA","mapBounds":{"west":-84.73523648339844,"east":-84.22574551660156,"south":33.671398471115744,"north":33.876873347414715},"regionSelection":[{"regionId":37211,"regionType":6}],"isMapVisible":true,"filterState":{"sortSelection":{"value":"globalrelevanceex"},"isAllHomes":{"value":true},"isCondo":{"value":false},"isMultiFamily":{"value":false},"isManufactured":{"value":false},"isLotLand":{"value":false},"isTownhouse":{"value":false},"isApartment":{"value":false},"isApartmentOrCondo":{"value":false}},"isListVisible":true,"mapZoom":11}&wants={"cat1":["listResults","mapResults"],"cat2":["total"]}&requestId=4'
COOKIE = '_px3=001b4c8eeedafb074cf54558d5fd2d14cf3d56628e03d7c049a867cd87369d4d:iZw07tfH0ew/4pxEbZHtzcjEIl4oU/NdM1RxPXKq9MK/y2irmQK0oEHkSYmyDbb5ZDpk/kWkMX8/U0IGhUo2Pw==:1000:N0Ohz4FvpJZTRQUaQwfbXFm7d15+ToXxaprBsIZ5kfX67/bedaBI+YnqLWQsHVoIqKEyAW2im+1RuOOY2ZZCnm/4Dn+BdsE497HRFU6Ut+13Q3qv2dmPuBlxCev4QBeALaOrPfqf8E4kTlIxtMOKGY4KTHCLLO5a+Tkb1RbLFGIbi3LfUXvPG9OIu8tPqJPC5tq8fKXIwiRMhJ/o/7UxVQ==; search=6|1645293330625%7Crect%3D33.876873347414715%252C-84.22574551660156%252C33.671398471115744%252C-84.73523648339844%26rid%3D37211%26disp%3Dmap%26mdm%3Dauto%26p%3D3%26z%3D1%26type%3Dhouse%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0937211%09%09%09%09%09%09; AWSALB=9NTWuu7S70/W8vlw9TbQSDueQOVUZ/vO7V6V2Pv77lIsJtL9rxe5srEoJcUy4w2m7dyQZPmcc1bpkRM6QjB7b9Yn5uugZluDD8gDwW8Nc+jgOqrcp6PgnSO2XdL+; AWSALBCORS=9NTWuu7S70/W8vlw9TbQSDueQOVUZ/vO7V6V2Pv77lIsJtL9rxe5srEoJcUy4w2m7dyQZPmcc1bpkRM6QjB7b9Yn5uugZluDD8gDwW8Nc+jgOqrcp6PgnSO2XdL+; zjs_anonymous_id=%223e05f1ea-f776-4bdd-8bdd-4c2ca2012870%22; zjs_user_id=null; JSESSIONID=B9FF820554C15AF238F748C0CA8EB737; _pxvid=dc35b9bf-7a0c-11ec-bed5-61724b55715a; zgsession=1|0c9d9e37-fe69-44ca-9538-057c271f3564; zguid=23|%243e05f1ea-f776-4bdd-8bdd-4c2ca2012870'

def parse_cookies():
    cookie_parts = COOKIE.split()
    cookie_dict = {}
    for cookie in cookie_parts:
        index = cookie.index("=")
        cookie_name = cookie[:index]
        cookie_value = cookie[index+1:].rstrip(";")
        cookie_dict[cookie_name] = cookie_value
    return cookie_dict


def parse_new_url(url, page_number):
    url_parser = urlparse(url)
    query_string = parse_qs(url_parser.query)
    search_query_state = json.loads( query_string.get("searchQueryState")[0] )
    search_query_state["pagination"] = {"currentPage":page_number}
    query_string.get("searchQueryState")[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq=1)
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url
# %%
