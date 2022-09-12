class InToPostFix:
    open = "("
    close = ")"

    def __init__(self, exp):
        self.exp = exp
        self.stack = []

    def push(self, itm):
        return self.stack.append(itm)

    def pop(self):
        return self.stack.pop()

    def priority(self, char):
        dct = {0: ["("], 1: ["+", "-"] , 2: ["/", "*"]}
        for p in dct:
            if char in dct[p]:
                return p

    def get_post_fix(self):
        for char in self.exp:
            if char.isalnum():
                print(char)
            elif char == InToPostFix.open:
                self.stack.append(char)
            elif char == InToPostFix.close:
                x = ""
                while x != "(":
                    x = self.stack.pop()
                    if x != "(": print(x)
            else:
                while self.priority(self.stack[-1]) >= self.priority(char):
                    print(self.stack.pop())
                self.stack.append(char)
        while len(self.stack) != 0:
            print(self.stack.pop())


if __name__ == "__main__":
    exp_str = "(2*3+4*(5-6+2))"
    exp = InToPostFix(exp_str)
    exp.get_post_fix()  # 23*456-2+*+

