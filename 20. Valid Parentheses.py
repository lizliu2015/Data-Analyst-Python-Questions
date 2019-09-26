class Solution:
    def isValid(self, s):
        stack = [0]
        mapping = {0: None, '(':')', '[':']', '{':'}'}
        for c in s:
            if c in mapping: 
                stack.append(c)
            else:
                if mapping[stack.pop()] != c: return False
        return stack == [0]
###
1.创建一个字典，把反括号存为value,正括号存为key--
2.遍历这个字符串：
--判断是否为value:
如果存在
保存value，
如果不存在判断是否为Key，
若为Key:
>若直接输入反括号且stack=[] 返回false
>若这个key与stack弹出值不相等 返回false
不为key也不为value:
>false
3.遍历结束后，判断是否为空”如果直接输入[/{/( ，只循环一次就结束循环，且stack不为空 ，所以只能用stack判断“
