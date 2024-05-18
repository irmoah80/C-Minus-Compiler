import parsetable
import scanner
from anytree import Node, RenderTree


Scanner = scanner.Scanner('input.txt')
count = 0
ch = Scanner.getnexttoken()
ch0 = Node("Program")


class Parser():
    def __init__(self) -> None:
        pass

    def get_tbranch(self , token:str):
        global token_branch
        return parsetable.RHS_get(token)

    def anytree_handler(self , keyword:str , subroot):
        l_ch = "ch" + str(subroot)
        f_ch = "ch" + str(subroot+1)
        globals()[f_ch] = Node(keyword , parent= globals()[l_ch])
        pass

    def isterminal(self ,token):
        if parsetable.IS_terminal(token):
            return True
        else:
            return False

    def printer(self):
        global ch0
        for pre, _, node in RenderTree(ch0):
            print("%s%s" % (pre, node.name))

    def currunt_lk(self , l):
        global ch
        ch = l

    # def currunt_lk(self):
    #     global ch
    #     return ch

    def is_match(self , tk='Program' , lk =  None):
        # if lk == None:
        global ch
        lk = ch
        #"lookahead" is the current token , while "token" is pervious one
        global Scanner , token_branch , count
        can_write_intree = True
        sub_id = count
        print(tk +'----')

        token_branch = self.get_tbranch(tk)
        if token_branch is None or self.isterminal(tk):
            self.anytree_handler("(%s , %s)" % (lk[0] , lk[1]) , sub_id)
            count += 1
            print("(%s , %s)" % (lk[0] , lk[1]))
            self.currunt_lk(Scanner.getnexttoken())
            return

        Pr = Parser()
        for i in range(len(token_branch)):
            buff = token_branch[i].split()
            if len(buff) > 1:
                inner_token_branch = buff
                for i in inner_token_branch:
                    l = Pr.is_match(i , lk)
                    if l == -1 :
                        return -1
                break

            #     for j in buff:
            #         if lk[0] in buff and self.isterminal(lk[0]):
            #             #pass to compiler to go next
            #             lookahead = Scanner.getnexttoken()
            #             if lookahead == -1:
            #                 return -1
            #             self.anytree_handler("(%s , %s)" % (lk[0] , lk[1]) , sub_id)
            #             #track back to top branch
            #             break
            #         self.anytree_handler("%s" % (j) , sub_id)
            #         l = Pr.is_match(token_branch[i] , lk)
            #         if l == -1 :
            #             return -1
            #         pass
            if lk[0] in token_branch and self.isterminal(lk[0]):
                #pass to compiler to go next
                if can_write_intree:
                    self.anytree_handler("(%s , %s)" % (lk[0] , lk[1]) , sub_id)
                    # count += 1
                    print("(%s , %s)" % (lk[0] , lk[1]))
                    self.currunt_lk(Scanner.getnexttoken())
                #track back to top branch
                if lk == -1:
                    return -1
                break
            if can_write_intree:
                self.anytree_handler("%s" % token_branch[i] , sub_id)
                count += 1
            l = Pr.is_match(token_branch[i] , lk)
            if l == -1 :
                if "EPSILON" in token_branch and can_write_intree:
                    self.anytree_handler("epsilon" , sub_id)
                    count += 1
                return -1
