# 递归
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		def dfs(root):
			if not root:
				return
			# 按照 左-打印-右的方式遍历	
			dfs(root.left)
			res.append(root.val)
			dfs(root.right)
		dfs(root)
		return res

# 迭代
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		stack = []
		while stack or root:
			# 不断往左子树方向走，每走一次就将当前节点保存到栈中
			# 这是模拟递归的调用
			if root:
				stack.append(root)
				root = root.left
			# 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
			# 然后转向右边节点，继续上面整个过程
			else:
				tmp = stack.pop()
				res.append(tmp.val)
				root = tmp.right
		return res

# 莫里斯遍历
class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		pre = None
		while root:
			# 如果左节点不为空，就将当前节点连带右子树全部挂到
			# 左节点的最右子树下面
			if root.left:
				pre = root.left
				while pre.right:
					pre = pre.right
				pre.right = root
				# 将root指向root的left
				tmp = root
				root = root.left
				tmp.left = None
			# 左子树为空，则打印这个节点，并向右边遍历	
			else:
				res.append(root.val)
				root = root.right
		return res