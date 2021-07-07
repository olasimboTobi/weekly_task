from art import art


print(art)



#Encryption Function
def encrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    key = int(key)

    for i in text:
        if not i.islower() :
            encrypted += i
        
        if i in alphabet:
            index_alphabet = alphabet.index(i)
            if (index_alphabet + key) > len(alphabet) - 1:
                diff = (len(alphabet) - 1) - index_alphabet
                encrypted += alphabet[(key-diff) - 1]
            else:
                encrypted += alphabet[index_alphabet+key]

    return encrypted



#Decryption Function
def decrypt(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    key = int(key)
    for i in text:
        if not i.islower():
            decrypted += i

        if i in alphabet:
            index_alphabet = alphabet.index(i)
            if (index_alphabet - key) > len(alphabet) - 1:
                diff = (len(alphabet) - 1) + index_alphabet
                decrypted += alphabet[(key+diff) - 1]

            else:
                decrypted += alphabet[index_alphabet - key]
    

    return decrypted








def cryptography():    
    
    
    prompt = input("Do you want to encode or decode:").lower()

    while True:
        try:
            if prompt!= 'encode'and prompt != "decode":
                if prompt == '':
                    prompt = input('You are wrong enter either encode or decode').lower() 
                if prompt.isdigit:
                    prompt = input('You are wrong enter either encode or decode').lower()
                    raise Exception
        
        
        except Exception:
            print("Please enter either encode or decode")
            
        
        else:
            
            if prompt == "encode":
                text = input("Enter Text to Encode:")
                 
                key = input("Enter Encryption Key: ")
                while True:
                    try:
                        if key == "" or key.isspace():
                            key = "0"
                        if not key.isdigit() : #or int(key) not in range(1, 11):
                            key =input(" key must be a number\n enter again")
                        if int(key) > 10:
                            key = input("the key is not in range")
                        else:
                             # call encrpytion method
                             result_encrypt = encrypt(text, key)
                             print(f"This is the is the encrypted text: %s" % (result_encrypt))
                    except:
                        print("Please enter a valid key, that is digit")

                    
                    else:
                         
                         # continued operation  option
                        try_again = input("Do you want to perform another action? Yes or No: ").lower()
                        if try_again == "no":
                            print("Thank you for using our cryptography app")
                            exit()
                        else:
                            # go back to cryptography
                            cryptography()
            
            else:
                
                if prompt == "decode":
                    text = input("Enter Text to decode:")
                    
                    key = input("Enter decryption Key: ")
                    while True:
                        try:
                            if key == "" or key.isspace():
                                key = "0"
                            if not key.isdigit() : #or int(key) not in range(1, 11):
                                key =input(" key must be a number\n enter again")
                            if int(key) > 10:
                                key = input("the key is not in range")
                            else:
                                # call decrpytion method
                                result_decrypt = decrypt(text, key)
                                print(f"This is the is the encrypted text: %s" % (result_decrypt))
                        except:
                            print("Please enter a valid key, that is digit")

                        
                        else:
                            
                            # continued operation  option
                            try_again = input("Do you want to perform another action? Yes or No: ").lower()
                            if try_again == "no":
                                print("Thank you for using our cryptography app")
                                exit()
                            else:
                                # go back to cryptography
                                cryptography()
                        
            

            


        

cryptography()
