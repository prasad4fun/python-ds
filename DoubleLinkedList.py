class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        temp = self.head
        print("\nTraversal in forward direction")
        while temp:
            print(temp.data)
            if not temp.next:
                break
            temp = temp.next

        print("\nTraversal in reverse direction")
        while temp:
            print(temp.data)
            temp = temp.prev

    def push(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
        new_node = Node(new_data)

        new_node.next = prev_node.next
        prev_node.next = new_node

        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        temp = self.head
        # if list is empty
        if not temp:
            self.head = new_node
            return

        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def delete_node(self, key):
        # if head or key is null, deletion is not possible
        if not self.head or not key:
            return
        # if del_node is the head node, point the head pointer to the next of del_node
        if self.head == key:
            self.head = key.next

        # if key is not last node, point the prev of node next to key to the previous of key
        if key.next:
            key.next.prev = key.prev
        # Change prev only if node to be deleted is NOT the first node
        if key.prev:
            key.prev.next = key.next

        # gc.collect()


if __name__ == "__main__":
    dll = DoubleLinkedList()

    # Let us create the doubly linked list 10<->8<->4<->2
    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)

    print("\n Original Linked List", end=' ')
    dll.print()

    dll.delete_node(dll.head)
    dll.delete_node(dll.head.next)
    dll.delete_node(dll.head.next)
    # Modified linked list will be NULL<-8->NULL
    print("\n Modified Linked List", end=' ')
    dll.print()
