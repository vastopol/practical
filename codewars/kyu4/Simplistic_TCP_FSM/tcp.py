def traverse_TCP_states(events):
    state = "CLOSED"  # initial state, always

    # states = [CLOSED, LISTEN, SYN_SENT, SYN_RCVD, ESTABLISHED, CLOSE_WAIT, LAST_ACK, FIN_WAIT_1, FIN_WAIT_2, CLOSING, TIME_WAIT]
    # actions = [APP_PASSIVE_OPEN, APP_ACTIVE_OPEN, APP_SEND, APP_CLOSE, APP_TIMEOUT, RCV_SYN, RCV_ACK, RCV_SYN_ACK, RCV_FIN, RCV_FIN_ACK]
    # transitions:
    for e in events:
        # CLOSED: APP_PASSIVE_OPEN -> LISTEN
        # CLOSED: APP_ACTIVE_OPEN  -> SYN_SENT
        if state == "CLOSED":
            if e == "APP_PASSIVE_OPEN":
                state = "LISTEN"
            elif e == "APP_ACTIVE_OPEN":
                state = "SYN_SENT"
            else:
                state = "ERROR"

        # LISTEN: RCV_SYN          -> SYN_RCVD
        # LISTEN: APP_SEND         -> SYN_SENT
        # LISTEN: APP_CLOSE        -> CLOSED
        elif state == "LISTEN":
            if e == "RCV_SYN":
                state = "SYN_RCVD"
            elif e == "APP_SEND":
                state = "SYN_SENT"
            elif e == "APP_CLOSE":
                state = "CLOSED"
            else:
                state = "ERROR"

        # SYN_RCVD: APP_CLOSE      -> FIN_WAIT_1
        # SYN_RCVD: RCV_ACK        -> ESTABLISHED
        elif state == "SYN_RCVD":
            if e == "APP_CLOSE":
                state = "FIN_WAIT_1"
            elif e == "RCV_ACK":
                state = "ESTABLISHED"
            else:
                state = "ERROR"

        # SYN_SENT: RCV_SYN        -> SYN_RCVD
        # SYN_SENT: RCV_SYN_ACK    -> ESTABLISHED
        # SYN_SENT: APP_CLOSE      -> CLOSED
        elif state == "SYN_SENT":
            if e == "RCV_SYN":
                state = "SYN_RCVD"
            elif e == "RCV_SYN_ACK":
                state = "ESTABLISHED"
            elif e == "APP_CLOSE":
                state = "CLOSED"
            else:
                state = "ERROR"

        # ESTABLISHED: APP_CLOSE   -> FIN_WAIT_1
        # ESTABLISHED: RCV_FIN     -> CLOSE_WAIT
        elif state == "ESTABLISHED":
            if e == "APP_CLOSE":
                state = "FIN_WAIT_1"
            elif e == "RCV_FIN":
                state = "CLOSE_WAIT"
            else:
                state = "ERROR"

        # FIN_WAIT_1: RCV_FIN      -> CLOSING
        # FIN_WAIT_1: RCV_FIN_ACK  -> TIME_WAIT
        # FIN_WAIT_1: RCV_ACK      -> FIN_WAIT_2
        elif state == "FIN_WAIT_1":
            if e == "RCV_FIN":
                state = "CLOSING"
            elif e == "RCV_FIN_ACK":
                state = "TIME_WAIT"
            elif e == "RCV_ACK":
                state = "FIN_WAIT_2"
            else:
                state = "ERROR"

        # CLOSING: RCV_ACK         -> TIME_WAIT
        elif state == "CLOSING":
            if e == "RCV_ACK":
                state = "TIME_WAIT"
            else:
                state = "ERROR"

        # FIN_WAIT_2: RCV_FIN      -> TIME_WAIT
        elif state == "FIN_WAIT_2":
            if e == "RCV_FIN":
                state = "TIME_WAIT"
            else:
                state = "ERROR"

        # TIME_WAIT: APP_TIMEOUT   -> CLOSED
        elif state == "TIME_WAIT":
            if e == "APP_TIMEOUT":
                state = "CLOSED"
            else:
                state = "ERROR"

        # CLOSE_WAIT: APP_CLOSE    -> LAST_ACK
        elif state == "CLOSE_WAIT":
            if e == "APP_CLOSE":
                state = "LAST_ACK"
            else:
                state = "ERROR"

        # LAST_ACK: RCV_ACK        -> CLOSED
        elif state == "LAST_ACK":
            if e == "RCV_ACK":
                state = "CLOSED"
            else:
                state = "ERROR"

        # ERROR
        if state == "ERROR":
            break

    return state
    