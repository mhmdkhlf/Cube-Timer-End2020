from solve import Solve, to_time_format

class SessionSolves:
    def __init__(self):
        self.solves = []

    def get_session_solves_list(self):
        return self.solves

    def add_solve(self, solve):
        if isinstance(solve, Solve):
            self.solves.append(solve)

    def delete_last_solve(self):
        del self.solves[-1]

    def get_solve_number(self, number):
        return self.solves[number-1]

    def get_number_of_solves(self):
        return len(self.solves)

    def get_best_solve(self, of=None):
        if self.get_number_of_solves() == 0:
            return None
        of = of if of!=None else self.get_number_of_solves()
        selected_solves = self.solves[-of:]
        return min(selected_solves)

    def get_worst_solve(self, of=None):
        if self.get_number_of_solves() == 0:
            return None
        of = of if of!=None else self.get_number_of_solves()
        selected_solves = self.solves[-of:]
        return max(selected_solves)

    def average(self, of=None):
        of = of if of!=None else self.get_number_of_solves()
        if self.get_number_of_solves() < of or of < 3:
            return '__'
        selected_solves = self.solves[-of:]
        best_time = self.get_best_solve(of=of)
        worst_time = self.get_worst_solve(of=of)
        selected_solves.remove(best_time)
        selected_solves.remove(worst_time)
        sum_times = 0
        for solve in selected_solves:
            if not solve.is_finished():
                return 'DNF'
            sum_times += solve.get_time()
        return to_time_format(sum_times / (of - 2))

    def mean(self):
        finished_solves = [solve for solve in self.solves if solve.is_finished()]
        if len(finished_solves) == 0:
            return '__'
        sum_times = 0
        for solve in finished_solves:
            sum_times += solve.get_time()
        return to_time_format(sum_times / len(finished_solves))
