from typing import List, Tuple

'''
turing_machine.py

Simulates a nondeterministic turing machine and returns the turing machine definition when it halts.
User inputs the initial tape, and transitions of the form: qsd, where q is the state to go to, s is
the symbol to write at the head location, and d is direction (r or l) to move the head.
'''

# Moves one symbol to the right on the tape, and ensures there are always blanks on the ends of the tape
def right(i, tape):
    if (i == len(tape) - 1):
        tape.append('#')
    elif (i == 0):
        tape.insert(0, '#')
        i += 1
        
    return (tape, i + 1)
    
# Moves one symbol left on the tape, and ensures there is always a blank at the start of the tape
def left(i, tape):
    if (i == 0):
        tape.insert(0, '#')
    elif (i == len(tape) - 1):
        tape.append('#')
    else:
        i -= 1

    return (tape, i)

# Run the turing machine on the given state, recording the transitions
def process(tape):
    transitions: List[Tuple] = []
    states = ['0']
    # Populate the input alphabet
    sigma = []
    for c in tape:
        if c not in sigma:
            sigma.append(c)
            
    gamma = []
    gamma.extend(sigma)
    tape.insert(0, '#')
    tape.append('#')
    state = '0'
    i = 1
    running = True
    
    while(running):          
        print('State ' + state + ': ' + ''.join(tape))
        print(' ' * (i + 8 + len(state)) + '^')
        
        # Read the user input as the destination of the current transition
        move = input('Transition to: ')
        
        # Exit the loop if halt is entered
        if (move == 'halt'):
            running = False
            continue
        elif (len(move) < 3):
            continue

        # Add the complete transition to the list if it hasn't been recorded
        t = (state + tape[i], move)
        if (t not in transitions):
            transitions.append(t)
        
        # Update the state and add it to the list of states if needed
        state = move[0]
        if (state not in states):
            states.append(state)
        
        # Replace the symbol at the head position, adding it to the tape alphabet if needed
        tape[i] = move[1]
        if move[1] not in gamma:
            gamma.append(move[1])
        
        if (move[2] == 'r'):
            tape, i = right(i, tape)
        elif (move[2] == 'l'):
            tape, i = left(i, tape)
        else:
            continue
    
    # Print the turing machine description
    print('\nM = ({' + ', '.join(states) + '}, {' + ', '.join(sigma) + '}, {' + ', '.join(gamma) + '}, δ, 0, #, {' + state + '})')
    
    print('Transitions: ')
    for t in transitions:
        print('(' + ', '.join(t[0]) + ') = (' + ', '.join(t[1]) + ')')
        
# Initialize tape
tape = list(input('Insert string: '))

process(tape)
    