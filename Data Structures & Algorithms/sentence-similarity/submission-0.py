from typing import List

class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]]
    ) -> bool:
        
        # 1️⃣ Must be same length
        if len(sentence1) != len(sentence2):
            return False
        
        # 2️⃣ Build similarity set (bidirectional)
        similar = set()
        for w1, w2 in similarPairs:
            similar.add((w1, w2))
            similar.add((w2, w1))
        
        # 3️⃣ Compare word by word
        for w1, w2 in zip(sentence1, sentence2):
            if w1 == w2:
                continue
            if (w1, w2) not in similar:
                return False
        
        return True
        