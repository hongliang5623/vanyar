# -*- coding: utf-8 -*-

def largestRectangleArea(height):
    stack, i, area=[], 0, 0

    while i<len(height):
        print 'len(stack):%s, height[%s] :%s, stack:' % (
            len(stack), i, height[i]), stack
        last_s = stack[len(stack)-1] if stack else None
        print 'last_s:%s, area:%s' % (last_s, area)
        if stack==[] or height[i]>height[last_s]:
            print '压栈:height[%s]:%s height[last_s]:%s' % (
                i, height[i], height[last_s] if not last_s is None else None)
            stack.append(i)
        else:
            curr=stack.pop()
            width=i if stack==[] else i-last_s-1
            print '出栈：curr:%s, width:%s' % (curr, width)
            area = max(area, width*height[curr])
            i-=1
        i += 1
    print '------>>>>stack:', i, stack
    while stack != []:
        curr = stack.pop()
        last_s = stack[len(stack)-1] if stack else None
        print 'last_s:', last_s
        width = i if stack==[] else len(height)-last_s-1
        print '出栈：curr:%s, width:%s' % (curr, width)
        area = max(area, width*height[curr])
        print 'height[curr]', height[curr], area

    return area


if __name__ == '__main__':
    data = [1, 5, 6, 4]
    print 'data:', data
    result = largestRectangleArea(data)
    print result
