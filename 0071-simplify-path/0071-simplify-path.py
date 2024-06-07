class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        stack = path.split('/')

        # 쓸데 없이 생긴 '' 제거하기
        while '' in stack:
            stack.remove('')

        stack2 = []
        skip = 0
        for i in range(len(stack)-1, -1, -1):
            if stack[i]=='.':
                continue
            elif stack[i]=='..':
                skip += 1
            elif skip>0:
                skip -= 1
            else:
                stack2.append(stack[i])

        stack2.reverse()

        return '/'+"/".join(stack2)