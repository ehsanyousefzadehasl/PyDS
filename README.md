# Data-Structures

This repository aims to implement popular data structures with python programming language Version 3

## Season 1 - Introduction and Efficiency
Efficiency: In Algorithm Concept, It is also called Complexity. It is how well you are using your computer resources to get a particular job done. We can Think about it in terms of Space (How Much Storage Space Needed?) and Time (How Long the Code takes to Run?).

The important Tradeoff in Algorithms Complexity Discussion:

1. Time Efficiency
2. Storage Space Efficiency

Open an Algorithm Book and read the Complexity Notations which we use for explaining algorithms complexity too in this repository

This season is Done!

## Season 2 - List-based Collection

The main Work starts from this point. Be Ready for Coding and Enjoying DS and AD :)

We can list the list-based collection as in following list

1. **Arrays**
    (1) The most common implementation of Lists
    (2) fixed length
    (3) hard to exploit
    (4) Messy Insertion and Deletion (index finiding for accesses - shiftings are needed by the programmer - order: O(n) -> very inefficient) 
2. **Linked Lists**: 
    (1) Insertion and Deletion is more easier and neater than Array - Order O(1) 
    (2) Each element has the next element (or even previous element in DLL (Doubled Linked List)) pointer
3. **Stacks**:
    (1) Push and Pop Operations are done by order of O(1)
    (2) We can use Linked List to implement a Stack by focusing on its head
    (3) Stack is know as LIFO (Last-In-First-Out) Structure
4. **Queues**:
    (1) It is a FIFO (First-In-First-Out) Structure
    (2) It is oposite of a stack
    (3) Head -> Oldest Element in the Queue, Tail -> Newest Element in the Queue
    (4) Enqueue -> Adding an Element to the tail
    (5) Dequeue -> Removing the Head Element
    (6) Peak Operation -> Viewing Head Element without changing it
    (7) It is implementable by a Linked-List
    (8) Deque --> It is a double ended queue that goes both ways. We can enqueue and dequeue from either end. A Deque is a general version of both stacks and queues.
    (9) Priority Queue: Each element has a priority number when we insert them into the queue. When we are going to dequeue, element with maximum priority goes to be removed.

**Python list**
Python has an interesting data stucture called a "list" that is much more than a mere list. In fact, a Python list actually encompasses the functionality of almost every list-based data structure came above. 

**Linked List**
There is not a built-in data structure in python that look likes a linked list. but you can see how it is implementable in python v3 in [here](https://github.com/ehsanyousefzadehasl/Data-Structures/blob/master/season1_List_based_Collection/Linked-List/linked-list.py)

**Stack**
I want to make you happy that you don't need to implement the stack in the python because The Python has the stack functionality in built-in way. Python with `append()` and `pop()` functions does push and pop functionalities. You can find Stack implementation in python v3 [here](https://github.com/ehsanyousefzadehasl/Data-Structures/blob/master/season1_List_based_Collection/Stack/stack.py)

**Queue**
Be Happy! Python has a built-in class for Queues and the following example shows how to use python built-in queues. But we are going to implement it ourselves, you can view it [here]()

```import Queue
q = Queue.Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print q.get()```
