import os

# states is a number list. A number represent a state.

#general discriminator
def discriminator(input):
    return ord(input) in range(65, 91) or ord(input) in range(97, 123) or ord(input) in range(48, 58) or ord(input) in [95]

def discriminator_alphabet(input):
    return ord(input) in range(65, 91) or ord(input) in range(97, 123)

def discriminator_num(input):
    return ord(input) in range(48, 58)

class I_NFA():
    def __init__(self):
        self.state_list = [0,1]
        self.now_state = 0

    def switch_state(self,input): # we don't know whether input is belong to I_NFA. It's redundant to discriminate again.
        if self.now_state == 0 and (ord(input) in range(65,91) or ord(input) in range(97,123) or ord(input) == 95):
            self.now_state = 1
        elif self.now_state == 1 and (ord(input) in range(65,91) or ord(input) in range(97,123) or ord(input) in range(48,58) or ord(input) == 95):
            self.now_state = 1
        else:
            return False
        return 1
    def return_to_zero(self):
        self.now_state = 0

class ZS_NFA():
    def __init__(self):
        self.state_list = [0,1,2]
        self.now_state = 0

    def switch_state(self,input): # we don't know whether input is belong to ZS_NFA. It's redundant to discriminate again.
        if self.now_state == 0 and (ord(input) == 43 or ord(input) == 45):
            self.now_state = 1
        elif self.now_state == 1 and ord(input) in range(48,58):
            self.now_state = 2
        elif self.now_state == 2 and ord(input) in range(48,58):
            self.now_state = 2
        elif self.now_state == 0 and ord(input) in range(48,58):
            self.now_state = 2
        else:
            return False  # meaning that it's not mine again or it's wrong
        return 1

    def return_to_zero(self):
        self.now_state = 0

class ZF_NFA():
    def __init__(self):
        self.state_list = [0,1,2,3]
        self.now_state = 0

    def switch_state(self,input): # we don't know whether input is belong to ZF_NFA. It's redundant to discriminate again.
        if self.now_state == 0 and ord(input) == 39:
            self.now_state = 1
        elif self.now_state == 1 and (ord(input) in range(65,91)
                                      or ord(input) in range(97,123)
                                      or ord(input) in range(48,58)
                                      or ord(input) in [95,42,43,45,47]):
            self.now_state = 2
        elif self.now_state == 2 and ord(input) == 39:
            self.now_state = 3
        else:
            return False  # meaning that it's not mine again or it's wrong
        return 1

    def return_to_zero(self):
        self.now_state = 0

class ZFC_NFA():
    def __init__(self):
        self.state_list = [0,1,2,3]
        self.now_state = 0

    def switch_state(self,input): # we don't know whether input is belong to ZFC_NFA. It's redundant to discriminate again.
        if self.now_state == 0 and ord(input) == 34:
            self.now_state = 1
        elif self.now_state == 1 and (ord(input) in [32,33] or ord(input) in range(35,127)):
            self.now_state = 2
        elif self.now_state == 2 and ord(input) == 34:
            self.now_state = 3
        elif self.now_state == 2 and (ord(input) in [32,33] or ord(input) in range(35,127)):
            self.now_state = 2
        else:
            return False  # meaning that it's not mine again or it's wrong
        return 1

    def return_to_zero(self):
        self.now_state = 0

def read_str_merge():
    if not os.path.exists("./testfile.txt"):
        raise FileNotFoundError
    with open("./testfile.txt") as f:
        list_str = f.readlines()
    f.close()

    return list_str   # return list of inputs.we would like to analyse line by line.

def write_into_file_initialize():
    with open("./output.txt","w") as f:
        pass
    f.close()

def write_into_file(str,type):
    with open("./output.txt","a") as f:
        f.write(f"{type} {str}\n")
    f.close()

def self_cleaning(str):
    if str[0] == ' ' or str[0] == '\n':
        return self_cleaning(str[1:])
    else:
        return str

# please distinguish between chars in key words and chars.
def key_recognition(str):
    # assert length of str is greater than 1
    record = str
    if (str[:5] in ['const' ,'CONST']) and( not discriminator(str[5])):
        write_into_file(str[:5],"CONSTTK")
        return str[5:]
    elif (str[:3] in [ 'int', 'INT']) and (not discriminator(str[3])):
        write_into_file(str[:3],"INTTK")
        return str[3:]
    elif (str[:4] in [ 'char', 'CHAR']) and (not discriminator(str[4])):
        write_into_file(str[:4],"CHARTK")
        return str[4:]
    elif (str[:4] in [ 'void', 'VOID']) and not discriminator(str[4]):
        write_into_file(str[:4],"VOIDTK")
        return str[4:]
    elif (str[:4] in [ 'main', 'MAIN']) and not discriminator(str[4]):
        write_into_file(str[:4],"MAINTK")
        return str[4:]
    elif (str[:2] in [ 'if', 'IF']) and not discriminator(str[2]):
        write_into_file(str[:2],"IFTK")
        return str[2:]
    elif (str[:4] in ['else' or 'ELSE']) and not discriminator(str[4]):
        write_into_file(str[:4],"ELSETK")
        return str[4:]
    elif (str[:2] in [ 'do' , 'DO']) and not discriminator(str[2]):
        write_into_file(str[:2],"DOTK")
        return str[2:]
    elif (str[:5] in [ 'while' , 'WHILE']) and not discriminator(str[5]):
        write_into_file(str[:5],"WHILETK")
        return str[5:]
    elif (str[:3] in [ 'for' , 'FOR']) and not discriminator(str[3]):
        write_into_file(str[:3],"FORTK")
        return str[3:]
    elif (str[:5] in [ 'scanf' , 'SCANF']) and not discriminator(str[5]):
        write_into_file(str[:5],"SCANFTK")
        return str[5:]
    elif (str[:6] in [ 'printf' , 'PRINTF']) and not discriminator(str[6]):
        write_into_file(str[:6],"PRINTFTK")
        return str[6:]
    elif (str[:6] in [ 'return' , 'RETURN']) and not discriminator(str[6]):
        write_into_file(str[:6],"RETURNTK")
        return str[6:]
    elif str[:1] == '+':
        write_into_file(str[:1],"PLUS")
        return str[1:]
    elif str[:1] == '-':
        write_into_file(str[:1],"MINU")
        return str[1:]
    elif str[:1] == '*':
        write_into_file(str[:1],"MULT")
        return str[1:]
    elif str[:1] == '/':
        write_into_file(str[:1],"DIV")
        return str[1:]
    elif str[:2] == '<=': # guarantee that it's ahead of '<'
        write_into_file(str[:2],"LEQ")
        return str[2:]
    elif str[:1] == '<':
        write_into_file(str[:1],"LSS")
        return str[1:]
    elif str[:2] == '>=':  # guarantee that it's ahead of '>'
        write_into_file(str[:2],"GEQ")
        return str[2:]
    elif str[:1] == '>':
        write_into_file(str[:1],"GRE")
        return str[1:]
    elif str[:2] == '==':   # guarantee that it's ahead of '='
        write_into_file(str[:2],"EQL")
        return str[2:]
    elif str[:1] == '=':
        write_into_file(str[:1],"ASSIGN")
        return str[1:]
    elif str[:2] == '!=':
        write_into_file(str[:2],"NEQ")
        return str[2:]
    elif str[:1] == ';':
        write_into_file(str[:1],"SEMICN")
        return str[1:]
    elif str[:1] == ',':
        write_into_file(str[:1],"COMMA")
        return str[1:]
    elif str[:1] == '(':
        write_into_file(str[:1],"LPARENT")
        return str[1:]
    elif str[:1] == ')':
        write_into_file(str[:1],"RPARENT")
        return str[1:]
    elif str[:1] == '[':
        write_into_file(str[:1],"LBRACK")
        return str[1:]
    elif str[:1] == ']':
        write_into_file(str[:1],"RBRACK")
        return str[1:]
    elif str[:1] == '{':
        write_into_file(str[:1],"LBRACE")
        return str[1:]
    elif str[:1] == '}':
        write_into_file(str[:1],"RBRACE")
        return str[1:]
    return record

def lexical_analysis():
    write_into_file_initialize()
    infa = I_NFA()
    zsnfa = ZS_NFA()
    zfnfa = ZF_NFA()
    zfcnfa = ZFC_NFA()

    for line in read_str_merge():
        # sp: cleaning and deciding
        if line == '' or line == '\n':
            continue
        line = self_cleaning(line)

        # sr: decide key words
        line = key_recognition(line)

        # s2: decide remaining architectures
        while (line != ''):

            # sr: decide key words --special
            line = key_recognition(line)

            # identifier
            temp = ''
            cnt = 0
            while(infa.switch_state(line[cnt]) != False):
                temp = temp + line[cnt]
                cnt += 1
            if temp != '' and infa.now_state == infa.state_list[-1]:
                line = line[cnt:]
                write_into_file(temp,"IDENFR")
                infa.return_to_zero()

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            # sr: decide key words
            line = key_recognition(line)

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            # sr: decide key words   ####  controversial! -100 is integer ,you can not recognise '-' partially.  ####
            line = key_recognition(line)

            if discriminator_alphabet(line[0]):
                continue

            # integer
            temp = ''
            cnt = 0
            while(zsnfa.switch_state(line[cnt]) != False):
                temp = temp + line[cnt]
                cnt += 1
            if temp != '' and zsnfa.now_state == zsnfa.state_list[-1]:
                line = line[cnt:]
                write_into_file(temp,"INTCON")
                zsnfa.return_to_zero()

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            # sr: decide key words
            line = key_recognition(line)

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            if discriminator_num(line[0]):
                continue

            # chars
            temp = ''
            cnt = 0
            while(zfnfa.switch_state(line[cnt]) != False):
                temp = temp + line[cnt]
                cnt += 1
            if temp != '' and zfnfa.now_state == zfnfa.state_list[-1]:
                line = line[cnt:]
                write_into_file(temp[1:-1],"CHARCON")
                zfnfa.return_to_zero()

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            # sr: decide key words
            line = key_recognition(line)

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            if line[0] == "\'":
                continue

            # string
            temp = ''
            cnt = 0
            while(zfcnfa.switch_state(line[cnt]) != False):
                temp = temp + line[cnt]
                cnt += 1
            if temp != '' and zfcnfa.now_state == zfcnfa.state_list[-1]:
                line = line[cnt:]
                write_into_file(temp[1:-1],"STRCON")
                zfcnfa.return_to_zero()

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

            # sr: decide key words
            line = key_recognition(line)

            # sp: cleaning and deciding
            if line == '' or line == '\n':
                break
            line = self_cleaning(line)

lexical_analysis()


