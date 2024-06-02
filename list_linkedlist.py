class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while (current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("hato index")

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove_first_node(self):
        if (self.head == None):
            return

        self.head = self.head.next

    def remove_node(self, db):
        current_node = self.head

        if current_node.data == db:
            self.remove_first_node()
            return

        while (current_node != None and current_node.next.data != db):
            current_node = current_node.next

        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next


l_list = LinkedList()

a = Node(24)
b = Node(15)
c = Node(20)
d = Node(30)
e = Node(40)
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
print(l_list.printList())

# push
l_list.push(25)
l_list.push(89)
l_list.push(45)
l_list.push(90)
l_list.push(67)
print(l_list.printList())

# insert
l_list.insert(5, 1)
l_list.insert(8, 2)
print(l_list.printList())

# append
# data = []
#
# for i in range(10, 50, 2):
#     data.append(i)
#
# l_list.head = Node(data[0])
# for g in data[1:]:
#     l_list.append(g)
#
# print(data)

# remove
l_list.remove_node(5)
l_list.remove_node(8)
print(l_list.printList())
