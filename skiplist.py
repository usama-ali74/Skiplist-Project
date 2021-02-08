import random


class Node:  # making a class Node with attributes
    def __init__(self, value=None, height=0):
        self.height = height  # height attribute store height of a node by pick_height func
        self.value = value  # value attribute store value of a node
        self.next = [None] * (height)  # In self.next we make a list to store address of the adjacent nodes.


class Skiplist:  # making a class to implement Skiplist data structure
    def __init__(self):
        self.counter = 0  # self.counter count the total no of nodes in the skip list
        self.maxHeight = 0  # self.maxHeight will store the maximum height of skiplist
        self.sentinel = Node(None, 0)  # self.sentinal is point from where we start traversing to the nodes.
        self.stack = [None for i in
                      range(100)]  # self.stack is used to store the pointer for adding the new nodes in skiplist
        self.sentinel.next.append(None)  # this line is use to insert None type in the sentinal

    def pick_height(self):  # func pick_height pick the height of the node when we adding in skiplist
        z = random.getrandbits(32)  # random.getrandbits() choose an integer in the specified size (in bits).
        k = 0  # Initialize total height of newnode with 0
        while z & 1:  # we run this loop until we get 1
            k = k + 1  # Update the height Var by increment 1
            z = z // 2  # divide value of z by 2
        return k

    def find_pred_node(self, x):  # In func find_pred_node we find the given element in our skiplist
        u = self.sentinel  # making a pointer for searching
        r = self.maxHeight  # store the maximum of height of skiplist
        while r >= 0:  # for searching the required node we run a while loop until we reach at base list
            while u.next[r] != None and u.next[
                r].value < x:  # In this line we also run a while loop with condition if the next node of skiplist should not be equal to None and value is is greater then the value of the skiplist
                u = u.next[r]  # go right in list r
            r = r - 1  # go down into list r-1
        return u

    def find(self, x):  # In this func we call find_pred_node func
        u = self.find_pred_node(x)  # In this varaible we store the output of find_pred_node func
        if u.next[0] == None:  # In this line we check the condition that if the u.next is None
            return None  # the return None
        elif u.next[0].value == x:  # In this condition we check if the required is found
            return u.next[0].value  # then return value

    def Add(self, x):  # Add func will add a node in the skiplist
        u = self.sentinel  # making a pointer for searching
        r = self.maxHeight  # store the maximum of height of skiplist
        while r >= 0:  # for searching the required node we run a while loop until we reach at base list
            while u.next[r] != None and u.next[
                r].value < x:  # In this line we also run a while loop with condition if the next node of skiplist should not be equal to None and value is is greater then the value of the skiplist
                u = u.next[r]  # go right in list r
            if u.next[r] != None and u.next[
                r].value == x:  # In this condition we check if the new node value is already in the list
                return False  # the return false
            self.stack[r] = u  # Storing pointer in the stack for new node
            r = r - 1  # go down into list r-1
        w = Node(x, self.pick_height())  # Make a new Node
        w.next.append(None)  # store None in w.next

        while self.maxHeight < w.height:  # this loop will run if the maxheight becomes less then to newnode's height
            self.maxHeight = self.maxHeight + 1  # In this we increment maxheight by 1
            self.sentinel.next.append(None)  # Also increases sentinel.next by appending None
            self.stack[self.maxHeight] = self.sentinel  # In this line we store sentinel in stack
        self.sentinel.height = self.maxHeight  # Update the sentinel height by maxheight

        for i in range(len(w.next)):  # In this loop we are connecting the pointers for newly added node
            w.next[i] = self.stack[i].next[i]  # In this line we connect the pointer with new node
            self.stack[i].next[i] = w  # connecting previous nodes to new node
        self.counter = self.counter + 1  # increment the total no of node by 1
        return True

    def remove(self, x):  # Remove func will remove the node in skiplist
        removed = False  # Intitalize the removed Var with false
        u = self.sentinel  # making a pointer for searching
        r = self.maxHeight  # store the maximum of height of skiplist
        while r >= 0:  # for searching the required node we run a while loop until we reach at base list
            while u.next[r] != None and u.next[
                r].value < x:  # In this line we also run a while loop with condition if the next node of skiplist should not be equal to None and value is is greater then the value of the skiplist
                u = u.next[r]  # go right in list r
            if u.next[r] != None and u.next[
                r].value == x:  # In this condition we check if the new node value is already in the list
                removed = True  # If element is removed then update removed Var true
                u.next[r] = u.next[r].next[r]  # disconecting links of  provided node
                if u == self.sentinel and u.next[r] == None:
                    self.maxHeight = self.maxHeight - 1  # height has decreased
            r = r - 1  # go down into list r-1
        if removed:
            self.counter = self.counter - 1  # Decriment the total no of node Var
        if self.maxHeight == -1 and self.sentinel.height >= 1:  # check if the maxheight is gone into -1 now update the heights
            self.maxHeight = 0  # Update maxheight
            self.sentinel.height = 0  # Update sentinel height
        while self.sentinel.height == 0 and len(
                self.sentinel.next) != 1:  # if lenght of sentinel is greater then 1 and height of sentinel is equal to 0 then
            self.sentinel.next.pop()  # In this line remove None from the sentinel.next
        return removed
