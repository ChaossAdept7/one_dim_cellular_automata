from cellular_automata import cellular_automaton

rule = 90

# other rules.
# 222 == 11011110
# 190 == 10111110
# 30 == 00011110
# 110 == 01101110
# 90 == 01011010
# 259 == 100000011

begin_generation = '0000000000000000000100000000000000000000'
number_of_generations = 20


cellular_automaton(rule, begin_generation, number_of_generations)