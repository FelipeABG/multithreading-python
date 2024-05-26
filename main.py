import threading
from entities.waiter import Waiter
from entities.chef import Chef


def main():

    orders = []
    condition = threading.Condition()
    threads = []

    waiters = []
    chefs = []

    for i in range(5):
        waiters.append(Waiter(i, orders, condition))
    for i in range(1):
        chefs.append(Chef(i, orders, condition))

    for waiter in waiters:
        t = threading.Thread(target=waiter.make_order)
        t.start()
        threads.append(t)

    for chef in chefs:
        t = threading.Thread(target=chef.prepare_order)
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
