from random import uniform
from time import sleep


class Chef:

    def __init__(self, id, orders, condition):
        self.id = id
        self.orders = orders
        self.condition = condition

    def prepare_order(self):
        while True:
            with self.condition:
                while not self.orders:
                    self.condition.wait()

                order = self.orders.pop(0)
                print(f"Chef {self.id} prepared | {order} |")
                self.condition.notify_all()

            sleep(uniform(1, 3))
