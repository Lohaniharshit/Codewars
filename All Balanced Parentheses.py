"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]

"""


def balanced_parens(n):
    stack = []
    res = []

    def backtrack(left, right):
        if left == right == n:
            res.append("".join(stack))
        if left < n:
            stack.append("(")
            backtrack(left + 1, right)
            stack.pop()
        if right < left:
            stack.append(")")
            backtrack(left, right + 1)
            stack.pop()

    backtrack(0, 0)
    print(res)


balanced_parens(3)
