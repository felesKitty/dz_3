
def int_func():
     for i_words in input('If you want to see a miracle, '
                        'enter any words, which contains'
                        'lower latin leters - \n').split():
         buk = 0
         for buk2 in i_words:
             if 97 <= ord(buk2) <= 122:
                buk += 1
         print(i_words.title() if buk == len(i_words)
              else f'{words} - Error! Not this symbols!')

int_func()