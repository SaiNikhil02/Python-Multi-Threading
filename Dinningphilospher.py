import threading
import time

class Philosopher(threading.Thread):
    def __init__(self, name, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            time.sleep(1)  # Thinking
            print(f"{self.name} is hungry")
            self.dine()

    def dine(self):
        left_fork, right_fork = self.left_fork, self.right_fork

        # To avoid deadlock, we need to establish a total ordering of resources (forks)
        first_fork, second_fork = (left_fork, right_fork) if id(left_fork) < id(right_fork) else (right_fork, left_fork)

        with first_fork:
            with second_fork:
                print(f"{self.name} is eating")
                time.sleep(1)  # Eating
                print(f"{self.name} finished eating and is thinking")

if __name__ == "__main__":
    forks = [threading.Lock() for _ in range(5)]
    philosopher_names = ['Philosopher 1', 'Philosopher 2', 'Philosopher 3', 'Philosopher 4', 'Philosopher 5']

    philosophers = [Philosopher(philosopher_names[i], forks[i], forks[(i + 1) % 5]) for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    for philosopher in philosophers:
        philosopher.join()
