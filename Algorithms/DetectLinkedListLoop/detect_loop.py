class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        iter_node = self.head
        elem_list = []
        while(iter_node):
            elem_list.append(iter_node.data)
            iter_node = iter_node.next
        print elem_list

    def detect_loop_using_hash(self):
        iter_node = self.head
        visited_nodes = []
        while (iter_node):
            if iter_node in visited_nodes:
                print "Loop Detected using Hashing"
                return
            else:
                visited_nodes.append(iter_node);
            iter_node = iter_node.next
        print "Loop Not Found Using Hashing"

    def detect_loop_using_slow_fast(self):
        slow_pointer = self.head
        fast_pointer = self.head
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if (slow_pointer == fast_pointer):
                print "Loop Detected using Slow Fast"
                return
        print "Loop Not Detected using Slow Fast"


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.push(10)
    linked_list.push(20)
    linked_list.push(30)
    linked_list.push(40)
    linked_list.print_list()
    linked_list.detect_loop_using_hash()
    linked_list.detect_loop_using_slow_fast()
    linked_list.head.next.next.next = linked_list.head.next
    linked_list.detect_loop_using_hash()
    linked_list.detect_loop_using_slow_fast()

