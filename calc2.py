import pdb
'''该程序用于处理多位数的加减法'''


# EOF标记用于说明没有更多的内容需要此法分析器来分析
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


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

    def isOp(self, text):
        '''用于判断是否是操作符'''
        if text == '+' or text == '-':
            return True
        else:
            return False

    def get_next_token(self):
        '''完成词法分析器的功能， 将完整的text分隔成多个tokens'''
        text = self.text
        length = len(text)  # 字符总长度
        if self.pos > length - 1:  # 如果指针在末尾(pos从0开始)
            return Token(EOF, None)
        current_char = text[self.pos]
        if self.isOp(current_char):
            if current_char == '+':
                token = Token(PLUS, current_char)
                self.pos += 1
                return token
            if current_char == '-':
                token = Token(MINUS, current_char)
                self.pos += 1
                return token

        s = ''
        while True:  # 如果没到末尾，判断是否是数字，是数字则继续移动指针直到遇到操作符获取整个数字
            if current_char.isdigit():  # 如果是数字
                s += current_char  # 如果是数字则追加到list
                self.pos += 1  # 移动指针，之后的判断都是对pos+1后的位置的值进行判断
            # 遇到符号要计算整个INTEGER的值
            if self.isOp(current_char):    # 如果是符号，则把之前记录下来的一串字符作为Token返回
                # 将list先转化成str再转化成int的整数
                # pdb.set_trace()
                token = Token(INTEGER, int(s))
                return token
            # 遇到最后个数字要计算整个INTEGER的值
            if self.pos > length - 1:  # 如果指针在末尾(pos从0开始)
                token = Token(INTEGER, int(s))
                return token

            else:
                current_char = text[self.pos]  # 重新获取下一个字符
                continue
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

        op = self.current_token.value
        if op == '+':
            self.eat(PLUS)
        elif op == '-':
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        # self.current_token = self.get_next_token()
        # self.eat(EOF)

        # 此时的current_token变成EOF，可以返回结果
        result = 0
        if op == '+':
            result = left.value + right.value
            return result
        if op == '-':
            result = left.value - right.value
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
