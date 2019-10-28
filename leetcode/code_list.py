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

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''

        target_dict = {}
        for item in t:
            target_dict[item] = target_dict.get(item, 0) + 1
        min_len = 10000000000000
        slow = 0
        match_count = 0
        index = 0

        for fast in xrange(len(s)):
            current_item = s[fast]

            if current_item not in target_dict:
                continue

            item_need_count = target_dict[current_item]
            target_dict[current_item] = item_need_count - 1

            if target_dict[current_item] == 0:
                match_count = match_count + 1 # 本来需要，现在不需要了

            while match_count == len(target_dict):
                # find a valid substring
                if (fast - slow + 1) < min_len:
                    min_len = fast - slow + 1
                    index = slow # 记录上一个valid 开始的位置

                left_item = s[slow] # 从valid中去掉这个item
                slow = slow + 1 # 慢指针开始前移

                if left_item not in target_dict:
                    continue

                left_need_count = target_dict.get(left_item)
                target_dict[left_item] = left_need_count + 1

                if target_dict[left_item] > 0:
                    match_count = match_count - 1  # 本来不需要，现在需要了

        return s[index: index + min_len] if min_len else ''


if __name__ == '__main__':
   # print '----------->>>'
    #print Solution().permute(['1', '2', '3'])
    print Solution().minWindow('ADOBECODEBANC', 'ABC')
