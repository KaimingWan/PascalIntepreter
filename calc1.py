import pdb
'''该程序用于处理个位数的加法'''


# EOF标记用于说明没有更多的内容需要此法分析器来分析
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'


class Token(object):  # Token表示一个对<类型,值>例如表达式"3+5"中的3对应的token是<3,INTEGER>

    def __init__(self, type, value):  # 初始化的内容包括类型和值
        self.type = type
        self.value = value

    def __str__(self):  # 输出实例本身时的输出信息
        return 'Token({type},{value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text):  # text指整个表达式比如"3+5"
        self.text = text
        self.pos = 0  # 记录指针的位置，用于分析text
        self.current_token = None  # 记录当前的token比如"3"

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        '''完成词法分析器的功能， 将完整的text分隔成多个tokens'''
        text = self.text
        if self.pos > len(text) - 1:  # 如果指针位置到末尾了
            return Token(EOF, None)

        current_char = text[self.pos]

        # 如果没到末尾，判断是否是数字，是数字则返回对应的Token
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        # 如果是符号
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        '''该方法用于计算表达式,判断实际的token与预期的token_type的类型是否相等'''
        # pdb.set_trace()
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''计算表达式例如：INTEER PLUS INTEGER'''
        # pdb.set_trace()
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)  # 预期输入的第一个token是数字

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        # 此时的current_token变成EOF，可以返回结果
        result = left.value + right.value
        return result


def main():
    while True:
        try:
            text = input('calc>')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
