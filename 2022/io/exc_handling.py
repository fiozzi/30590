def print_file():
    retry = True
    while True:
        filename = input('Type filename: ')
        try:
            with open(filename,'r') as f:
                print(f.read())
            # a = b
            break
        except IOError:
            print('IO Error. Something did not work.')
            if input('Would you like to retry? (y/N) ').upper() != 'Y':
                break
        except Exception as e:
            print(e)
            break
    print('End.')

def test_try(number):
    try:
        a = 3/number
    except Exception as e:
        print(e)
        print('Exiting error.')
    else:
        print(a)
        print('Doing other stuff.')

if __name__ == '__main__':
    test_try(0)

