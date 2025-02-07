class Codec:
    def serialize(self, root):
        parts = []
        def rec(root):
            if not root:
                parts.append("null")
            else:
                parts.append(str(root.val))
                rec(root.left)
                rec(root.right)
        rec(root)
        return ",".join(parts)
    
    def deserialize(self, data):
        treelist = data.split(",")
        self.index = 0
        def rec():
            if self.index >= len(treelist):
                return None
            val = treelist[self.index]
            self.index += 1
            if val is "null":
                return None
            node = TreeNode(int(val))
            node.left = rec()
            node.right = rec()
            return node
        return rec()
            