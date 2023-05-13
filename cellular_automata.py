def cellular_automaton(rule_number, initial_state, steps):
    # Получение бинарного представления правила
    rule_string = format(rule_number, '08b')
    rule = list(map(int, rule_string))

    # Инициализация текущего состояния
    current_state = initial_state

    for _ in range(steps):
        print(''.join(current_state).replace('0', ' ').replace('1', '*'))
        new_state = ''

        for i in range(len(current_state)):
            # Определение окрестности каждой ячейки
            left = '0' if i == 0 else current_state[i - 1]
            center = current_state[i]
            right = '0' if i == len(current_state) - 1 else current_state[i + 1]
            neighborhood = left + center + right

            # Применение правила к окрестности
            rule_index = 7 - int(neighborhood, 2)
            new_state += str(rule[rule_index])

        current_state = new_state