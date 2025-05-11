class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
        
    
    def insertAtBegining(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAtEnd(self,data):
        node = Node(data)
    
        if self.head is None:
            '''
            in this condition we are checking if the head is none i.e if the first position is none 
            the make the data to first node
            '''
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            '''
            in this loop we iterate with the head's next pointer if head.next is not null
            untill then run the loop, and inside the loop change the head of linked list
            so that we can check if the next is null or not and when next is null loop will
            end then we assign new node to the next. and by default last node's next will be empty.
            '''
            itr = itr.next
        itr.next = node
        return
    
    def insert_multiple_values(self, lst):
        
        if len(lst) == 0:
            print("Give atleast one data")
            return
        
        for i in lst:
            self.insertAtEnd(i)
        return
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            count +=1
            itr = itr.next
            
            
        return count
        
        
    def remove_at(self, index):
        if self.head is None:
            return
        
        if index < 0 or index >= int(self.get_length()):
            raise Exception("invalid index")
            return
        
        if index == 0:
            self.head = self.head.next
            
        itr = self.head
        ind_count = index
        
        while ind_count != 0:
            ind_count -= 1
            itr = itr.next
            
            if ind_count == index-1:
                itr.next = itr.next.next
                break
        
        itr = itr.next
    
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insertAtBegining(data)
            return
    
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                return
            itr = itr.next
            count += 1


        
        
        
        
    
    def printLL(self):
        if self.head is None:
            print("No data in linked list....")
            return
            
        itr = self.head
        itr_list = ''
        while itr:
            itr_list += str(itr.data) + "-->"
            itr = itr.next
            
            
        print(itr_list)
        
    
            
    
    

obj1 = LinkedList()

# obj1.insertAtBegining('a')
# obj1.insertAtBegining('b')
# obj1.insertAtBegining('c')
# obj1.insertAtEnd("#A")
# obj1.insertAtEnd("#B")
# obj1.insertAtEnd("#C")

obj1.insert_multiple_values([1,2,3,4,5,6,7,8,9])
# obj1.get_length()
# obj1.remove_at(4)
obj1.insert_at(0,'a')

obj1.printLL()


