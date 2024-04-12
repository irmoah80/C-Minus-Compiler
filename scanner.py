#IN THE NAMEOF GOD
#first project
#sina maleki & mohammad ebrahin nejati jahromi


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
    'SingleLine' : '#'
}

ID_CHAR = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

NUMBERS = '0123456789'

SYMBOL_tABLE = []

def error_handler():
    pass

def exp_check(exp : str):
    '''
    return 1 when error is "invalid input".
    0 when error is "invalid number".
    -1 when exp is correct.
    '''
    return

def exp_print():
    pass


def readline(line :str):
    buff = ''
    ADD_KEYWORD = set
    LINE_TOKEN = list
    In_word = False
    In_num = False #we can just use number after = , or in function
    word_type = ''
    for i in range(len(line)):
        if In_word:
            if line[i] in SYMBOL: #not space charecters
                if In_word:
                    In_word = False
                    In_num = True
                #maybe we need else here for turn is number off
                if buff in KEYWORD:
                    LINE_TOKEN.append('(KEYWORD , ' + line[i] + ')')
                    #for finding () or {} errors , we need some if here , and change keyword from set to dict
                    LINE_TOKEN.append('(SYMBOL , ' + line[i] + ')')

                elif buff.isalpha():
                    status = exp_check(buff)
                    if status is -1:
                        LINE_TOKEN.append('(ID , ' + line[i] + ')')

                elif buff.isnumeric():
                    pass

            elif line[i].isalpha():
                buff += line[i]
                In_word = True
            elif line[i].isnumeric():
                buff += line[i]
                if not In_word:
                    In_num = True
                pass
            elif line[i] in WH_SPACE:
                #check buff -> what is it?
                if buff in KEYWORD:
                    LINE_TOKEN.append('(KEYWORD , ' + line[i] + ')')
                    elif:
                    status = exp_check()
                    if status is -1:
                        LINE_TOKEN.append('(ID , ' + line[i] + ')')
            
        #     if buff in KEYWORD:
        #         LINE_TOKEN.append('(kEYWORD , ' + buff + ')')
        #     else:
        #         LINE_TOKEN.append('(ID , ' + buff + ')')

        #     LINE_TOKEN.append('(SYMBOL , ' + line[i] + ')')

        # elif line[i] is ' ':
        #     bu
        #     pass


    return LINE_TOKEN


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



def main() :
    input = open('input.txt' , 'r')
    input = input.readlines()

    for i in  range(len(input)):
        readline(input[i])
        pass
    pass

main()