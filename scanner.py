#IN THE NAMEOF GOD
#first project
#sina maleki & mohammad ebrahin nejati jahromi
#1403 Farvardin - Sharif UNI


WH_SPACE = ' \n \r \t \v \f'
KEYWORD = [
    "break",
    "else",
    "if",
    "int",
    "while",
    "return",
    "void",
]
SYMBOL = {
    ";",
    ":",
    ",",
    "[",
    "]",
    "(",
    ")",
    "{",
    "}",
    "+",
    "-",
    "*",
    "=",
    "<",
    "==",
    "/"
}
COMMENT = {
    'Start' : '/*',
    'End' : '*/',
}
SYMBOL_TABLE = []
ERROR_TABLE = []
TOKENS = []
KE_BYUSER = []

def error_handler(lineerror : str , line : int):
    '''
    print errors of each line on ERROR_TABLE
    '''
    ERROR_TABLE.append(str(line) + '.	' + lineerror)

def token_handler(linetokens : str , line : int):
    '''
    print tokens of each line on SYMBOL_TABLE
    '''
    TOKENS.append(str(line) + '.	' + linetokens)

def exp_print():
    sym = open('symbol_table.txt' , 'a')
    tkn = open('tokens.txt' , 'a')
    err = open('lexical_errors.txt' , 'a')

    ke = KEYWORD + KE_BYUSER
    for i in range(len(ke)):
        sym.write("%s.\t%s\n" % (i+1 , ke[i]))
    
    for i in ERROR_TABLE:
        err.write("%s\n" % i)

    if len(ERROR_TABLE) == 0:
        err.write('There is no lexical error.')

    for i in TOKENS:
        tkn.write("%s\n" % i)
    

def readline(line :str , lno : int):
    '''
    read each line , must run from main function
    '''
    buff = ""
    LINE_TOKEN = ''
    ERROR_LINE = ''

    In_word = False
    In_num = False #we can just use number after = , or in function
    word_type = ''
    for i in range(len(line)): # we must modify each line token on another function
        #save pervious line information
        
        if In_word:
            if line[i] in SYMBOL: #not space charecters
                In_word = False
                #maybe we need else here for turn is number off
                if buff in KEYWORD:
                    LINE_TOKEN += '(KEYWORD, ' + buff + ') '
                    #for finding () or {} errors , we need some if here , and change keyword from set to dict
                    LINE_TOKEN += '(SYMBOL, ' + line[i] + ') '

                elif buff.isalnum():
                    # status = exp_check(buff)
                    # if status is -1:
                    LINE_TOKEN += '(ID, ' + buff + ') '
                    LINE_TOKEN += '(SYMBOL, ' + line[i] + ') '
                    if buff not in KE_BYUSER:
                        KE_BYUSER.append(buff)
                buff=''#clear buff for next one

            elif line[i].isalnum():
                buff += line[i]
            elif line[i] in WH_SPACE:
                In_word = False
                #check buff -> what is it?
                # print(str(type(buff)) + buff)
                if buff in KEYWORD:#do not print white spaces in tokens
                    LINE_TOKEN += '(KEYWORD, ' + buff + ') '
                else:
                    # status = exp_check()
                    # if status is -1:
                    LINE_TOKEN += '(ID, ' + buff + ') '
                    if buff not in KE_BYUSER:
                        KE_BYUSER.append(buff)
                buff=''#clear buff for next one
            else: #illigal charecters
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid input) '
                buff = ''
                In_word = False
        elif In_num:
            if line[i].isalpha():
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid number) '
                In_num = False
                In_word = False
                buff = ''
            elif line[i] in WH_SPACE:
                In_num = False
                LINE_TOKEN += '(NUM, ' + buff + ') '
                buff=''#clear buff for next one
            elif line[i] in SYMBOL:
                In_num = False
                LINE_TOKEN += '(NUM, ' + buff + ') '
                LINE_TOKEN += '(SYMBOL, ' + line[i] + ') '
                buff=''
            elif line[i].isnumeric():
                buff += line[i]

        else: #just for start case , when we do not know what happened at first
            if line[i].isnumeric():
                if buff == '=':
                    LINE_TOKEN += '(SYMBOL, ' + buff + ') '
                    buff = ''
                buff += line[i]
                In_num = True
            elif line[i].isalpha():
                if buff == '=':
                    LINE_TOKEN += '(SYMBOL, ' + buff + ') '
                    buff = ''
                buff += line[i]
                In_word = True
            elif line[i] in WH_SPACE:
                if buff == '=':
                    LINE_TOKEN += '(SYMBOL, ' + buff + ') '
                    buff = ''
                pass
            elif line[i] in SYMBOL and line[i]!='=':
                if buff == '=':
                    LINE_TOKEN += '(SYMBOL, ' + buff + ') '
                    buff = ''
                LINE_TOKEN += '(SYMBOL, ' + line[i] + ') '
            elif line[i] == '=':
                buff+=line[i]
                if buff == '==':
                    LINE_TOKEN += '(SYMBOL, ' + buff + ') '
                    buff = ''
            else:
                buff += line[i]
                ERROR_LINE += '(' + buff + ', Invalid input) '
                buff = ''

    if ERROR_LINE != '':
        error_handler(ERROR_LINE , lno)
    if LINE_TOKEN != '':
        token_handler(LINE_TOKEN , lno)

    
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

        if In_pro:
            end_c = clean_code[i].rfind('*/')
            if end_c != -1 :
                clean_code[i] = clean_code[i].replace(clean_code[i][:end_c+2] , '')
                In_pro = False
            else:
                clean_code[i] = clean_code[i].replace(clean_code[i] , '')
        else:
            start_c = clean_code[i].find('/*')
            end_c = clean_code[i].rfind('*/')

            if start_c != -1 and end_c != -1 :
                print(clean_code[i]+'11')
                clean_code[i] = clean_code[i].replace(clean_code[i][start_c:end_c+2] , '') #remove single line comment
                print(clean_code[i]+ '00')
                In_pro= False
            elif start_c == -1 and end_c != -1:
                clean_code[i] = clean_code[i].replace('*/' , '')
                error_handler('(*/, Unmatched comment)' , i+1)
            elif start_c != -1 and  end_c == -1:
                clean_code[i] = clean_code[i].replace(clean_code[i][start_c:] , '')
                In_pro = True
                error_handler('(, Unclosed comment)' , i+1)

        # if In_pro:
        #     if end_c != -1 :
        #         clean_code[i] = clean_code[i].replace(clean_code[i][:end_c+2] , '')
        #         In_pro = False
        #         #remove Multiline comments: last line
        #     else:
        #         #remove Multiline comments: mid lines
        #         mid_line.append(i)
        #         if i == len(clean_code):
        #             error_handler('(,Unclosed comment)' , i+1)

        # if not In_pro: #handeling errors
        #     if end_c != -1:
        #         print(clean_code[i]+'33.%s' %i)
        #         error_handler('(*/, Unmatched comment)' , i+1)

    return clean_code

def main() : #done in 4 step
    #1.read input file
    input = open('input.txt' , 'r')
    input = input.readlines()

    #2.cleaning code from comments
    input = cleaner(input)

    #3.read line per line and detect sym , tkn etc.
    for i in range(len(input)):
        readline(input[i] , i+1)
    
    #4.print items to file
    exp_print()

main()