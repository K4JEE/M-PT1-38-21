def sep(text, maxlen):
    text_new = ''  
    count = 0  
    for i in text.split():  
        count += len(i)  
        if count > (int(maxlen)-1):  
            text_new += '\n'  
            count = len(i)  
        elif text_new != '':  
            text_new += ' '  
            count += 1  
        text_new += i  
    return text_new

def align(text_new):
    strings = [string.splitlines() for string in text_new.split('\n')]  
    for string in strings: 
        for i, line in enumerate(string):   
            words = line.split()  
            dif_symb = (int(maxlen)-1) - sum(map(len, words))  
            spaces = len(words) - 1 
            spaces = spaces if spaces > 0 else dif_symb
            div, mod = divmod(dif_symb, spaces) 
            new_spaces = [' ' * (div + 1) for _ in range(mod)] + [' ' * div] * (spaces - mod) + ['']
            string[i] = ''.join(w + ns for w, ns in zip(words, new_spaces))
    text_format = ('\n'.join(''.join(string) for string in strings))
    with open ("text_format.txt", "w", encoding="utf-8") as f:
        f.write(text_format)
    return(print('Well done, your text is in file text_format.txt'))


with open ("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

maxlen = input('Enter an integer greater than 35\n')
align(sep(text, maxlen)) 