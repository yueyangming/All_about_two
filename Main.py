__author__ = ' Harold (Finch) '

RESULT_LIMIT = 100
RESULT_LIST = [[0, []] for i in range(RESULT_LIMIT + 1)]
K = 5  # Num of 2.
SYMBOL_OPTION = ['+', '-', '*', '/', '%', '**']  # 6 possible symbols.


def string_insert(string, index, insertion):
    length = len(string)
    output = string[0:index] + insertion + string[index:length]
    return output


def string_pop(string, index='default'):
    if index == 'default':
        index = len(string)
    output = string[0:index] + string[index + 1:len(string)]
    return output


def base_transformtion(number, base=6, length=4):
    output = []
    for i in range(length):
        output.append(number % base)
        number = number / base
    return output[::-1]


def list_to_symbols(number_list):
    symbol_option = ['+', '-', '*', '/', '%', '&']  # 6 possible symbols.
    output = []
    for each in number_list:
        output.append(symbol_option[int(each)])
    return output

if __name__ == '__main__':

    for i in range(len(SYMBOL_OPTION) ** K):
        number_list = base_transformtion(i)
        symbol_list = list_to_symbols(number_list)
        whole_string = '2'
        end_index = 1
        for each in symbol_list:
            whole_string += each
            whole_string += '2'
            end_index += 1
            for left_bracket_position in range(0, end_index - 1):
                for right_bracket_position in range(left_bracket_position + 2, end_index):
                    whole_string = string_insert(whole_string, left_bracket_position * 2, '(')
                    whole_string = string_insert(whole_string, right_bracket_position * 2, ')')
                    whole_string = whole_string.replace('&', '**')  # First change it to some one-space char
                    try:  # 0 may cause some problem, 2 / 0 or 2 % 0
                        result = eval(whole_string)
                        if result >= 0 and result <= RESULT_LIMIT and (whole_string not in RESULT_LIST[result][1]):
                            RESULT_LIST[result][0] += 1
                            RESULT_LIST[result][1].append(whole_string)
                        whole_string = whole_string.replace('**', '^')  # Then change back to form the string.
                        whole_string = string_pop(whole_string, right_bracket_position * 2)
                        whole_string = string_pop(whole_string, left_bracket_position * 2)
                    except:
                        whole_string = whole_string.replace('**', '^')
                        whole_string = string_pop(whole_string, right_bracket_position * 2)
                        whole_string = string_pop(whole_string, left_bracket_position * 2)
    # Output part.
    target = input('Input target number \n')
    exit_flag = 0
    while exit_flag == 0:
        target = int(target)
        print(RESULT_LIST[target][0])
        for each in RESULT_LIST[target][1]:
            print(each)
        target = input('Input target number \n')
        if target == 'q':
            exit_flag = 1
