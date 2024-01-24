class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        rowS, rowE, colS, colE = 0, m, 0, n
        start, end = 0, m*n
        ans = [[-1]*n for i in range(m)]
        flag = False
        while start<end and head:
            # moving right
            if start<end:
                for i in range(colS, colE):
                    try:
                        ans[rowS][i] = head.val
                        head = head.next
                    except:
                        flag = True
                        break
                    start += 1
                rowS += 1
            if flag:
                break
            # moving down
            if start<end:
                for i in range(rowS, rowE):
                    try:
                        ans[i][colE-1] = head.val
                        head = head.next
                    except:
                        flag = True
                        break
                    start += 1
                colE -= 1
            if flag:
                break
            # moving left
            if start<end:
                for i in range(colE-1, colS-1, -1):
                    try:
                        ans[rowE-1][i] = head.val
                        head = head.next
                    except:
                        flag = True
                        break
                    start += 1
                rowE -= 1
            if flag:
                break
            # moving up
            if start<end:
                for i in range(rowE-1, rowS-1, -1):
                    try:
                        ans[i][colS] = head.val
                        head = head.next
                    except:
                        flag = True
                        break
                    start += 1
                colS += 1
            if flag:
                break
        return ans