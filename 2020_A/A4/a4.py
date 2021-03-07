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
        self.children = [None] * 26
        self.is_word = False
        self.value = 1


class Trie:

    def __init__(self):
        self.root = TrieNode()


    def char2index(self, char):
        return ord(char) - ord('A')
  

    def insert(self, key):
        curr = self.root
        for level in range(len(key)):
            index = self.char2index(key[level])
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.is_word = True
  

    def get_node(self, key):
        curr = self.root
        for level in range(len(key)):
            index = self.char2index(key[level])
            if not curr.children[index]:
                return None
            curr = curr.children[index]
        return curr


    def search(self, key):
        curr = self.get_node(key)
        return curr != None and curr.is_word
 


def solution_trie(N, K, strings):
    pre = Trie()

    for s in strings:
        for i in range(len(s), 0, -1):
            if pre.search(s[:i]):
                node = pre.get_node(s[:i])
                node.value += 1
            else:
                pre.insert(s[:i])

    def helper(root):
        if root == None:
            return 0
        
        total = 0
        for child in root.children:
            if child != None and child.is_word:
                total += child.value // K
            total += helper(child)

        return total

    return helper(pre.root)


solution = solution_trie


tc = int(input())
for i in range(1, tc + 1):
    N, K = input().split()
    strings = []
    for j in range(int(N)):
        strings.append(input())

    out = solution(int(N), int(K), strings)
    print(f"Case #{i}: {out}")