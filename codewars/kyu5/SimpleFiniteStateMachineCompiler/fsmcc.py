class FSM(object):

    def __init__(self, instructions):
        # Members
        self.states = dict()
        # Compile instructions string to states map
        i = 0
        j = 0
        states = dict()
        for i in range(len(instructions)):
            if instructions[i] == '\n':
                tmp = instructions[j:i].split(';')
                nxt = tmp[1].split(',')
                states[tmp[0]] = (nxt[0].strip(),nxt[1].strip(),tmp[2].strip())
                j = i+1
        tmp = instructions[j:].split(';')
        nxt = tmp[1].split(',')
        states[tmp[0]] = (nxt[0].strip(),nxt[1].strip(),tmp[2].strip())
        self.states = states

    def run_fsm(self, start, sequence):
        # return tuple: (final_state, final_state_output, path)
        cur = start
        out = self.states[start][2]
        path = list()

        for inp in sequence:
            print(cur, out, inp, self.states[cur][inp])
            path.append(cur)
            cur = self.states[cur][inp]
            out = self.states[cur][2]
        path.append(cur)

        return (cur, int(out), path)
        