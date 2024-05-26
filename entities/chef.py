from random import uniform
from time import sleep, time


class Chef:

    def __init__(self, id, orders, condition, finished_waiters, waiters):
        self.waiters = waiters
        self.finished_waiters = finished_waiters
        self.id = id
        self.orders = orders
        self.condition = condition

    def prepare_order(self):
        while True:
            with self.condition:
                while not self.orders and len(self.finished_waiters) < len(
                    self.waiters
                ):
                    self.condition.wait()

                if not self.orders and len(self.finished_waiters) == len(self.waiters):
                    break

                order = self.orders.pop(0)
                order.chef_id = self.id
                order.finish_time = time()
                print(f"Chef {self.id} prepared | {order.get_info()} |")
                self.condition.notify_all()

            sleep(uniform(1, 3))
