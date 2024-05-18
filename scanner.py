from typing import List
import string as s
from pprint import pprint

# ------------------ impl 

ID           = "ID"
KEYWORD      = "KEYWORD"
PUNCH        = "PUNCH"
NUM          = "NUM"
SYMBOL       = "SYMBOL"
WORD         = "WORD"
EOF          = "EOF"
COMMENT      = "COMMENT"


class Lexer:
    def __init__(self, content: str) -> None:
        self.content = content + '\0'

        self.i = 0
        self.len = len(self.content)
        self.end = self.len - 1
    
    @property
    def ch(self):
        return self.content[self.i]

    @property
    def nch(self):
        return self.content[self.i+1]


    def next_till_end(self):
        return range(self.i + 1, self.len)

    def till_end(self):
        return range(self.i, self.len)

    def skip_whitespace(self):
        for j in self.till_end():
            ch = self.content[j]
            if ch not in s.whitespace:
                self.i = j 
                return


    def kind1(self):
        """
        should be called after skip_whitespace 
        """
        if   self.ch in ";,.{}()[]+-/*%'\"=" : return SYMBOL
        elif self.ch in s.digits:              return NUM
        elif self.ch in s.ascii_letters + '_': return WORD
        elif self.ch == '\0'                 : return EOF
        else: raise KeyError(f"LEX err character '{self.ch}'") 

    def lex_char(self):
        res = self.ch
        self.i += 1
        return res

    def lex_number(self):
        """
        currently only parser integer
        """
        for j in self.next_till_end():
            if self.content[j] not in s.digits:
                res = self.content[self.i:j]
                self.i = j
                return res

    def lex_word(self):
        for j in self.next_till_end():
            if self.content[j] not in s.ascii_letters + s.digits:
                res = self.content[self.i:j]
                self.i = j
                return res

    def lex_comment(self):
        last_was_star = False
        for j in self.next_till_end():
            ch = self.content[j]
            if ch == '*':
                last_was_star = True
            
            elif ch == '/' and last_was_star:
                cmt = self.content[self.i:j+1]
                self.i = j + 1
                return cmt

            elif ch == '\0':
                raise "you did not close you comment"
            
            else:
                last_was_star = False

    def lex1(self):
        k = self.kind1()
        val = None

        if   k == SYMBOL: 
            if self.ch == '/' and self.nch == '*':
                val = (COMMENT, self.lex_comment())
            else:
                val = (k, self.lex_char())

        elif k == NUM:    val = (k, self.lex_number())
        elif k == WORD:   val = (k, self.lex_word())
        elif k == EOF:    val = (EOF, None)
        else: raise "How is that even possible? from"

        return val

    def step1(self):
        self.skip_whitespace()
        return self.lex1()

    def lex(self) -> List[str]:
        acc = []
        while True:
            token = self.step1()
            if (token[0] == EOF):
                return acc
            else:
                acc.append(token)

# ------------------ utils 

def read_file(path):
    with open(path, 'r') as f:
        return f.read()

# ------------------ test 

if __name__ == "__main__":
    l = Lexer(read_file("./my_sample.txt"))
    pprint(l.lex())
