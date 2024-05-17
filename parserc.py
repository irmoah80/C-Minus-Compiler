import parsetable


class Parser():
    def __init__(self) -> None:
        global token_branch , token
        pass

    def get_tbranch(self , token:str):
        parsetable.RHS_get(token)
        pass

    def settoken(tk):
        global token
        token = tk
    
    def setlookahead(lk):
        global lookahead
        lookahead = lk

    def anytree_handler(self):
        pass

    def is_match(self):
        #lookahead is a rightnow token , while token is pervious one
        global token_branch , 
        token_branch = self.get_tbranch(token)
        for i in token_branch:
            pass
        