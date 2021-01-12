import pandas as pd
import openpyxl
import random

class HRstdnts:
    name = None
    number = None
    char_pmt1 = None #개인성격
    char_pmt2 = None #교우관계
    study_pmt2 = None
    study_pmt2 = None
    spcl1 = None #봉사활동
    spcl2 = None #악기
    spcl3 = None #운동

    def __init__(self,name,number):
        #name 자리에는 이름 칼럼에서 정보를 끌어오고,
        #number 자리에는 번호 칼럼에서 정보를 끌어온다.
        self.name = name
        self.number = number
    def char1_sentence(self,char_pmt1_input):
        self.char_pmt1 = char_pmt1_input
        sentence_list = list()

        '''
        성격에 대한 쉬트 및 칼럼 정보를 읽어서, list에 append 한다.
        문장을 계속해서 업데이트할 수 있도록, 새로운 쉬트를 활용한다. 
        문장들은 앞서 내가 썼던 생기부 문장들을 참고한다.
        '''
        sentence_list.append()
