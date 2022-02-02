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
        self.top = None
        self.items = {}
        self.aux_stack = []
    
    def empty(self):
        return self.top == None
    
    def peek(self):
        return [self.top[0], self.top[1]]
    
    def pop(self):
        print(self.top)
        top = self.top
        self.top = self.items[self.top[3]]

        if self.top: self.top[2] = None  
        else: self.top = None

        self.remove(top[0])

        return [top[0], top[1]]
    
    def remove(self, key):
        self.items.pop(key)
        self.aux_stack = [item for item in self.aux_stack if item[0] != key]
    
    def push(self, key, priority):
        # check if exists and has a different priority
        self.item_exists(key, priority)
        # if new
        item = [key, priority, None, None]
        self.items[key] = item

        self.heap_sort(item)

        for idx, item in enumerate(self.aux_stack):
            if not self.aux_stack[idx - 1]: 
                self.items[self.aux_stack[idx][0]][2] = None
            if len(self.aux_stack) > 1 and len(self.aux_stack) - 1 >= idx + 1: 
                self.items[self.aux_stack[idx][0]][3] = self.aux_stack[idx + 1][0]
            if self.aux_stack[idx - 1]:
                self.items[self.aux_stack[idx][0]][2] = self.aux_stack[idx - 1][0]
        
        self.top = self.aux_stack[0]
    
    def item_exists(self, key, priority):
        if key in self.items and self.items[key][1] != priority:
            self.remove(key)
    
    def heap_sort(self, item):
        contain = False
        for idx, item in enumerate(self.aux_stack):
            if self.aux_stack[idx][1] >= item[1]:
                self.aux_stack.insert(idx, item)
                contain = True
                break
        
        if not contain: self.aux_stack.append(item)

