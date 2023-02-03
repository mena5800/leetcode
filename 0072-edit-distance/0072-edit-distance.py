import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mat = np.array([[0] * (len(word1)+1)]*(len(word2)+1))
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0:
                    mat[i][j] = j
                if j == 0:
                    mat[i][j] = i

        for i in range(1, len(mat)):
            for j in range(1, len(mat[0])):
                score1 = mat[i-1][j] + 1
                score2 = mat[i][j-1] + 1
                if word1[j-1] == word2[i-1]:
                    score3 = mat[i-1][j-1]
                else:
                    score3 = mat[i-1][j-1] + 1
                mat[i][j] = min(score1, score2, score3)
        return mat[-1][-1]