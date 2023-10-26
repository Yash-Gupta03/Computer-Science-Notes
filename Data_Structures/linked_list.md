# Basics 

### Definition

It is a linear data structure where elements are not stored at contiguous memory locations. It is stored in nodes which are connected to each other with the help of pointers.

### Node creation 

> Node is a object having properties value and next, so create a class with constructor function and set value and next properties, then use it to create node.

```python
class Node:
    def __init__(self, a):
        self.value = a
        self.next = None

node = Node(10)

print(node.value)
```


### Insert Node in the beginning

```python

head = None

def insert_begin(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node
    
head = insert_begin(head, val)
```

### Print entire linked list

```python
def display(head):
    itr = head
    while itr != None:
        print(itr.value)
        itr = itr.next
        
display(head)
```

### Insert in the end

```python
def insert_end(head, val):
    itr = head
    while itr.next != None:
        itr = itr.next
    
    new_node = Node(val)
    itr.next = new_node
```

### Insert in the middle

```python
def insert_middle(head, val):
    itr = head
    while itr.value != 40:
        itr = itr.next
    
    new_node = Node(val)
    new_node.next = itr.next
    itr.next = new_node
    
insert_middle(head, 45)
``` 

### Delete from the beginning

```python
def delete_start(head):
    head = head.next
    return head
```

### Delete from the middle

```python
def delete_middle(head):
    count = count_nodes(head)
    count = count // 2
    itr = head
    while count-1:
        itr = itr.next
        count-=1
    itr.next = itr.next.next


def count_nodes(head):
    itr = head
    count = 0
    while itr:
        itr = itr.next
        count+=1
    return count

```


### Delete from the end

```python
def delete_end(head):
    itr = head
    while itr.next.next != None:
        itr = itr.next
    itr.next = None

```

## LeetCode Easy Questions

1. Delete given node in a linked list

```python
def deleteNode(self, node):
        itr = node.next
        node.val = itr.val
        node.next = node.next.next
```

2. Remove Nth node from end of list

```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        itr = head
        while itr:
            itr = itr.next
            count+=1
        
        if count == 1:
            head = None
            return head
        
        del_count = count-n
        
        if del_count == 0:
            return head.next
        
        itr = head
        while del_count > 1:
            itr = itr.next
            del_count-=1
        
        itr.next = itr.next.next
        
        return head
```

