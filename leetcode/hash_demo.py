# -*- coding: utf-8 -*-


def longestPalindrome(s):
        """
        :type s: str
        :rtype: int
        """
        hash_s = set()
        for i in s:
            if i not in hash_s:
                hash_s.add(i)
            else:
                hash_s.remove(i)
        print len(s), hash_s, len(hash_s)
        return len(s) - len(hash_s) + 1 if len(hash_s) > 0 else len(s)


print longestPalindrome('geeksskeeg')

