class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return
        
        current = self.root
        
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            elif data > current.data:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
                
    def search(self,data):
        current = self.root

        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False


bst = BinaryTree()

bst.insert(5)
bst.insert(2)
bst.insert(8)
bst.insert(1)
bst.insert(3)

print(bst.search(5))
print(bst.search(3)) 
print(bst.search(11))