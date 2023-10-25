
def encoder(password):
    string = ''
    for i in range(len(password)):
        string = string + str(int(password[i]) + 3)
    return string



while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')
    option = input('Please enter an option: ')
    if option == '1':
        password = input('Please enter your password to encode: ')
        encoded_password = encoder(password)
        print('Your password has been encoded and stored!\n')
    elif option == '2':
        # decoded_password = decoder(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is ')
    elif option == '3':
        quit()





