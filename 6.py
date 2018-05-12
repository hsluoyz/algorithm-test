def lca(self, root, p, q):
    if not root:
        return None, 0, 0

    l0, l1, l2 = self.lca(root.left, p, q)
    if l0:
        return l0, l1, l2
    r0, r1, r2 = self.lca(root.right, p, q)
    if r0:
        return r0, r1, r2

    m1 = 1 if root == p else 0
    m2 = 1 if root == q else 0
    if l1 | r1 | m1 and l2 | r2 | m2:
        return root, 1, 1
    else:
        return None, l1 | r1 | m1, l2 | r2 | m2


def get_lca(self, root, p, q):
    r0, r1, r2 = self.lca(root, p, q)
    return r0
