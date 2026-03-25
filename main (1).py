import random

class Room:
    def __init__(self, dirtiness_level: int = 0):
        self.dirtiness_level = dirtiness_level

    def is_clean(self) -> bool:
        return not self.dirtiness_level

    def clean(self) -> None:
        self.dirtiness_level = 0

    def make_dirty(self, level: int) -> None:
        if 1 <= level <= 5:
            self.dirtiness_level = level
        else:
            raise ValueError("Dirt level must be between 1 and 5")

    def get_dirt_level(self) -> int:
        return self.dirtiness_level


class Environment:
    def __init__(self, n_rooms: int):
        self.n_rooms = n_rooms
        self.rooms: list[Room] = []
        # Initialize rooms
        for i in range(self.n_rooms):
            self.rooms.append(Room(random.randint(0, 5)))

    def get_room(self, room_index: int) -> Room:
        return self.rooms[room_index]

    def clean_room(self, room_index: int) -> int:
        dirt_level = self.get_room(room_index).dirtiness_level
        self.rooms[room_index].clean()
        return dirt_level

    def update_environment(self) -> None:
        for room in self.rooms:
            if room.is_clean() and random.random() < 0.1:
                room.make_dirty(random.randint(1, 5))

    def is_all_clean(self) -> bool:
        return all(room.is_clean() for room in self.rooms)

    def get_state(self) -> list[int]:
        return [room.get_dirt_level() for room in self.rooms]


class Agent:
    def __init__(self, n_rooms: int):
        self.n_rooms = n_rooms
        self.current_position: int = 0
        self.current_energy: float = n_rooms * 2.5
        self.logs: list[dict] = []
        self.direction = 'right'

    def perceive(self, environment: Environment) -> dict:
        current_room = environment.get_room(self.current_position)
        percepts = {
            'position': self.current_position,
            'room_clean': current_room.is_clean(),
            'dirt_level': current_room.get_dirt_level(),
            'energy': self.current_energy
        }
        return percepts

    def decide_action(self, environment: Environment) -> str:
        current_room = environment.get_room(self.current_position)

        # Rule 1: Room is dirty and can afford → Suck
        if not current_room.is_clean() and self.can_suck(environment):
            return 'Suck'

        # Rule 2: Mission complete - all rooms clean
        if environment.is_all_clean():
            return 'Stop'

        # Rule 3: Try to move with direction tracking
        if self.can_move():
            if self.current_position == self.n_rooms - 1:
                self.direction = 'left'
                return 'MoveLeft'
            elif self.current_position == 0:
                self.direction = 'right'
                return 'MoveRight'
            else:
                # Continue in current direction
                if self.direction == 'right':
                    return 'MoveRight'
                else:
                    return 'MoveLeft'

        # Rule 4: Can't do anything (out of energy)
        return 'Stop'

    def suck(self, environment: Environment) -> None:
        energy_cost = environment.clean_room(self.current_position)
        self.current_energy -= energy_cost
        self.log_action('Suck', energy_cost)

    def move_left(self) -> None:
        self.current_position -= 1
        self.current_energy = self.current_energy - 2
        self.log_action('MoveLeft', 2)

    def move_right(self) -> None:
        self.current_position += 1
        self.current_energy = self.current_energy - 2
        self.log_action('MoveRight', 2)

    def can_suck(self, environment: Environment) -> bool:
        current_room = environment.get_room(self.current_position)
        return current_room.get_dirt_level() <= self.current_energy

    def can_move(self) -> bool:
        return self.current_energy >= 2

    def log_action(self, action: str, energy_cost: int) -> None:
        log_entry = {
            'action': action,
            'room': self.current_position,
            'energy_cost': energy_cost
        }
        self.logs.append(log_entry)


def simulate(n_rooms: int, max_steps: int) -> dict:
    environment = Environment(n_rooms)
    agent = Agent(n_rooms)

    initial_energy = agent.current_energy
    steps_taken = 0

    for step in range(max_steps):
        steps_taken += 1

        # Agent decides what to do
        action = agent.decide_action(environment)

        # If agent decided to stop, exit loop
        if action == "Stop":
            break

        # Execute the action
        if action == 'Suck':
            agent.suck(environment)
        elif action == 'MoveLeft':
            agent.move_left()
        elif action == 'MoveRight':
            agent.move_right()

        # Update environment (10% re-dirtying)
        environment.update_environment()

    rooms_cleaned = 0
    for log in agent.logs:
        if log['action'] == 'Suck':
            rooms_cleaned += 1

    energy_consumed = initial_energy - agent.current_energy

    final_state = environment.get_state()

    results = {
        'final_state': final_state,
        'rooms_cleaned': rooms_cleaned,
        'energy_consumed': energy_consumed,
        'energy_remaining': agent.current_energy,
        'actions': agent.logs,
        'steps_taken': steps_taken
    }

    return results


if __name__ == "__main__":
    while True:
        try:
            n_rooms = int(input("Enter number of rooms: "))
            if n_rooms < 1:
                print("Number of rooms must be at least 1")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")

    while True:
        try:
            max_steps = int(input("Enter maximum steps: "))
            if max_steps < 1:
                print("Maximum steps must be at least 1")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    results = simulate(n_rooms = n_rooms, max_steps = max_steps)

    print("=== SIMULATION RESULTS ===")
    print(f"Steps taken: {results['steps_taken']}")
    print(f"Rooms cleaned: {results['rooms_cleaned']}")
    print(f"Energy consumed: {results['energy_consumed']}")
    print(f"Energy remaining: {results['energy_remaining']}")
    print(f"\nFinal room states: {results['final_state']}")
    print(f"\nAction sequence:")
    for i, action in enumerate(results['actions'], 1):
        print(f"  {i}. {action['action']} at room {action['room']} (cost: {action['energy_cost']})")