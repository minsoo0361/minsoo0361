def preorder_traverse(T):  # 전위순회
    if T:                  # T is not None
        visit(T)           # print(T.item)
        preorder_traverse(T.left)   #  부모노드, 왼쪽 자식, 오른쪽 자식
        preorder_traverse(T.right)


def inorder_traverse(T):   # 중위순회
    if T:
        inorder_traverse(T.left)   # 왼쪽 자식, 부모, 오른쪽 자식
        visit(T)
        inorder_traverse(T.right)

def post_order_traverse(T):   # 후위순회
    if T:
        inorder_traverse(T.left)
        inorder_traverse(T.right)# 왼쪽 자식, 오른쪽 자식, 부모
        visit(T)
        