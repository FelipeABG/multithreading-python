import threading
from time import time
from entities.waiter import Waiter
from entities.chef import Chef


def main():

    condition = threading.Condition()
    orders = []
    all_orders = []
    threads = []

    waiters = []
    chefs = []
    finished_waiters = []

    for i in range(5):
        waiters.append(Waiter(i, orders, condition, finished_waiters, all_orders))
    for i in range(3):
        chefs.append(Chef(i, orders, condition, finished_waiters, waiters))

    for waiter in waiters:
        t = threading.Thread(target=waiter.make_order)
        t.start()
        threads.append(t)

    before = time()
    for chef in chefs:
        t = threading.Thread(target=chef.prepare_order)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()
    after = time()
    print(f"Time to finish: {after - before} seconds.")

    for order in all_orders:
        print(
            f"Time it took to prepare | {order.get_info()} |: {order.get_total_time()}"
        )


if __name__ == "__main__":
    main()
