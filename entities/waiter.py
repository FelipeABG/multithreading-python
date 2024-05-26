from random import uniform
from entities.order import Order
from time import sleep, time


class Waiter:

    def __init__(self, id, orders, condition, finished_waiters):
        self.finished_waiters = finished_waiters
        self.id = id
        self.orders = orders
        self.condition = condition
        self.MAX_ORDERS = 10

    def make_order(self):
        for i in range(self.MAX_ORDERS):
            sleep(uniform(0.5, 1.5))

            with self.condition:

                while len(self.orders) >= 4:
                    self.condition.wait()

                order = Order(i, self.id, time())
                self.orders.append(order)
                print(f"Waiter {self.id} realized | {order.get_info()} |")
                self.condition.notify_all()

        with self.condition:
            self.finished_waiters.append(self.id)
            self.condition.notify_all()
