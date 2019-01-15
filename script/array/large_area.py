# -*- coding: utf-8 -*-


def largestRectangleArea(heights):
    n = len(heights)

    # left[i], right[i] represent how many bars are >= than the current bar
    print 'len:', n, heights
    left = [1] * n
    right = [1] * n
    max_rect = 0

    # calculate left
    for i in range(0, n):
        j = i - 1
        while j >= 0:
            if heights[j] >= heights[i]:
                left[i] += left[j]
                j -= left[j]
            else: break

    print left

    # calculate right
    for i in range(n - 1, -1, -1):
      j = i + 1
      while j < n:
          if heights[j] >= heights[i]:
              right[i] += right[j]
              j += right[j]
          else: break

    print right

    for i in range(0, n):
      max_rect = max(
          max_rect,
          heights[i] * (left[i] + right[i] - 1))

    return max_rect


if __name__ == '__main__':
    data = [1, 5, 6, 4]
    result = largestRectangleArea(data)
    print result
