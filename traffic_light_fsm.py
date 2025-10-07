from enum import Enum


class TrafficLightState(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3

class TrafficLightFSM:
    def __init__(self):
        self.state = TrafficLightState.RED

    def next_state(self):
        if self.state == TrafficLightState.RED:
            self.state = TrafficLightState.GREEN
        elif self.state == TrafficLightState.GREEN:
            self.state = TrafficLightState.YELLOW
        elif self.state == TrafficLightState.YELLOW:
            self.state = TrafficLightState.RED

    def show_state(self):
        print("Current state:", self.state.name)

if __name__ == "__main__":
    tl = TrafficLightFSM()
    for _ in range(5):
        tl.show_state()
        tl.next_state()