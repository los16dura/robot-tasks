import re

STOPSTATE = "STOP"
EMPTYSYMBOL = "B"

def getRulesFromFile(file_rools = None):
    if not file_rools:
        file_rules = 'rules.txt'
    f = open(file_rules, 'r')
    lines = f.readlines()
    f.close()

    regExp = '^(.)q(\d+)->(.)(q(\d+)(.)|STOP)$'
    #key = (fromSymbol, fromState)
    #value = (toSymbol, toState, +/-1)
    rules = {}

    for line in lines:
        ruleLine = line.strip()
        matchObj = re.match(regExp, ruleLine)
        if matchObj:
            g = matchObj.groups()
            print(g)
            fromSymbol = g[0]
            fromState = g[1]
            toSymbol = g[2]
            toState = STOPSTATE if g[3] == STOPSTATE else int(g[4])
            move = 1 if g[5] == 'R' else -1

            if toState == STOPSTATE:
                rules[(fromSymbol, fromState)] = (toSymbol, toState, None)
            else:
                rules[(fromSymbol, fromState)] = (toSymbol, toState, move)
    return rules

def getInputFromFile(filename = None):
    if not filename:
        filename = 'input.txt'
    f = open(filename, 'r')
    return f.readline().strip()

def emulateTuringMachine(rules, inputData):
    tape = list(inputData) + [EMPTYSYMBOL]*10
    print(tape)

    currentState = 1
    currentInd = 0

    while currentState != STOPSTATE:
        currentSymbol = tape[currentInd]
        if (currentSymbol, currentState) not in rules:
            print("Error!!!")
            return
        else:
            toSymbol, toState, move = rules[(currentSymbol, currentState)]
            if toState == STOPSTATE:
                tape[currentInd] = toSymbol
                print(''.join(tape))
                return
            else:
                tape[currentInd] = toSymbol
                currentState = toState
                currentInd += move
                print(''.join(tape))


emulateTuringMachine(getRulesFromFile(), getInputFromFile())
