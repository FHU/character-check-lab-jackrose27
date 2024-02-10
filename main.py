#Remove pass and complete the code
def check_character(word, index):
   char_value = word[index]
   numbers = ("0","1","2","3","4","5","6","7","8","9")
   whitespace = " "
   alphabet = char_value.isalpha()

   if char_value == whitespace:
       return "white space"
   elif char_value in numbers:
       return "digit"
   elif alphabet == True:
       return "letter"
   else:
       return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
