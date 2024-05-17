grammer = {
    "Program" : ["Declaration-list"], #???
    "Declaration-list" : ["Declaration Declaration-list", "EPSILON"],
    "Declaration" : ["Declaration-initial Declaration-prime"],
    "Declaration-initial" : ["Type-specifier ID"],
    "Declaration-prime" : ["Fun-declaration-prime", "Var-declaration-prime"],
    "Var-declaration-prime" : [";", "[ NUM ] ;"],
    "Fun-declaraion-prime" : ["( Params ) Compound-stmt"],
    "Type-specifier" : ["int", "void"],
    "Params" : ["int ID Param-prime Param-list", "void"],
    "Param-list" : [", Param Param-list", "EPSILON"],
    "Param" : ["Declaration-initial Param-prime"],
    "Param-prime" : ["[ ]", "EPSILON"],
    "Compound-stmt" : ["Declaration-list Statement-list"],
    "Statement-list" : ["Statement Statement-list", "EPSILON"],
    "Statement" : ["Expression-stmt", "Compound-stmt", "Selection-stmt", "Iteration-stmt", "Return-stmt"],
    "Expression-stmt" : ["Expression ;", "break ;", ";"],
    "Selection-stmt" : ["if ( Expression ) Statement Else-stmt"],
    "Else-stmt" : ["endif", "else Statement endif"],
    "Iteration-stmt" : ["for (Expression; Expression; Expression) Statement"],
    "Return-stmt" : ["return Return-stmt-prime"],
    "Return-stmt-prime": [";", "Expression ;"],
    "Expression" : ["Simple-expression-zegond", "ID B"],
    "B" : ["= Expression", "[ Expression ] H", "Simple-expression-prime"],
    "H" : ["= Expression", "G D C"],
    "Simple-expression-zegond" : ["Additive-expression-zegond C"],
    "Simple-expression-prime" : ["Additive-expression-prime C"],
    "C" : ["Relop Additive-expression", "EPSILON"],
    "Relop" : ["<", "=="],
    "Additive-expression" : ["Term D"],
    "Additive-expression-prime" : ["Term-prime D"],
    "Additive-expression-zegond" : ["Term-zegond D"],
    "D" : ["Addop Term D", "EPSILON"],
    "Addop" : ["+", "-"],
    "Term" : ["Signed-factor G"],
    "Term-prime" : ["Signed-factor-prime G"],
    "Term-zegond" : ["Signed-factor-zegond G"],
    "G" : ["* Signed-factor G", "EPSILON"],
    "Signed-factor" : ["+ Factor", "- Factor", "Factor"],
    "Signed-factor-prime" : ["Factor-prime"],
    "Signed-factor-zegond" : ["+ Factor", "- Factor", "Factor-zegond"],
    "Factor" : ["( Expression )", "ID Var-call-prime", "NUM"],
    "Var-call-prime" : ["( Args )", "Var-prime"],
    "Var-prime" : ["[ Expression ]", "EPSILON"],
    "Factor-prime" : ["( Args )", "EPSILON"],
    "Factor-zegond" : ["( Expression )", "NUM"],
    "Args" : ["Arg-list", "EPSILON"],
    "Arg-list" : ["Expression Arg-list-prime"],
    "Arg-list-prime" : [", Expression Arg-list-prime", "EPSILON"]
}

terminals = ["EPSILON", "ID", ";", "[", "NUM", "]", "int", "void", "{", "}", "break", "if", "(", ")", "endif", "else", "for", "return", "<", "==", "+", "-", "*", ","]

def IS_terminal(t):
    if t in terminals:
        return True
    else:
        return False

def RHS_get(t):
    return grammer.get(t)
