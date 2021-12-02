import os
import sqlite3
from . import __name__ as module_name


class Cache:
    __cache_path = os.path.join(os.getcwd(), module_name, "leakvertise.sqlite")
    __connection = sqlite3.connect(__cache_path, isolation_level=None)
    def __init__(self) -> None:
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY AUTOINCREMENT,from_url TEXT NOT NULL,to_url TEXT NOT NULL)")

    def set(self, from_url: str, to_url: str):
        return self.__cursor.execute("INSERT INTO links (from_url,to_url) VALUES (?,?)", [from_url, to_url]).rowcount

    def get(self, from_url: str):
        result = self.__cursor.execute("SELECT links.to_url FROM links WHERE links.from_url=?", [from_url]).fetchone()
        if result and len(result) >= 0:
            return result[0]
        return None
