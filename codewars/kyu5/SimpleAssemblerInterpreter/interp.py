def simple_assembler(program):
    pc = 0
    regs = dict()
    instructions = [p.split() for p in program]
    while True:
        if pc >= len(program) or pc < 0:
            break
        cur_in = instructions[pc]
        op = cur_in[0]
        if  op == 'mov':
            reg = cur_in[1]
            val = cur_in[2]
            if val.lstrip('-').isdigit():
                regs[reg] = int(val)
            else:
                regs[reg] = regs[val]
        elif op == 'inc':
            reg = cur_in[1]
            regs[reg] += 1
        elif op == 'dec':
            reg = cur_in[1]
            regs[reg] -= 1
        elif op == 'jnz':
            reg = cur_in[1]
            val = cur_in[2]
            if reg.lstrip('-').isdigit() and reg is not '0':
                pc += int(val)
                continue
            elif reg.isalpha() and regs[reg] != 0:
                pc += int(val)
                continue
        pc += 1
    return regs