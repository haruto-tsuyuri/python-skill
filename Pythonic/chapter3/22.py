"""可変長一引数を使ってみた目をすっきりさせる"""


def log(message: str, *values: int or float) -> None:
    if not values:
        print(message)
    else:
        values_str = ", ".join(str(x) for x in values)
        print(f"{message}:{values_str}")


favorites = [1, 2, 3, 44]

log("My number is ", 1, 23, 4, 4)
log("Hi")

log("My favorites is ", *favorites)


