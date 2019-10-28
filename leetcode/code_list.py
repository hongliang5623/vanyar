# -*- coding: utf-8 -*-

from datetime import datetime


class Solution(object):
   # 152. Maximum Product Subarray
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = nums[0]
        max_temp = nums[0]
        min_temp = nums[0]
        for index, item in enumerate(nums):
            if index == 0:
                continue
            a = max_temp * item
            b = min_temp * item
            max_temp = max(max(a, b), item)
            min_temp = min(min(a, b), item)
            result = max(result, max_temp)
        return result


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs_num = 0

        def dfs(nums, temp):
            if len(temp) == len(nums):
                print 'got it:', temp
                self.res.append(temp[:])

            self.dfs_num += 1
            for i in xrange(len(nums)):

                if nums[i] in temp:
                    continue

                current_item = nums[i]
                print 'currnet temp:', temp, self.dfs_num, current_item

                temp.append(nums[i])
                dfs(nums, temp)
                print 'before pop temp:', temp, self.dfs_num, current_item
                temp.pop()

                print 'after pop temp:', temp, self.dfs_num, current_item

        dfs(nums, [])
        return self.res


if __name__ == '__main__':
    print 'gggggg----------->>>'
    print Solution().permute(['1', '2', '3'])
