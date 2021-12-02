import re
import json
import time
import random
import base64
from . import Cache, request


global cache
cache = Cache()


def get_x_linkvertise_ut():
    response = request("https://publisher.linkvertise.com/api/v1/account")
    data = json.loads(response)
    return data["user_token"] if "user_token" in data.keys() else None


def leakvertise_non_dynamic(url: str) -> str:
    object_path = re.search(r"\/\d+\/[^\/]+", url)
    if object_path is None:
        return None

    for path in ("/captcha", "/countdown_impression?trafficOrigin=network", "/todo_impression?mobile=true&trafficOrigin=network"):
        url = f"https://publisher.linkvertise.com/api/v1/redirect/link{object_path[0]}{path}"
        response = request(url)
        data = json.loads(response)
        if data["success"]: break

    response = request(f"https://publisher.linkvertise.com/api/v1/redirect/link/static{object_path[0]}")
    data = json.loads(response)
    options = dict(serial=base64.b64encode(json.dumps(dict(timestamp=int(str(time.time_ns())[0:13]), random="6548307", link_id=data["data"]["link"]["id"])).encode()).decode())
    token = get_x_linkvertise_ut()
    response = request(f"https://publisher.linkvertise.com/api/v1/redirect/link{object_path[0]}/target?X-Linkvertise-UT=" + token, options)
    data = json.loads(response)
    return data["data"]["target"]


def leakvertise(url: str) -> str:
    url = url.replace("%3D", " ").replace("&o=sharing", "").replace("?o=sharing", "").replace("dynamic?r=", "dynamic/?r=")

    result = cache.get(url)
    if result:
        return result

    if "dynamic/?r=" in url:
        buffer = url[url.index("dynamic/?r=") + 11:]
        result = base64.b64decode(buffer).decode("utf-8")
    else:
        result = leakvertise_non_dynamic(url)

    cache.set(url, result)
    return result
