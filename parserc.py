import parsetable
import scanner

class Parser():
    def __init__(self) -> None:
        global token_branch , token , lookahead
        global Scanner
        Scanner = scanner.Scanner('input.txt')
        pass

    def get_tbranch(self , token:str):
        global token_branch
        token_branch = parsetable.RHS_get(token)
        pass

    # def settoken(tk):
    #     global token
    #     token = tk
    
    # def setlookahead(lk):
    #     global lookahead
    #     lookahead = lk

    def anytree_handler(self):
        pass

    def is_match(self , tk , lk):
        #lookahead is a rightnow token , while token is pervious one
        global Scanner
        token_branch = self.get_tbranch(tk)
        if lk in token_branch:
            #pass to compiler to go next
            lookahead = Scanner.getnexttoken()
            Pr = Parser()
            Parser.is_match(lk , lookahead)
            

        