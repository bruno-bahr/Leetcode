class Solution:
    def removeNthFromEnd(head:list, n: int):
        for i in range(len(head)):
            if i == n:
                head.remove(head[-n])
        return head

if __name__ == '__main__':
    head = [1,2,3,4,5]
    n = 2
    print(Solution.removeNthFromEnd(head, n))
