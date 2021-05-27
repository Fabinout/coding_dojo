class Odometer:

    def __init__(self, mileage: int) -> None:
        self.mileage = mileage

    def get_label(self) -> str:
        standard_odometer_size = 6
        number_of_prefixed_zeros = standard_odometer_size - len(str(self.mileage))
        return "0" * number_of_prefixed_zeros + str(self.mileage)


def contains_interesting_number(odo: Odometer) -> bool:
    return any([value in odo.get_label() for value in ["051968", "69"]])


def is_interesting(odometer: Odometer) -> bool:
    if contains_interesting_number(odometer): return True
    if all_figures_are_the_same(odometer): return True
    return False


def all_figures_are_the_same(odometer: Odometer) -> bool:
    setOfFigures = set(odometer.get_label())
    return len(setOfFigures) == 1
