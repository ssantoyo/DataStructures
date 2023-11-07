from collections import deque

class Stack:
    def  __init__(self) -> None:
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def size(self):
        return len(self.container)
    
    def print_stack(self):
        print(self.container)
    
    def is_empty(self):
        return len(self.container) == 0
    
    def reverse_string(self, str):
        r_str = ""
        for i in str:
            self.push(i)
        while not self.is_empty():
            r_str += self.pop()
        return r_str
    
    def match(self, ch1, ch2):
        match_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        return match_dict[ch1] == ch2
    
    def is_balanced(self,str):
        for ch in str:
            if ch == '(' or ch == '[' or ch == '{':
               self.push(ch)
            if (ch == ")" or ch == ']' or ch == '}'):
                if self.is_empty():
                    return False

                if not self.match(ch, self.pop()):
                    return False
        return self.is_empty()





if __name__ == '__main__':
    s = Stack()
    # print(s.reverse_string("We will conquere COVID-19"))
    # s.print_stack()
    print(s.is_balanced("({a+b})"))
    print(s.is_balanced("))((a+b}{"))
    print(s.is_balanced("((a+b))"))
    print(s.is_balanced("((a+g))"))
    print(s.is_balanced("))"))
    print(s.is_balanced("[a+b]*(x+2y)*{gg+kk}"))
