class ExpenseReportAnalyzer():

    def __init__(self, input: list) -> None:
        self.list_input = input
        super().__init__()

    def get_couples_list(self) -> [int, int, list]:
        for idx, nb in enumerate(self.list_input):
            for idx_bis in range(idx + 1, len(self.list_input)):
                nb2 = self.list_input[idx_bis]
                yield nb, nb2, self.list_input[idx_bis + 1:]

    def get_target_couple(self) -> (int, int):
        for nb1, nb2, _ in self.get_couples_list():
            if nb1 + nb2 == 2020:
                return nb1, nb2

    def get_target_triplet(self) -> (int, int, int):
        for nb1, nb2, remainder_list in self.get_couples_list():
            if nb1 + nb2 < 2020:
                maybe_nb3 = 2020 - nb1 - nb2
                if maybe_nb3 in remainder_list:
                    return nb1, nb2, maybe_nb3

    def compute_anwswer(self) -> (int, int):
        nb1, nb2 = self.get_target_couple()
        return nb1 * nb2

    def compute_anwswer_part2(self) -> (int, int, int):
        nb1, nb2, nb3 = self.get_target_triplet()
        return nb1 * nb2 * nb3
