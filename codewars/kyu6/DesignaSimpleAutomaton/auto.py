class Automaton(object):

    # q1: start state, q2: accept state
    # language: {'0','1'}
    def __init__(self):
        self.state = 1

    # q1: 0 -> q1; 1 -> q2;
    # q2: 0 -> q3; 1 -> q2;
    # q3: 0 -> q2; 1 -> q2;
    def read_commands(self, commands):
        for c in commands:
            if self.state == 1 and c == '1':
                self.state = 2
            elif self.state == 2 and c == '0':
                self.state = 3
            else:
                self.state = 2
        if self.state == 2:
            return True
        return False

my_automaton = Automaton()

