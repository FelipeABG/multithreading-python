# README: Restaurant Simulation Using Threads in Python

## Overview

This project is a practical exercise designed to simulate a restaurant system using threads and conditionals in Python. The simulation involves one cook and multiple waiters who take orders from customers, deliver these orders to the cook, and finally serve the prepared food back to the customers. The goal is to ensure efficient operation without unnecessary waiting times.

## Objectives

- **Learn and practice**: Enhance your understanding of Python threading and conditionals by applying these concepts to a real-world scenario.
- **Develop coordination**: Implement a system where multiple waiters and a cook coordinate efficiently using threading.Condition.
- **Performance measurement**: Measure and optimize the total service time of the restaurant.

## Project Description

### Task

You are required to simulate a restaurant with one cook and multiple waiters using Python. The simulation will involve:
- **Waiters**: Take orders from customers and deliver them to the cook. Each waiter can make up to 10 orders per night.
- **Cook**: Prepares the orders received from the waiters and hands them back to the waiters for serving.

### Constraints

- The kitchen can only handle a limited number of pending orders at a time (maximum of 4).
- Waiters need to wait if the kitchen is full.
- The cook waits if there are no pending orders.
- The restaurant closes when all orders have been processed.

### Implementation Steps

1. **Class Garcom (Waiter)**
   - Method `make_order`: Adds a new order to the list of pending orders.
   
2. **Class Cozinheiro (Cook)**
   - Method `prepare_order`: Removes an order from the list of pending orders and prepares it.
   
3. **Coordination**
   - Use `threading.Condition` to manage access to the list of pending orders.
   
4. **Simultaneous Operation**
   - Create multiple instances of `Waiter` and one instance of `Chef`, running them in separate threads.

5. **Synchronization**
   - Ensure waiters wait if the kitchen is full and the cook waits if there are no pending orders.

6. **Completion**
   - Ensure the kitchen closes after all orders are processed.
   
7. **Performance Measurement**
   - Implement a system to measure the total time from opening the restaurant to closing the kitchen.


