def newState(thatInput, state):
    nextState = None
    match state:
        case 'A':
            if thatInput == 1:
                nextState = 'B'
            else:
                nextState = 'A'
        case 'B':
            if thatInput == 1:
                nextState = 'C'
            else:
                nextState = 'A'
        case 'C':
            if thatInput == 1:
                nextState = 'C'
            else:
                nextState = 'D'
        case 'D':
            if thatInput == 1:
                nextState = 'B'
            else:
                nextState = 'A'
    return nextState

def output(state):
    outputNum = -1
    match state:
        case 'A':
            outputNum = 0
        case 'B':
            outputNum = 0
        case 'C':
            outputNum = 0
        case 'D':
            outputNum = 1
    return outputNum

def stateMachine(thisInput):
    state = 'A'
    outputString = ''
    for num in range(len(thisInput)):
        outputString += str(output(state))
        print(output(state))
        state = newState(int(thisInput[num]),state)
    return outputString

def main():
    inputString = input('Enter a binary string: ')
    fullOutput = stateMachine(inputString)
    print('The output from this SM is:',fullOutput)

if __name__ == "__main__":
    main()

