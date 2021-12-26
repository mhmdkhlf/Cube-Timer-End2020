from datetime import datetime, timedelta

class Solve:
    def __init__(self, puzzle, scramble, initial_time, penalty = None):
        self.puzzle = puzzle
        self.scramble = scramble
        self.initial_time = initial_time
        self.penalty = penalty

    def __eq__(self, other):
        return (self.get_puzzle() == other.get_puzzle()
            and self.get_scramble == other.get_scramble()
            and self.get_time() == other.get_time()
            and self.get_penalty() == other.get_penalty()
        )

    def __gt__(self, other):
        if self.is_finished() and not other.is_finished():
            return False
        if not self.is_finished() and other.is_finished():
            return True
        return self.get_time() > other.get_time()

    def __lt__(self, other):
        if self.is_finished() and not other.is_finished():
            return True
        if not self.is_finished() and other.is_finished():
            return False
        return self.get_time() < other.get_time()

    def __str__(self):
        actual_time = self.get_time()
        return (f'Puzzle: {self.puzzle}\nScramble: {self.scramble}\nInnitial Time: {self.initial_time}'
               +f'\nPenalty: {self.penalty}\nActual time: {actual_time}')

    def is_finished(self):
        return self.penalty != 'DNF'

    def get_puzzle(self):
        return self.puzzle

    def get_scramble(self):
        return self.scramble

    def get_time(self):
        if not self.is_finished():
            return 0
        elif self.penalty == '+2':
            return self.initial_time + 2
        return self.initial_time

    def get_penalty(self):
        return self.penalty

    def set_time(self, time):
        if isinstance(time, float):
            self.initial_time = time

    def dnf(self):
        self.penalty = 'DNF'

    def plus2(self):
        self.penalty = '+2'

    def time_output(self):
        if not self.is_finished():
            return 'DNF'
        sec = timedelta(seconds=self.get_time())
        d = datetime(1,1,1) + sec
        if d.minute==0:
            time = "%d.%.3d" % (d.second,d.microsecond/1000)
        else:
            time = "%d:%.2d.%.3d" % (d.minute, d.second,d.microsecond/1000)
        if self.penalty == '+2':
            return f'({time})+'
        return time