# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
        

class MyLinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >=self.size:
            return -1
        curr=self.head
        for i in range(index):
            curr=curr.next
        
        return curr.val
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            curr=self.head

            while curr.next:
                curr=curr.next
            curr.next=new_node
        self.size+=1
            
        
    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)