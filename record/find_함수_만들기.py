def find_list(sentence,word_list):
    # sentence는 문자열
    # word_list는 찾을 문자가 들어있는 리스트.
    discrimination = []
    for i in range(len(word_list)):
        if word_list[i] in sentence:
            discrimination.append('T')
        else:
            discrimination.append('F')
    # print(discrimination)

    if 'F' in discrimination:
        None
    else:
        print(sentence)

def find_words(sentence,*args):
    # sentence는 문자열
    # args는 찾을 단어('문자열')들을 하나하나 병렬로 입력.
    discrimination = []
    word_list=[]
    for word in args:
        word_list.append(word)
    for i in range(len(word_list)):
        if word_list[i] in sentence:
            discrimination.append('T')
        else:
            discrimination.append('F')
    # print(discrimination)

    if 'F' in discrimination:
        None
    else:
        print(sentence)



sentence = '원리와 원칙을 중시한다.'
sentence_1 = '원리를 중시한다.'
sentence_2 = '원칙을 중시한다.'

list = ['원리', '원칙']
list_2 = ['원리','원칙','정의']

print(sentence.find('원리'))
print(sentence.find('원칙'))
print('\n')
print(sentence.find('원리' or '원칙'))
print(sentence_1.find('원리'or'원칙'))
print(sentence_2.find('원리'or'원칙'))
print('\n')

print(sentence.find('원리' and '원칙'))
print(sentence_1.find('원리' and '원칙'))
print(sentence_2.find('원리' and '원칙'))

print('원리' and '원칙' in sentence)
print('원리' and '원칙' in sentence_1)
print('원리' and '원칙' in sentence_2)
print('\n')

print('원리' in list and '원칙' in list )
print('가오가이거' in list or '원칙' in list )
print('가오가이거' in list and '원칙' in list )





find_list(sentence,list)
find find_words(sentence,'원리','원칙')
