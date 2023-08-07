# Sort function Collection
List of Sort algorism
- bubble sort
- insert sort
- select sort
- shell sort
- quick sort(with critical bug)
- merge sort

And memory array
- stack
- queue

## Usage
```shell
pip install git+https://github.com/maru0123-2004/sort
```
and...
```python3
import sort

sort.bubble([1, 4, 5, 2, 3])
# [1, 2, 3, 4, 5]
sort.insert([1, 4, 5, 2, 3])
# [1, 2, 3, 4, 5]
sort.select([1, 4, 5, 2, 3])
# [1, 2, 3, 4, 5]
#...

#You can check is the list sorted with...
sort.isSorted([1, 2, 3, 4, 5])
# True

import pipe
stack=pipe.Stack(length=2)
stack.push(1)
stack.push(2)
stack.push(3) # raise pipe.stack.StackOverflow
stack.pop() # 2
stack.pop() # 1
stack.pop() # raise pipe.stack.StackUnderflow

queue=pipe.Queue(length=2)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3) # raise pipe.queue.Full
queue.dequeue() # 1
queue.dequeue() # 2
queue.dequeue() # raise pipe.queue.Empty
```
