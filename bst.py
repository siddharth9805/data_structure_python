class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def add(self,data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insertion(self.root, data)

    def _insertion(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = TreeNode(data)
            else:
                return self._insertion(root.left, data)
        elif data> root.data:
            if root.right is None:
                root.right=TreeNode(data)
            else:
                self._insertion(root.right, data)
        return root

    def search(self,data):
        return self._search_word(self.root,data)

    def _search_word(self,root,data):
        if root is None:
            return

        if data<root.data:
            if root.left is None:
                return False
            else:
                return self._search_word(root.left,data)
        elif data>root.data:
            if root.right is None:
                return False
            else:
                return self._search_word(root.right, data)
        else:
            return True

    def inorder_traversal(self):
        self._inorder_traversal(self.root)

    def _inorder_traversal(self,root):
        if root:
            self._inorder_traversal(root.left)
            print(root.data,'->' , end=' ')
            self._inorder_traversal(root.right)

    def preorder_traversal(self):
        self._preorder_traversal(self.root)

    def _preorder_traversal(self,root):
        if root:
            print(root.data,'->' ,end=' ')
            self._preorder_traversal(root.left)
            self._preorder_traversal(root.right)

    def bst_check(self):
        self._bst_check(self.root)

    def _bst_check(self,root):
        if root is None:
            return None

        if root.left is None:
            if root.right and  root.data<root.right.data:
                flag=True
        elif root.right is None:
            if root.left and  root.data<root.left.data:
                flag=True
        elif root.left.data<root.data<root.right.data:
            flag=True
        else:
            return False

        self._bst_check(root.left)
        self._bst_check(root.right)
        return flag

    def postorder_traversal(self):
        self._postorder_traversal(self.root)

    def _postorder_traversal(self,root):
        if root:
            self._postorder_traversal(root.left)
            self._postorder_traversal(root.right)
            print(root.data,'->', end=' ')

    def delete(self,data):
        self.root=self._delete(self.root,data)

    def _delete(self, root, data):
        if root is None:
            return None

        # Traverse the tree to find the node to delete
        if data < root.data:
            root.left = self._delete(root.left, data)
        elif data > root.data:
            root.right = self._delete(root.right, data)
        else:
            if root.left is None or root.right is None:
                return root.left or root.right

            # Node with two children: Get the inorder successor
            temp = self._inorder_successor(root.right)

            # Copy the inorder successor's content to this node
            root.data = temp.data

            # Delete the inorder successor
            root.right = self._delete(root.right, temp.data)

        return root

    def _inorder_successor(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def bfs(self):
        if not self.root:
            return []
        queue = [self.root]  # Initialize queue with root node
        result = []  # List to store the traversal result
        while queue:
            current_node = queue.pop(0)  # Dequeue the front node from the queue
            if current_node is None:
                result.append(None)  # Append None for missing children
                continue  # Skip the rest of the loop for None values
            else:
                result.append(current_node.data)  # Process the current node

            # Check and enqueue left child, or enqueue None if no left child
            if current_node.left:
                queue.append(current_node.left)
            else:
                queue.append(None)  # Use None to represent missing left child

            # Check and enqueue right child, or enqueue None if no right child
            if current_node.right:
                queue.append(current_node.right)
            else:
                queue.append(None)  # Use None to represent missing right child

            # Early stopping condition to avoid infinite loop with None values
            if all(node is None for node in queue):
                break

        print(result)  # Optionally, return the result instead of printing


    def dfs(self):
        print(self._dfs_preorder(self.root))

    def _dfs_preorder(self,root):
        if not root:
            return []
        result = [root.data]
        result += self._dfs_preorder(root.left)
        result += self._dfs_preorder(root.right)
        return result

    def _common_ancistor(self,root,p,q):
        if p<root.data and q<root.data:
            return self._common_ancistor(root.left,p,q)

        if p>root.data and q>root.data:
            return self._common_ancistor(root.right,p,q)
        return root
    def distance_calculation(self,root,val,count):
        if root.data==val:
            return count

        if root.right and root.data<val:
            count+=1
            return self.distance_calculation(root.right,val,count)

        if root.left and root.data>val:
            count += 1
            return self.distance_calculation(root.left, val, count)
    def distance_between_nodes(self,p,q):
        root=self._common_ancistor(self.root,p,q)
        if p<q:
            left=p
            right=q
        else:
            left = q
            right = p
        return self.distance_calculation(root.left,left,1) + self.distance_calculation(root.right,right,1)


def main():
    bst=BST()
    bst.add(15)
    bst.add(10)
    bst.add(20)
    bst.add(8)
    bst.add(12)
    bst.add(25)
    bst.add(17)
    bst.add(19)

    # print("Found" if bst.search(int(input("Enter the number :"))) else "Not found")
    # bst.preorder_traversal()
    # print()
    # bst.delete(15)
    # bst.preorder_traversal()
    bst.bfs()
    # print(bst.distance_between_nodes(19,25))
    # bst.inorder_traversal()


if __name__=='__main__':
    main()