"""動的なデフォルト引数を指定するときにはNoneとdocstringを使う"""

from time import sleep
from datetime import datetime
import json
from typing import Optional


def log(message: str, when: Optional[datetime] = None) -> None:
    """
    Log a message with a timestamp.
    Args:
        message: Message to print.
        when: datetime of when the message occurred.
        Defaults to the present time.

    """
    if when is None:
        when = datetime.now()

    print(f"{when}: {message}")


log("Hi there!")
sleep(1)
log("Hi again!")


def decode(data: any, default: Optional[dict] = None) -> dict:
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default


foo = decode("bad data0")
foo["stuff"] = 5
print(foo)
