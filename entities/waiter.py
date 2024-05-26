from random import uniform
from time import sleep


class Waiter:

    def __init__(self, orders, condition, id):
        self.id = id
        self.orders = orders
        self.condition = condition
        self.MAX_ORDERS = 10

    def make_order(self):
        for i in range(self.MAX_ORDERS):
            sleep(uniform(0.5, 1.5))

            with self.condition:

                while len(self.orders) <= 4:
                    self.condition.wait()

                order = f"Order {i} - Waiter {self.id}"
                self.orders.append(order)
                print(f"Waiter {self.id} realized | {order} |")
                self.condition.notify_all()
