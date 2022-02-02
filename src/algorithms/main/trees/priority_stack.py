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

