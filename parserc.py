import parsetable
import scanner
from anytree import Node, RenderTree

class Parser():
    def __init__(self) -> None:
        global token_branch , ch0 , ch , count
        global Scanner
        count = 0
        Scanner = scanner.Scanner('input.txt')
        ch = Scanner.getnexttoken()
        ch0 = Node("Program")
        pass

    def get_tbranch(self , token:str):
        global token_branch
        return parsetable.RHS_get(token)

    def anytree_handler(self , keyword:str , subroot):
        l_ch = "ch" + str(subroot)
        f_ch = "ch" + str(subroot+1)
        globals()[f_ch] = Node(keyword , parent= globals()[l_ch])
        pass

    def isterminal(token):
        if parsetable.IS_terminal(token):
            return True
        else:
            return False

    def printer(slf):
        global ch0
        print(RenderTree(ch0))

    def getnexttoken(self):
        global Scanner
        return Scanner.getnexttoken()


    def is_match(self , tk='Program' , lk =  None):
        #"lookahead" is the current token , while "token" is pervious one
        if lk == None:
            global ch
            lk = ch
        global Scanner , token_branch , count
        sub_id = count
        print(tk +'----')
        token_branch = self.get_tbranch(tk)
        if token_branch == None:
            token_branch = tk.split()
        Pr = Parser()
        for i in range(len(token_branch)):
            buff = token_branch[i].split()
            if len(buff) > 1:
                for j in buff:
                    if lk in buff and self.isterminal(lk):
                        #pass to compiler to go next
                        lookahead = Scanner.getnexttoken()
                        if lookahead == -1:
                            return -1
                        self.anytree_handler("(%s , %s)" % (lk[0] , lk[1]) , sub_id)
                        #track back to top branch
                        break
                    self.anytree_handler("%s" % (j) , sub_id)
                    l = Pr.is_match(token_branch[i] , lk)
                    if l == -1 :
                        return -1
                    pass
            if lk in token_branch and self.isterminal(lk):
                #pass to compiler to go next
                lookahead = Scanner.getnexttoken()
                if lookahead == -1:
                    return -1
                self.anytree_handler("(%s , %s)" % (lk[0] , lk[1]) , sub_id)
                #track back to top branch
                break
            self.anytree_handler("%s" % token_branch[i] , sub_id)
            l = Pr.is_match(token_branch[i] , lk)
            if l == -1 :
                if "EPSILON" in token_branch:
                    self.anytree_handler("epsilon" , sub_id)
                return -1



            


        