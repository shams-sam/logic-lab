import java.util.ArrayList;

class LinkedList {
    Node head = null;
    class Node {
        int data;
        Node next;
        Node(int initData) {
            data = initData;
            next = null;
        }
    }

    public void push(int data) {
        Node new_node = new Node(data);
        new_node.next = head;
        head = new_node;
    }

    public int detectLoopWithSlowFastPointer(int useHash) {
        Node slowPointer = head;
        Node fastPointer = head;
        while (slowPointer != null &&
               fastPointer != null &&
               fastPointer.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
            if (slowPointer == fastPointer) {
                if (useHash != 1) {
                    breakLoopWithoutHash(slowPointer);
                }
                System.out.println("Loop Detected");
                return 1;
            }
        }
        System.out.println("Loop not detected");
        return 0;
    }

    public void breakLoop() {
            Node iterNode = head;
            ArrayList<Node> traversedNodes = new ArrayList<Node>();
            while (true) {
                traversedNodes.add(iterNode);
                if (traversedNodes.contains(iterNode.next) || iterNode.next == null) {
                    iterNode.next = null;
                    return;
                }
                iterNode = iterNode.next;
            }
    }

    public void breakLoopWithoutHash(Node loopNode) {
        Node startNode = head;
        Node endNode = null;
        while (true) {
            endNode = loopNode;
            while (endNode.next != loopNode && endNode.next != startNode) {
                endNode = endNode.next;
            }

            if (endNode.next == startNode) break;
            startNode = startNode.next;
        }
        endNode.next = null;
    }

    public void printList() {
        Node iterNode = head;
        while (iterNode != null) {
            System.out.println(iterNode.data);
            iterNode = iterNode.next;
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();
        list.push(1);
        list.push(2);
        list.push(3);
        list.push(4);
        list.detectLoopWithSlowFastPointer(1);
        list.head.next.next.next.next = list.head.next.next;
        list.detectLoopWithSlowFastPointer(1);
        list.breakLoop();
        list.detectLoopWithSlowFastPointer(1);
        list.head.next.next.next.next = list.head.next;
        list.detectLoopWithSlowFastPointer(0);
        list.detectLoopWithSlowFastPointer(1);
    }
}
