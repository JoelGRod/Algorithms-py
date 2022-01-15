import time

""" Count list elements
"""

def count_items(elements):
    if elements == []: return 0
    return 1 + count_items(elements[1:])

# Faster
def count_items_two(elements):
    try: elements[1]
    except: return 1
    return 1 + count_items_two(elements[1:])

elements = [1,2,3,4,5,6,7,8,9,99]

start = time.process_time()
print(count_items(elements))
print(f"{(time.process_time() - start)*1000:8f} ms")

start = time.process_time()
print(count_items_two(elements))
print(f"{(time.process_time() - start)*1000:8f} ms")