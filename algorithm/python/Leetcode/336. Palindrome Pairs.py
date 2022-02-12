import collections
from typing import *

# 트라이 저장할 노드
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.word_idx = -1
        self.word_tmps = [] # 서칭중 지나간 단어를 제외한 나머지 단어셋을 저장
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def is_palindrome(self, word) -> bool:
        return word[::] == word[::-1]

    # 단어 삽입
    def insert(self, idx, word):
        word = word[::-1]
        tmp = word[:]
        node = self.root
        for ch in word:
            node = node.child[ch]
            tmp = tmp[1:]
            node.word_tmps.append([tmp, idx])
        node.word_idx = idx

    def search(self, idx, word) -> List[List[int]]:
        node = self.root
        tmp = []
        for i, ch in enumerate(word):
            if ch not in node.child:
                return tmp
            node = node.child[ch]
            if node.word_idx != -1: # trie에 저장된 단어를 찾음
                if len(word)-1 == i: # 1번경우, trie에 저장된 단어 = 입력된 단어를 정확히 뒤집은 단어
                    if idx != node.word_idx: # 같은 단어 중복해서 쓰면안된다
                        tmp.append([idx, node.word_idx])
                elif len(word)-1 > i: # 2번경우, word1 + word2에서 word1의 나머지부분이 펠린드롬인지 판단
                    if self.is_palindrome(word[i+1:]):
                        tmp.append([idx, node.word_idx])
                        

        for word_tmp in node.word_tmps: # 3번경우, word1 + word2에서 word2의 나머지 부분이 펠린드롬인지 판단
            if self.is_palindrome(word_tmp[0]):
                if [idx, word_tmp[1]] not in tmp and idx != word_tmp[1]: # 예외 처리
                    tmp.append([idx, word_tmp[1]])
                
        return tmp

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # word1 + word2 가 펠린드롬인지 판단하는 3경우 (input : word1 기준, -word는 word를 뒤집은 값이라고 가정)
        # 1. -word2가 word인 경우  펠린드롬
        # 2. -word2 전체가 word1의 첫 부분 부터 부분집합이며 word1에서 -word2를 뺀부분이 펠린드롬이면 펠린드롬
        # ex) -word2 : abc word1 : abceee -> 펠린드롬
        # 3. word1 전체가 -word2의 첫 부분 부터 부분집합이며 -word2에서 word1을 뺀부분이 펠린드롬이면 펠린드롬
        # ex) word1 : abc -word2 : abceee
        trie = Trie()
        res = []
        
        for idx, word in enumerate(words):
            trie.insert(idx, word)
        
        for idx, word in enumerate(words):        
            if not word: # word가 ''이되고 더할 단어가 펠린드롬이면 펠린드롬이 된다
                for i, w in enumerate(words):
                    if trie.is_palindrome(w) and idx != i:
                        res.append([idx, i])
                        res.append([i, idx])
                continue
            res += trie.search(idx, word)

        return res
            
            
            
            
            
            
            
            
            
            
            