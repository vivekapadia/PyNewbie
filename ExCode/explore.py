# ============================================================================
# ============================================================================
# ============================================================================
# Strings
var_str_a = 'Hello, Wo'
var_str_a_len = len(var_str_a)
for item in var_str_a:
    print(item,end='\t')

print('\n\n[0]\t',var_str_a[0])
print('[8]\t',var_str_a[8])
print(f'[-1]\taka[{var_str_a_len-1}]\t',var_str_a[-1],'\n')
# print('\n[9]\t',var_str_a[9])
# print('\n[-10]\t',var_str_a[-10])

for num in range(len(var_str_a)):
    print(var_str_a[num],end = '\t')
print('Hello' in var_str_a,'\n\n')

def print_index(len):
    for i in range(len):
        print(i, end='')
    print()
print(var_str_a,f'\t[:]\t',var_str_a[:])
print_index(var_str_a_len)
print(var_str_a,f'\t[:1]\t',var_str_a[:1])
print_index(var_str_a_len)
print(var_str_a,f'\t[1:2]\t',var_str_a[1:2])
print_index(var_str_a_len)
print(var_str_a,f'\t[1:]\t',var_str_a[1:])
print_index(var_str_a_len)
print(var_str_a,f'\t[-1:0]\taka\t[{var_str_a_len-1}:0]',var_str_a[-1:0])
print_index(var_str_a_len)
print(var_str_a,f'\t[-1:]\taka\t[{var_str_a_len-1}:{var_str_a_len}]',var_str_a[-1:])
print_index(var_str_a_len)
print(var_str_a,f'\t[-5:]\taka\t[{var_str_a_len-5}:{var_str_a_len}]',var_str_a[-5:])
print_index(var_str_a_len)
print(var_str_a,f'\t[-10:]\taka\t[{var_str_a_len-10}:{var_str_a_len}]',var_str_a[-10:])
print_index(var_str_a_len)
print(var_str_a,f'\t[-20:]\taka\t[{var_str_a_len-20}:{var_str_a_len}]',var_str_a[-20:])
print_index(var_str_a_len)
print(var_str_a,f'\t[-1:2]\taka\t[{var_str_a_len-1}:2]',var_str_a[-1:2])
print_index(var_str_a_len)
print(var_str_a,f'\t[:-1]\taka\t[0:{var_str_a_len-1}]',var_str_a[:-1])
print_index(var_str_a_len)
print(var_str_a,f'\t[2:-1]\taka\t[2:{var_str_a_len-1}]',var_str_a[2:-1])
print_index(var_str_a_len)
print(var_str_a,f'\t[-1:-1]\taka\t[-1:{var_str_a_len-1}]',var_str_a[-1:-1])
print_index(var_str_a_len)

print('\n\n')
print(var_str_a, '\tupper()\t' ,var_str_a.upper(), '\t',type(var_str_a.upper())) # make string upper case
print(var_str_a, '\tlower()\t' ,var_str_a.lower(), '\t',type(var_str_a.lower())) # make string lower case
print(var_str_a, '\tstrip()\t' ,var_str_a.strip(), '\t',type(var_str_a.strip())) # make strip lose whitespace from beginning and end
print(var_str_a, '\treplace()\t' ,var_str_a.replace('hello','Vivek'), '\t',type(var_str_a.replace('hello','Vivek'))) #make string replace 1st string with 2nd string
print(var_str_a, '\treplace()\t' ,var_str_a.replace('Hello','Vivek'), '\t',type(var_str_a.replace('Hello','Vivek'))) #make string replace 1st string with 2nd string
print(var_str_a, '\tsplit()\t' ,var_str_a.split(','), '\t',type(var_str_a.split(','))) #make string split into sub string and return list
print(var_str_a, '\tsplit()\t' ,var_str_a.split('#'), '\t',type(var_str_a.split('#'))) #make string split into sub string and return list
print(var_str_a, '\tcapitalize()\t' ,var_str_a.capitalize(), '\t',type(var_str_a.capitalize()))







# ============================================================================
# ============================================================================
# ============================================================================
# Variables & DataTypes
# var_complex = complex (1,2)
# var_boolean = True
# var_string = 'Explore Newbie'
# var_none = None
# var_integer = 10
# var_float = 10.2
# var_range = range(5)
# var_list = [1, 2, [3,4], 5]
# var_tuple = (1, 2, (3,4), 5)
# var_dictionary = {1:'a',2:'b', 3: {3:'c', 4:'d'}, 5:'e'}
#
# print(var_complex,'   Type :',type(var_complex))
# print(var_boolean,'   Type :',type(var_boolean))
# print(var_string,'   Type :',type(var_string))
# print(var_none,'   Type :',type(var_none))
# print(var_integer,'   Type :',type(var_integer))
# print(var_float,'   Type :',type(var_float))
# print(var_range,'   Type :',type(var_range))
# print(var_list,'   Type :',type(var_list))
# print(var_tuple,'   Type :',type(var_tuple))
# print(var_dictionary,'   Type :',type(var_dictionary))



