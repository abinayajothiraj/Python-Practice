# A Linked list is a linear data structure made up of nodes.
# Each node contains: Data and Pointer to the next node.
#This POINTER CONNECTION is the actual linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create Nodes:
node1=Node(11)
node2=Node(7)
node3=Node(3)

#connect Nodes:
node1.next = node2
node2.next = node3

#Print values manually:

print(node1.data)           #11
print(node1.next.data)      #7
print(node1.next.next.data) #3


"""
The advantage of linked list lies in updating and deleting in the middle or adding in the beginning when compared to arrays which O(N).
Accessing in Linked list is a drawback compared to arrays as we have to traverse the previous elements to get to the exact element.

"""

#Instead of calling manually, Traversal is being used.Traversal means visiting each node one by one in order.

#Traversal is the HEART of linked lists. Traversal means - keep moving automatically until end.
     # Repeatedly using . next automatically ,without knowing how many nodes exist.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create Nodes

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

#connect nodes

node1.next=node2
node2.next=node3
node3.next=node4

#Traversal:

current = node1 # current is a temporary variable ,to traverse the linked list without losing the head reference.

while current:
    print(current.data, end ="->")
    current = current.next  # move to the next connected node

print("None")


"""
Traversal allows:

i)Print all nodes
ii)Search nodes
iii)Modify nodea
iv)Count nodes
v)Reverse list
vi)Delete node
vii)Reverse list
viii)Insert node

"""

#eg3: Search for a value
current = node1
while current:
    if current.data == 20:
        print("Found")
    current = current.next

#eg4: Modify values using traversal

current = node1
while current:
    current.data += 5
    current = current.next

#eg5: count nodes

current = node1
count = 0
while current:
    count += 1
    current = current.next
print(count)

#eg5: Reverse linked list using traversal

#before: 10->20->30->40->None
#after:  40->30->20->10->None

"""prev = None
current = node1
while current:
    nextNode = current.next
    current.next = prev
    prev = current
    current = nextNode
head = prev"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to print linked list
def traverse(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4


# Original list
print("Before reverse:")
traverse(node1)


# Reverse linked list
prev = None
current = node1

while current:

    nextNode = current.next

    current.next = prev

    prev = current

    current = nextNode

# New head after reverse
head = prev
# Reversed list
print("\nAfter reverse:")
traverse(head)


#eg6:Delete a node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to print linked list
def traverse(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")


# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

print()
# Original list
print("Before deletion:")
traverse(node1)


# Delete node with value 30
current = node1

while current.next:

    if current.next.data == 30:
        current.next = current.next.next
        break

    current = current.next


# After deletion
print("\nAfter deletion:")
traverse(node1)

print()

#eg7: Insert node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to print linked list
def traverse(head):
    current = head

    while current:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(40)

# Connect nodes
node1.next = node2
node2.next = node3

# Original linked list
print("Before insertion:")
traverse(node1)

# Create new node
newNode = Node(50)

# Traversal to find insertion point
current = node1
while current.data != 20:
    current = current.next

# Insert 50 after 20
newNode.next = current.next
current.next = newNode

# After insertion
print("\nAfter insertion:")
traverse(node1)