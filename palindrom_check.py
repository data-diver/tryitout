def checking_palindrome (given_input_string):

   filtered_input = []

   for elem in given_input_string:
        if 'a' <= elem <= 'z' or 'A' <= elem <= 'Z' or '0' <= elem <= '9': 
            filtered_input.append(elem)
    

   filtered_string = ''.join(filtered_input)
   filtered_string.lower()

   print(type(filtered_string))

   if filtered_string == filtered_string[::-1]:
    print ('The input','"',given_input,'"','is palindrom')
   else:
    print ('The input','"',given_input,'"','is not palindrom')


string_input = input("Please Enter the word or phrase to check...")
checking_palindrome (string_input)
