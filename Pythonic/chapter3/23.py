"""キーワード引数にオプションのふるまいを与える"""


def print_parameters(**kwargs: any) -> None:
    for key, value in kwargs.items():
        print(f"{key} = {value}")


rgb = {"R": 256, "G": 0, "B": 55}

print_parameters(**rgb)


def flow_rate(weight_diff: float, time_diff: float, period: float = 1.0, units_per_kg: float = 1.0) -> float:
    return ((weight_diff * units_per_kg) / time_diff) * period


print(flow_rate(1.9, 0.4, period=2.0, units_per_kg=2.0))

