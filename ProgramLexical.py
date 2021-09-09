import string

#input
sentence = ' vader beeldhouwen hout'
input_string = sentence.lower() + '#'

#inisiasi
alphabet_list = list(string.ascii_lowercase)
state_list = ['q0','q1','q2','q3','q4','q5','q6','q7','q8','q9','q10','q11','q12','q13','q14','q15','q16','q17','q18','q19','q22','q23','q24','q25','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37','q38']

transition_table = {}

for state in state_list:
    for alphabet in alphabet_list:
        transition_table[(state,alphabet)] = 'error'
    transition_table[(state,'#')] = 'error'
    transition_table[(state,' ')] = 'error'

#spasi sebelum input
transition_table['q16', ' '] = 'q16'

#update transisi table untuk moeder
transition_table[('q16', 'm')] = 'q6'
transition_table[('q6' , 'o')] = 'q7'
transition_table[('q7' , 'e')] = 'q8'
transition_table[('q8' , 'd')] = 'q9'
transition_table[('q9' , 'e')] = 'q10'
transition_table[('q10' , 'r')] = 'q14'
transition_table[('q14' , ' ')] = 'q15'
transition_table[('q14' , '#')] = 'accept'
transition_table[('q15' , ' ')] = 'q15'
transition_table[('q15' , '#')] = 'accept'

#transisi untuk vader
transition_table[('q16' , 'v')] = 'q11'
transition_table[('q11' , 'a')] = 'q8'
transition_table[('q8' , 'd')] = 'q9'
transition_table[('q9' , 'e')] = 'q10'
transition_table[('q10' , 'r')] = 'q14'


#transisi untuk m,v
transition_table[('q15' , 'm')] = 'q6'
transition_table[('q15' , 'v')] = 'q11'

#transisi untuk zitten
transition_table[('q16' , 'z')] = 'q1'
transition_table[('q1' , 'i')] = 'q2'
transition_table[('q2' , 't')] = 'q3'
transition_table[('q3' , 't')] = 'q4'
transition_table[('q4' , 'e')] = 'q5'
transition_table[('q5' , 'n')] = 'q14'

#transisi untuk eten
transition_table[('q16' , 'e')] = 'q3'
transition_table[('q3' , 't')] = 'q4'
transition_table[('q4' , 'e')] = 'q5'
transition_table[('q5' , 'n')] = 'q14'

#transisi untuk wassen
transition_table[('q16' , 'w')] = 'q17'
transition_table[('q17' , 'a')] = 'q18'
transition_table[('q18' , 's')] = 'q19'
transition_table[('q19' , 's')] = 'q4'
transition_table[('q4' , 'e')] = 'q5'
transition_table[('q5' , 'n')] = 'q14'

#transisi untuk z,e,w
transition_table[('q15' , 'z')] = 'q1'
transition_table[('q15' , 'e')] = 'q3'
transition_table[('q15' , 'w')] = 'q17'

#transisi untuk ei
transition_table[('q16' , 'e')] = 'q3'
transition_table[('q3' , 'i')] = 'q14'

#transisi untuk fiets
transition_table[('q16' , 'f')] = 'q24'
transition_table[('q24' , 'i')] = 'q25'
transition_table[('q25' , 'e')] = 'q26'
transition_table[('q26' , 't')] = 'q27'
transition_table[('q27' , 's')] = 'q14'

#transisi untuk vis
transition_table[('q16' , 'v')] = 'q11'
transition_table[('q11' , 'i')] = 'q27'
transition_table[('q27' , 's')] = 'q14'

#transisi untuk kip
transition_table[('q16' , 'k')] = 'q31'
transition_table[('q31' , 'i')] = 'q32'
transition_table[('q32' , 'p')] = 'q14'

#transisi untuk stoel
transition_table[('q16' , 's')] = 'q34'
transition_table[('q34' , 't')] = 'q35'
transition_table[('q35' , 'o')] = 'q36'
transition_table[('q36' , 'e')] = 'q37'
transition_table[('q37' , 'l')] = 'q14'

#transisi e,f,v,k,s
transition_table[('q15' , 'e')] = 'q3'
transition_table[('q15' , 'f')] = 'q24'
transition_table[('q15' , 'v')] = 'q11'
transition_table[('q15' , 'k')] = 'q31'
transition_table[('q15' , 's')] = 'q34'

#lexical analysis
idx_char = 0
state = 'q16'
current_token = ''
while state != 'accept' :
    current_char = input_string[idx_char]
    current_token += current_char
    state = transition_table[(state, current_char)]
    if state=='q14':
        print('Kata :' , current_token, ', valid')
        current_token = ''
    if state=='error':
        print('Kata tidak valid')
        break;
    idx_char = idx_char+1

#conclusion
if state=='accept':
    print('Kalimat yang terbuat :',sentence, ', valid')
else :
    print('Error : Kalimat tidak valid')
