class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        # if self is empty
        if not temp:
            self.head = new_node
            return

        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head
        # if head is key to be removed
        if temp.data == key:
            self.head = temp.next
            temp = self.head
            # return

        while temp.next:
            if temp.next.data == key:
                temp.next = temp.next.next
                continue
            temp = temp.next


if __name__ == "__main__":
    llist = LinkedList()

    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)
    llist.insert_after(llist.head.next, 8)
    llist.insert_after(llist.head.next, 8)
    llist.append(8)
    llist.push(8)
    llist.print()
    llist.delete_node(8)
    llist.print()
