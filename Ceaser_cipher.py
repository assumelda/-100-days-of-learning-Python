# Building a ceaser cipher

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
cipher=False

# Creating a function for decrypting and encrypting

# def encrypt(message, shift):
#     cipher_text=""
#     for letter in message:
#         new_position=alphabet.index(letter)+shift
#         new_position%=len(alphabet)
#         cipher_text+=alphabet[new_position]
#     print(f"Here is the encoded result: \n{cipher_text}")
    
# def decrypt(message, shift):
#     cipher_text=""
#     for letter in message:
#         new_position=alphabet.index(letter)-shift
#         new_position%=len(alphabet)
#         cipher_text+=alphabet[new_position]
#     print(f"Here is the decoded result: \n{cipher_text}")

def encrypt_decrypt(message, shift, cryption):
    cipher_text=""
    for letter in message:
        
        if letter not in alphabet:
            cipher_text+=letter
        else:
            if cryption=="decode":
                new_position=alphabet.index(letter)-shift
            elif cryption=="encode":
                new_position=alphabet.index(letter)+shift
            new_position%=len(alphabet)
            cipher_text+=alphabet[new_position]
    print(f"Here is the {cryption}d result: \n{cipher_text}")
    
print("Welcome to the CEASER CIPHER!!!")

while not cipher:
    cryption=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    message=input("Type your message: \n").lower()
    shift=int(input("Type the Shift Number: "))
    encrypt_decrypt(message, shift, cryption) 
    again=input("Type 'yes' to go again. Otherwise type 'no'. ").lower()
    if again=="yes":
        cipher=False
    elif again=="no":
        cipher=True
        print("Goodbye!")
    else:
        print("You typed in the incorrect option, try again!!")
        again=input("Type 'yes' to go again. Otherwise type 'no'. ").lower()
        if again=="yes":
            cipher=False
        elif again=="no":
            cipher=True
            print("Goodbye!")
