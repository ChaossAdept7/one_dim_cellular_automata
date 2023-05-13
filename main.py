def cellular_automaton(rule_number, initial_state, steps):
    # Obtaining a binary representation of a rule
    rule_string = format(rule_number, '08b')
    rule = list(map(int, rule_string))

    # Initializing the current state
    current_state = initial_state

    for _ in range(steps):
        print(''.join(current_state).replace('0', ' ').replace('1', '*'))
        new_state = ''

        for i in range(len(current_state)):
            # Determining the neighborhood of each cell
            left = '0' if i == 0 else current_state[i - 1]
            center = current_state[i]
            right = '0' if i == len(current_state) - 1 else current_state[i + 1]
            neighborhood = left + center + right

            # Applying a Rule to a Neighborhood
            rule_index = 7 - int(neighborhood, 2)
            new_state += str(rule[rule_index])

        current_state = new_state

# other rules.
# 222 == 11011110
# 190 == 10111110
# 30 == 00011110
# 110 == 01101110
# 90 == 01011010
# 259 == 100000011

rule_number = 90
begin_generation = '0000000000000000000100000000000000000000'
number_of_generations = 20


cellular_automaton(rule_number, begin_generation, number_of_generations)