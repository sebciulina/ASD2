import heapq
from heapq import heappop, heappush


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def buildHuffmanTree(text):
    if len(text) == 0:
        return

    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    while len(pq) != 1:
        left = heappop(pq)
        right = heappop(pq)

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    root = pq[0]

    huffmanCode = {}
    encode(root, '', huffmanCode)

    s = ''
    for c in text:
        s += huffmanCode.get(c)

    file = open("after.txt", "w")
    file.write(str(huffmanCode) + "\n")
    file.write(s)
    file.close()

    if isLeaf(root):
        while root.freq > 0:
            print(root.ch, end='')
            root.freq = root.freq - 1


def encode(root, s, huffman_code):
    if root is None:
        return

    if isLeaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.right, s + '1', huffman_code)


def isLeaf(root):
    return root.left is None and root.right is None


def createFile(s):
    file = open("before.txt", "w")
    file.write(s)
    file.close()
    file2 = open("before.txt", "r")
    text = file2.read()
    file2.close()
    return text


if __name__ == '__main__':
    s = "ACAABAB"
    buildHuffmanTree(createFile(s))
