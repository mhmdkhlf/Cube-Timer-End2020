from solve import Solve

class Session_Solves():
    def __init__(self, solves = []):
        self.solves = solves
    
    def get_session_solves_list(self):
        return self.solves

    def add_solve(self, solve):
        if isinstance(solve, Solve):
            self.solves.append(solve)

    def delete_last_solve(self):
        del self.solves[-1]
    
    def get_number_of_solves(self):
        return len(self.solves)

    def get_best_time(self, of=None):
        if of==None:
            of = self.get_number_of_solves()
        selected_solves = self.solves[-of:] 
        return min(selected_solves)

    def get_worst_time(self, of=None):
        if of==None:
            of = self.get_number_of_solves()
        selected_solves = self.solves[-of:] 
        return max(selected_solves)

    def average(self, of=None):
        if of != None and (self.get_number_of_solves() < of or of < 3):
            return ''    
        if of==None:
            of = self.get_number_of_solves()
        selected_solves = self.solves[-of:] 
        best_time = self.get_best_time(of=of)
        worst_time = self.get_worst_time(of=of)
        selected_solves.remove(best_time)
        selected_solves.remove(worst_time)
        sum_times = 0
        for solve in selected_solves:
            if not solve.is_finished():
                return 'DNF'
            sum_times += solve.get_time()
        return format(sum_times / (of - 2), '.3f')
    
    def session_mean(self):
        finished_solves = [solve for solve in self.solves if solve.is_finished()]
        if len(finished_solves) == 0:
            return ''
        sum_times = 0
        for solve in finished_solves:
            sum_times += solve.get_time()
        return format(sum_times / len(finished_solves), '.3f')