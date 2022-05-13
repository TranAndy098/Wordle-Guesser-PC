import random

f = open("words.txt", "r")
l = f.readline()
possible_words = []
while l != "":
    possible_words.append(l[:5])
    l = f.readline()

menu = "d: display words left \na: add attempt \nr: random possible word \np: play again(restart) \nq: quit\n"
current_right = "?????"
print(current_right)
option = input(menu)

no_need_check_letters = []
correct_letter_wrong_spot = []

orig_words = possible_words

while option != "q":
    if option == "d":
        length_checker = "Words left: " + str(len(possible_words)) + " , are you sure? y/n\n"
        display = input(length_checker)
        while display != "n":
            if display == "y":
                #print(possible_words)
                i = display_menu(possible_words)
                print(8)
                break
            else:
                length_checker = "invalid repsonse. " + length_checker
                display = input("invalid option, y or n only\n")

    elif option == "r":
        print(random.choice(possible_words))

    elif option == "p":
        possible_words = orig_words
        no_need_check_letters = []
        correct_letter_wrong_spot = []
        current_right = "?????"
    elif option == "a":
        word = input("what was attempt? (length of 5)\n")
        for i in range(5):
            if word[i] not in no_need_check_letters:
                if word[i] in correct_letter_wrong_spot:
                    correct_letter = "y"
                else:
                    ask_correct_letter = "is " + word[i] + " in the correct word? y/n\n"
                    correct_letter = input(ask_correct_letter)
                while correct_letter != "n":
                    if correct_letter == "y":
                        ask_correct_spot = "is " + word[i] + " in the correct spot? y/n\n"
                        correct_spot = input(ask_correct_spot)
                        while correct_spot != "n":
                            if correct_spot == "y":
                                new_possible_words = []
                                for words in possible_words:
                                    if word[i] == words[i]:
                                        new_possible_words.append(words)
                                possible_words = new_possible_words
                                no_need_check_letters.append(word[i])
                                current_right = current_right[:i] + word[i] + current_right[i+1:]
                                break
                            else:
                                ask_correct_spot = "invalid response. " + ask_correct_spot
                                correct_spot = input(ask_correct_spot)
                        if correct_spot == "n":
                            new_possible_words = []
                            for words in possible_words:
                                if (word[i] in words) and (word[i] != words[i]):
                                    new_possible_words.append(words)
                            possible_words = new_possible_words
                            correct_letter_wrong_spot.append(word[i])
                        
                        break
                    else:
                        ask_correct_letter = "invalid response. " + ask_correct_letter
                        correct_letter = input(ask_correct_letter)
                if correct_letter == "n":
                    new_possible_words = []
                    for words in possible_words:
                        if word[i] not in words:
                            new_possible_words.append(words)
                    possible_words = new_possible_words
                    no_need_check_letters.append(word[i])
        

    elif option == "q":
        break
    else:
        print("invalid option")
    print(current_right)
    option = input(menu)
