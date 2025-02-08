import Spaceship

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def __str__(self):
        return str(self.head)
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    def del_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    def del_last(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    def insertatindex(self, value, index):
        if index == 0:
            mylinkedlist.prepend(value)
        elif index > self.length:
            return "Index out of bounds."
        elif index == self.length:
            mylinkedlist.append(value)
        else:
            new_node = Node(value)
            temp1 = self.head   # index before new value
            temp2 = self.head   # index after new value
            for i in range(index - 1):
                temp1 = temp1.next
            for i in range(index):
                temp2 = temp2.next
            temp1.next = new_node
            new_node.next = temp2
            self.length += 1
            return True
    def deleteatindex(self, index):
        if index == 0:
            mylinkedlist.del_first()
        elif index > self.length - 1:
            return "Index out of bounds."
        elif index == self.length - 1:
            mylinkedlist.del_last()
        else:
            temp1 = self.head
            temp2 = self.head
            for i in range(index):
                temp1 = temp1.next
            for i in range(index - 1):
                temp2 = temp2.next
            temp2.next = temp2.next.next
            return temp1
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


# TODO : Write function insertatindex to insert a new node at any given index. Consider all edge cases, including missing nodes.
# TODO : Write function deleteatindex to delete a new node at any given index. Consider all edge cases, including missing nodes.
# Make sure to reuse existing function for the correct edge cases for both TODOs
# Write appropriate test function below to test for the new functions.

s1 = Spaceship.Spaceship("Voyager", 300)
s2 = Spaceship.Spaceship("Enterprise", 300)
s3 = Spaceship.Spaceship("Atlantis", 300)
s4 = Spaceship.Spaceship("Challenger", 300)
s5 = Spaceship.Spaceship("Artemis", 300)

mylinkedlist = LinkedList(s1)
mylinkedlist.append(s2)
mylinkedlist.append(s3)
mylinkedlist.prepend(s4)
mylinkedlist.prepend(s5)
mylinkedlist.print_list()
print("")

mylinkedlist.deleteatindex(2)
s6 = Spaceship.Spaceship("Alma",300)
mylinkedlist.insertatindex(s6,3)

mylinkedlist.print_list()