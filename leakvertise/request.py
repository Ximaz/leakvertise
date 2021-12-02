import json
import urllib.request
import urllib.parse
import urllib.error


def request(url: str, body: dict = None) -> str:
    http = urllib.request.Request(url=url, method="GET" if body is None else "POST", data=json.dumps(body).encode("utf-8") if body is not None else None, headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    with urllib.request.urlopen(http) as response:
        content = response.read().decode("utf-8")
    response.close()
    return content
