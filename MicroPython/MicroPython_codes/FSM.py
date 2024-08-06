import time

class StateMachine:
    def __init__(self):
        self.state = 'IDLE'
        self.transitions = {
            'IDLE': self.idle_state,
            'RUNNING': self.running_state,
            'STOPPED': self.stopped_state
        }

    def idle_state(self):
        print("Idle state")
        time.sleep(1)
        return 'RUNNING'

    def running_state(self):
        print("Running state")
        time.sleep(1)
        return 'STOPPED'

    def stopped_state(self):
        print("Stopped state")
        time.sleep(1)
        return 'IDLE'

    def run(self):
        while True:
            self.state = self.transitions[self.state]()

# Example usage
fsm = StateMachine()
fsm.run()


"""
(venv) PS C:\Users\vlab\PycharmProjects\MicroPython_codes> ampy --port COM7 run .\FSM.py       
Idle state
Running state
Stopped state
Idle state
Running state
Stopped state
Idle state
Running state
"""