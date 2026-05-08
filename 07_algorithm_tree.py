##이진트리
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
    def set_left(self, left):
        self.left = left
    def set_right(self, right):
        self.right = right
my_tree = TreeNode('A', None, None)
new_node = TreeNode('B', None, None)
my_tree.set_left(new_node)
new_node = TreeNode('C', None, None)
my_tree.set_right(new_node)

cur_node = my_tree.left #node B 객체 (주소)
new_node = TreeNode('D', None, None)
cur_node.set_left(new_node)
new_node = TreeNode('E', None, None)
cur_node.set_right(new_node)

cur_node = my_tree.right #node C 객체 (주소)
new_node = TreeNode('F', None, None)
cur_node.set_left(new_node)