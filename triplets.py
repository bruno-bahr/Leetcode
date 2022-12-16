class Solution:
    def threeSum(nums:int):
        list = []
        for i in range(len(nums) - 2):
            for j in range(1, len(nums) - 1):
                if i >= j:
                    continue
                for k in range(2, len(nums)):
                    if j >= k:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        s = ([nums[i],nums[j],nums[k]])
                        if s not in list:
                            list.append(s)
        print(list)
        result = []
        if len(list) == 1:
            result.append([list])
            return list
        elif len(list) == 2:
            if sorted(list[0]) == sorted(list[1]):
                result.append(list[0])
                return result
            else:
                result.append(list)
                return result
        elif len(list) >= 3:
            result.append(sorted(list[0]))
            for i in range(len(list)-1):
                for j in range(1, len(list)):
                    if sorted(list[i]) != sorted(list[j]):
                        if not sorted(list[i]) in result:
                            result.append(sorted(list[i]))
                        if not sorted(list[j]) in result:
                            result.append(sorted(list[j]))

        return result



if __name__ == '__main__':
    nums = [0,1,-1,2,-3,0]
    #nums = [0, 0, 0,0]
    print(Solution.threeSum(nums))

