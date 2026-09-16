class TrieNode:
    def __init__(self):
            self.children = {}
            self.is_end = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not str:
            return ""

        root = TrieNode()    

        # Step 1: Build the Trie/Trie insert word
        for word in strs:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char] 
            node.is_end = True       

        # Step 2: Walk down the single shared path 
        prefix =[]
        node = root

        while len(node.children) == 1 and not node.is_end:
            char, next_node = next(iter(node.children.items()))   

            prefix.append(char)
            node = next_node  
        return "".join(prefix)    

        