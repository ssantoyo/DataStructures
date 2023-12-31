class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def get_length(self):
        if self.head is None:
            print("Linked List is Empty")
            return -1
        
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked List is Empty")
            return -1
        
        itr = self.head
        llStr = ""
        while itr:
            if itr.next:
                llStr += str(itr.data) + "-->"
            else:
                llStr += str(itr.data) + "-->null"
            itr = itr.next
        print(llStr)
    
    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked List is Empty")
            return -1
        
        itr = self.get_last_node()
        llStr = ""
        while itr:
            if itr.prev:
                llStr += "null-->" + str(itr.data)
            else:
                llStr += "-->" + str(itr.data)
            itr = itr.prev
        print(llStr)

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def get_last_node(self):
        if self.head is None:
            return
        
        itr = self.head
        #tranverse through the entire linked list
        while itr.next:
            itr = itr.next
        #return last element
        return itr

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.get_last_node()
        
        itr.next = Node(data, None, itr.prev)

    def insert_at(self, index, data):
        #index out of bounds
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        #index is at the start of list
        if index == 0:
            self.insert_at_begining(data)
            return
        #Adding node anywhere else
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        #index out of bounds
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
       
        #index is at the start of list, skip to null 
        if index == 0:
            self.head = self.head.next
            return
        
        #removing node anywhere else
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    #create a linkedlist with a new array
    def insert_values_at_beginning(self, dataList):

        for data in dataList:
            self.insert_at_begining(data)
    
    #create a linkedlist with a new array
    def insert_values_at_end(self, dataList):

        for data in dataList:
            self.insert_at_end(data)
    
    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None: 
            print("Linked List is Empty")
            return

        #if the first element is a hit
        if self.head.data == data:
            #move to the second element
            self.head = self.head.next
            return 

        itr = self.head
        while itr.next:
            #any middle element is a hit
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            #there is no match
            itr = itr.next


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(2)
    ll.insert_at_begining(5)
    ll.insert_at_begining(20)
    ll.print_forward()
    ll.print_backward()
    print(ll.get_length())
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.insert_at(1,"blueberry")
    # ll.remove_at(2)
    # ll.print()

    # ll.insert_values([45,7,12,567,99])
    # ll.insert_at_end(67)
    # ll.print()