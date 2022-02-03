"""
A priority queue / stack is a special queue / stack where:

Every item in the queue has a priority, and Higher-priority items are 
dequeued before lower-priority items.

Picture a big list of bugs for an engineering team to tackle. 
You want to keep the highest-priority bugs at the top of the list.

Strengths:
Quickly access the highest-priority item. Priority queues allow 
you to peek at the top item in O(1)O(1) while keeping other operations 
relatively cheap (O(lg(n))O(lg(n))).

Weaknesses:
Slow enqueues and dequeues. Both operations take O(\lg(n))O(lg(n)) 
time with priority queues. With normal first-in, first-out queues, 
these operations are O(1)O(1) time.

Uses:
Any time you want to handle things with different priority levels: 
triaging patients in a hospital, locating the closest available taxi, 
or just a to-do list.

Operating system schedulers may use priority queues to select the next 
process to run, ensuring high-priority tasks run before low-priority ones.

Certain foundational algorithms rely on priority queues:
Dijkstra's shortest-path
A* search (a graph traversal algorithm like BFS)
Huffman codes (an encoding for data compression)
"""


class PriorityStack:

    def __init__(self):
        self.items = {}
        self.register = {}
        self.ordered_priorities = []

    def empty(self):
        return len(self.ordered_priorities) == 0

    def peek(self):
        return self.items[self.ordered_priorities[0]][0]

    def pop(self):
        next = self.peek()
        self.remove(next[0], next[1])
        self.sort_priorities()
        return [next[0], next[1]]

    def remove(self, key, priority):
        self.register.pop(key)
        self.items[priority] = [
            item for item in self.items[priority] if item[0] != key]
        if len(self.items[priority]) == 0:
            self.items.pop(priority)

    def push(self, key, priority):
        # check if exists and has a different priority
        self.item_exists(key, priority)
        # create new
        item = [key, priority]
        # Stack (item at the beginning - LIFO)
        self.items[priority].insert(0, item)
        # Update ordered priorities if necessary
        self.sort_priorities()

    def item_exists(self, key, priority):
        if key in self.register and self.register[key] != priority:
            self.remove(key, self.register[key])
        if priority not in self.items:
            self.items[priority] = []
        if key not in self.register:
            self.register[key] = priority

    def sort_priorities(self):
        # Error here
        priorities = list(self.items.keys())
        print(priorities)
        print(type(self.ordered_priorities))
        if len(self.ordered_priorities) < len(priorities):
            self.ordered_priorities = priorities.sort()
