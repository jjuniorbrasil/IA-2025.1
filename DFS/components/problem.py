class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Problem:
    def __init__(self, initialState: str, goal: str, actions):
        self.initialState = initialState
        self.goal = goal
        self.actions = actions
        print(bcolors.OKCYAN + f"\nProblema criado - ESTADO INICIAL: {self.initialState}, OBJETIVO: {self.goal}\n" + bcolors.ENDC)

    def goalTest(self, state: str):
        return self.goal == state

    def action(self, state):
        return self.actions.get(state, [])