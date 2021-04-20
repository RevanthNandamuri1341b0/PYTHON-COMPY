def cell_compete(states, days):
    def new_state(in_states):
        new_state = []
        for i in range(len(in_states)):
            if i == 0:
                group = [0, in_states[0], in_states[1]]
            elif i == len(in_states) - 1:
                group = [in_states[i - 1], in_states[i], 0]
            else:
                group = [in_states[i - 1], in_states[i], in_states[i + 1]]
            new_state.append(0 if group[0] == group[2] else 1)
        return new_state

    state = None
    j = 0
    while j < days:
        if not state:
            state = new_state(states)
        else:
            state = new_state(state)
        j += 1
    return state