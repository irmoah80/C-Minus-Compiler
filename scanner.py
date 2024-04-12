#IN THE NAMEOF GOD
#first project
#sina maleki & mohammad ebrahin nejati jahromi
#1403 Farvardin - Sharif UNI


WH_SPACE = ' \n \r \t \v \f'
KEYWORD = {
    "if", 
    "else",
    "void",
    "int",
    "for",
    "break",
    "return",
    "endif"
}
SYMBOL = {
    ';',
    ':',
    ',',
    '[',
    ']',
    '(',
    ')',
    '{',
    '}',
    '+',
    '-',
    '*',
    '=',
    '<',
    '=='
}
COMMENT = {
    'Start' : '/*',
    'End' : '*/',
}
SYMBOL_TABLE = []
ERROR_TABLE = []
TOKENS = []

def error_handler(lineerror : str , line : int):
    '''
    print errors of each line on ERROR_TABLE
    '''
    ERROR_TABLE.append(line + '.	' + lineerror)

def symbol_handler(linesymbols : str , line : int):
    '''
    print symbols of each line on SYMBOL_TABLE
    '''
    SYMBOL_TABLE.append(line + '.	' + linesymbols)


def token_handler(linetokens : str , line : int):
    '''
    print tokens of each line on SYMBOL_TABLE
    '''
    TOKENS.append(line + '.	' + linetokens)

#ignore , handling in readline states
# def exp_check(exp : str):
#     '''
#     return 1 when error is "invalid input".
#     0 when error is "invalid number".
#     -1 when exp is correct.
#     '''
#     return

def exp_print():
    sym = open('symbol_table.txt' , 'a')
    tkn = open('tokens.txt' , 'a')
    err = open('lexical_errors' , 'a')

    for i in SYMBOL_TABLE:
        sym.write("%s\n" % i)
    
    for i in ERROR_TABLE:
        err.write("%s\n" % i)

    for i in TOKENS:
        tkn.write("%s\n" % i)


def readline(line :str):
    '''
    read each line , must run from main function
    '''
    buff = ''
    LINE_TOKEN = ''
    ERROR_LINE = ''
    SYMBL_LINE = ''

    In_word = False
    In_num = False #we can just use number after = , or in function
    word_type = ''
    for i in range(len(line)): # we must modify each line token on another function
        #save pervious line information
        if ERROR_LINE != '':
            error_handler(ERROR_LINE , i)
        if LINE_TOKEN != '':
            token_handler(LINE_TOKEN)
        if SYMBL_LINE != '':
            symbol_handler(SYMBL_LINE , i)
        
        if In_word:
            if line[i] in SYMBOL: #not space charecters
                In_word = False
                #maybe we need else here for turn is number off
                if buff in KEYWORD:
                    LINE_TOKEN += '(KEYWORD , ' + line[i] + ') '
                    #for finding () or {} errors , we need some if here , and change keyword from set to dict
                    LINE_TOKEN += '(SYMBOL , ' + line[i] + ') '

                elif buff.isalpha():
                    # status = exp_check(buff)
                    # if status is -1:
                    LINE_TOKEN += '(ID , ' + line[i] + ') '
                buff=''#clear buff for next one

            elif line[i].isalnum():
                buff += line[i]
                In_word = True
            elif line[i] in WH_SPACE:
                #check buff -> what is it?
                if buff in KEYWORD:
                    LINE_TOKEN += '(KEYWORD , ' + line[i] + ') '
                else:
                    # status = exp_check()
                    # if status is -1:
                    LINE_TOKEN += '(ID , ' + line[i] + ') '
                buff=''#clear buff for next one
            else: #illigal charecters
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid input)'
        elif In_num:
            if not line[i].isnumeric():
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid number)'
        else: #just for start case , when we do not know what happened at first
            if line[i].isnumeric:
                In_num = True
            elif line[i].isalpha:
                In_word = True
            elif line[i] in WH_SPACE or SYMBOL:
                pass
            else:
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid input)'


def cleaner(clean_code : list):
    '''
    two stage :
    1.clean code from comments
    2.i dont know
    with error handeling
    '''

    In_pro = False
    mid_line = []
    for i in range(len(clean_code)):
        
        start_c = clean_code[i].find('/*') if not In_pro else start_c
        end_c = clean_code[i].rfind('*/')

        if start_c is not -1 and end_c is not -1 :
            clean_code[i][start_c:end_c+2] = '' #remove single line comment
            In_pro= False

        if In_pro:
            if end_c is not -1:
                clean_code[i][:end_c+2] = '' #remove Multiline comments: last line
            else:
                #remove Multiline comments: mid lines
                mid_line.append(i)
                if i is len(clean_code):
                    error_handler('Unclosed comment')

        if not In_pro: #handeling errors
            if end_c is not -1:
                error_handler('Unmatched comment')


    return clean_code



def main() : #done in 4 step
    #1.read input file
    input = open('input.txt' , 'r')
    input = input.readlines()

    #2.cleaning code from comments
    input = cleaner(input)

    #3.read line per line and detect sym , tkn etc.
    for i in  range(len(input)):
        readline(input[i])
    
    #4.print items to file
    exp_print()

main()