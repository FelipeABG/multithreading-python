class Order:

    def __init__(self, number, waiter_id, start_time):
        self.number = number
        self.waiter_id = waiter_id
        self.chef_id = None
        self.finish_time = None
        self.start_time = start_time

    def get_total_time(self):
        return self.finish_time - self.start_time

    def get_info(self):
        return f"Order {self.number} - Waiter {self.waiter_id}"
