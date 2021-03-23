import sys
sys.setrecursionlimit(10000)

preorder_list = []
postorder_list = []
class Node:
    def __init__(self, x,y,index):
        self.x = x
        self.y = y
        self.index = index
        self.right = None
        self.left = None

# 전위 순회 : root를 기준으로 왼쪽 서브트리 => 오른쪽 서브트리
def preorder(node):
    preorder_list.append(node.index)
    if node.left:
        preorder(node.left)
    if node.right:
        preorder(node.right)

# 후위순회 : 왼쪽 맨밑에서 시작, 왼쪽 서브트리 => 오른 서브트리
def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    postorder_list.append(node.index)

def solution(nodeinfo):
    nodeinfo = sorted([[x,y,idx+1] for idx, (x,y) in enumerate(nodeinfo)], key=lambda x:(-x[1],x[0]))
    print(nodeinfo)
    root_node = None
    for node in nodeinfo:
        if not root_node:
            # 1. 맨 처음에 root node를 생성
            root_node = Node(node[0],node[1],node[2])
        else:
            cur_node = root_node # 현재노드
            x, y, index = node[0],node[1],node[2]   # 다음 노드
            while True:
                # 2. cur_node와 다음 노드의 x값을 비교
                if cur_node.x > x:
                    # 3. cur_node의 x가 더 크면 왼쪽을 확인
                    if cur_node.left:
                        # 4. cur_node의 왼쪽이 존재하면 해당 노드를 cur_node로 할당
                        cur_node = cur_node.left
                        continue
                    else:
                        # 4. cur_node의 왼쪽이 존재안하면 왼쪽 노드 추가
                        cur_node.left = Node(x,y,index)
                        break
                elif cur_node.x < x:
                    if cur_node.right:
                        cur_node = cur_node.right
                        continue
                    else:
                        cur_node.right = Node(x,y,index)
                        break
                    break
    res = []
    preorder(root_node)
    postorder(root_node)
    res.append(preorder_list)
    res.append(postorder_list)
    return res

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))

#[[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]