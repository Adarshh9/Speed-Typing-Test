from wonderwords import RandomSentence
from colorama import init,Fore,Style
import time

init()
def typing_speed():
    def convert_to_colored(text):
        colored_text = ''
        for char in text:
            if user == generated_sentence:
                colored_text = Fore.GREEN + char + Style.RESET_ALL
            else:
                colored_text = Fore.RED + char + Style.RESET_ALL
        return colored_text


    sen1 = RandomSentence()
    generated_sentence = sen1.sentence()
    print(generated_sentence)

    print("Type To Start")
    start_time= time.time()
    user = input()
    stop_time= time.time()

    for char in user:
        output = convert_to_colored(char)
        print(output, end='')


    time_for_typing = stop_time - start_time  
    minutes = time_for_typing / 60          
    length_of_sentence = len(user)
    speed = int(length_of_sentence / minutes)

    if user == generated_sentence:
        print(f"\nSpeed of typing :{speed}")
    else:
        print("\nRETRY!!!\n")
        typing_speed()

typing_speed()

