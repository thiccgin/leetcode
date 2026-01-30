class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        new_node = TreeNode(key, val)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = new_node
                    return
                curr = curr.right
            else:
                curr.val = val
                return
            
    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root
        if not curr:
            return -1

        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        curr = self.root
        if not curr:
            return -1
        
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.remover(self.root, key)
    def remover(self, root, key):
        if not root:
            return None
        
        if key > root.key:
            root.right = self.remover(root.right, key)
        elif key < root.key:
            root.left = self.remover(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.findMin(root.right)
                root.key = min_node.key
                root.val = min_node.val
                root.right = self.remover(root.right, root.key)
        return root
    def findMin(self, root):
        curr = root
        if not curr:
            return -1

        while curr.left:
            curr = curr.left
        return curr

    def getInorderKeys(self) -> List[int]:
        res = []
        self.inorderTraversal(self.root, res)
        return res
    def inorderTraversal(self, root, res: list):
        if not root:
            return
        
        self.inorderTraversal(root.left, res)
        res.append(root.key)
        self.inorderTraversal(root.right, res)
        
