def print_file():
    retry = True
    while True:
        try:
            filename = input('Type filename: ')
            with open(filename,'r') as f:
                print(f.read())
            break
        except IOError:
            print('IO Error. Something did not work.')
            if input('Would you like to retry? (y/N) ').upper() != 'Y':
                break
    print('End.')

if __name__ == '__main__':
    print_file()

