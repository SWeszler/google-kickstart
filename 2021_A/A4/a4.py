from collections import defaultdict

def solution_bf(N, K, strings):
    pre = {}
    res = 0

    for s in strings:
        for i in range(len(s), 0, -1):
            if s[:i] in pre:
                pre[s[:i]] += 1
            else:
                pre[s[:i]] = 1

    for p, c in pre.items():
        res += c // K

    return res


  
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()
  

    def insert(self, word):
        node = self.root
        for char in word:
            new_node = node.children[char]
            new_node.count += 1
            node = new_node

        node.is_word = True
  

    def get_node(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        return node


    def search(self, word):
        node = self.get_node(word)
        return node != None and node.is_word


    def print_trie(self):
        self.print_trie_helper(self.root)


    def print_trie_helper(self, node):
        for k, n in node.children.items():
            print(k, n.count)
            self.print_trie_helper(n)



def solution_trie(N, K, strings):
    pre = Trie()

    for s in strings:
        pre.insert(s)

    queue = [pre.root]
    total = 0
    while queue:
        node = queue.pop(0)
        for k, n in node.children.items():
            total += n.count // K
            queue.append(n)

    return total


solution = solution_trie


tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    strings = []
    for j in range(int(N)):
        strings.append(input())

    out = solution(int(N), int(K), strings)
    print("Case #{}: {}".format(i, out))