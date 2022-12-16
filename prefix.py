

class Solution(object):
    def commonprefix(strs):
        if not strs:
            return'""'
        first_word =strs[0]
        for i in range(len(first_word)):
            for j in range(1, len(strs)):
                if strs[j][i] == first_word[i]:
                    continue
                else:
                    return first_word[:i]
        return first_word



if __name__ == '__main__':

    strs = ['boe', 'ball']
    print(strs)
    print(Solution.commonprefix(strs))


