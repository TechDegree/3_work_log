import os

from task import Task # import Task class, so it is accessible here


def clear():
    """Clears console."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_menu():
    """Displays worklog menu"""
    pass
    

def get_new_task():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    pass

def save_to_file():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    pass

def view_tasks():
    """[summary]

    Returns:
        [type] -- [description]
    """
    pass

def search_by_date():
    """[summary]
    
    Returns:
        [type] -- [description]
    """


def search_by_time():
    """[summary]
    
    Returns:
        [type] -- [description]
    """


def search_by_pattern():
    """[summary]

    Returns:
        [type] -- [description]
    """


def search_by_exact():
    """[summary]
    
    Returns:
        [type] -- [description]
    """












def main():
    """Asks user for choice of cypher and required data.
    Encrypts or decrypts the message and prints out to the screen
    """
    # available ciphers and their corresponding code names
    CIPHER_CODE_NAMES = {
        "A": "Affine",
        "AT": "Atbash",
        "C": "Ceasar",
        "K": "Keyword"
    }

    while True:
        clear()  # clear screen
        print(display_menu(CIPHER_CODE_NAMES))  # display menu choices
        # get correct cypher code
        cipher = get_cipher_choice(CIPHER_CODE_NAMES)
        clear()
        # what cipher is it? assign instance to cipher

        if cipher == "A":
            # ask for required parameters
            alpha = input("Enter an alpha value. Available values:"
                          ": 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"
                          "\n>>> ")
            while True:
                try:
                    alpha = int(alpha)
                    break
                except ValueError:
                    clear()
                    alpha = input("I do not think it is an integer. Try again."
                                  " Available values: 3, 5, 7, 9, 11, 15, 17,"
                                  " 19, 21, 23, 25\n>>> ")
                    continue

            while True:
                if alpha not in [3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
                    clear()
                    print('Alpha value is not within the range. Please try again.\n')
                    alpha = int(input("Available values: 3, 5, 7, 9, 11, 15, 17, 19"
                                      ", 21, 23, 25.\n>>> "))
                clear()
                break

            beta = input("Enter a beta value. Integers only.\n>>> ")

            while True:
                try:
                    beta = int(beta)
                    clear()
                    break
                except ValueError:
                    clear()
                    beta = input("Enter a beta value. Integers ONLY.\n>>> ")

            cipher_object = Affine(alpha, beta)
        elif cipher == "AT":
            cipher_object = Atbash()
        elif cipher == "C":
            cipher_object = Caesar()
        elif cipher == "K":
            # ask for the keyword
            key = input(
                "What keyword word would you like to use to en(de)crypt your message?\n>>> ")
            while True:
                # the key cannot be 0, as this will change nothing,
                # it can be non alphabet characters
                if len(key) > 1:
                    break
                else:
                    clear()
                    key = input(
                        "You need at least one character, although the more the better.\n>>>")
            cipher_object = Keyword(key)

        clear()
        encode_decode = input(
            "I see, That is a good choice."
            "\nAre we encoding (E) or decoding (D) a message?\n>>> ").upper()

        while encode_decode not in ["E", "D"]:
            clear()
            encode_decode = input("This is not a valid choice."
                                  "\nWe can encode (E) or decode (D)\n>>> ").upper()

        clear()
        message = input(
            "Got it! I see what you are doing there.\n"
            "What is the secret message?\n>>> ")

        # decrypt or encrypt the message
        en_de_message = run_cipher(cipher_object, message, encode_decode)

        # display secret message
        clear()
        print("Your original message: \n{}\n".format(message.upper()))
        print("This is your secret message:\n{}\nKeep it safe!\n".format(en_de_message))

        # run again or quit
        run_again = input(
            "Would you like to have another go? [N/y]\n>>> ").lower()
        if run_again != 'y':
            clear()
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
