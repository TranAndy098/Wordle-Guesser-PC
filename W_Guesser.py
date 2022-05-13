from tkinter import *
from tkinter import ttk
import random

root = Tk() 
root.geometry("525x350")
root.configure(background='gray20')
root.resizable(width=False, height=False)

f = open("words.txt", "r")
l = f.readline()
possible_words = []
while l != "":
    possible_words.append(l[:5])
    l = f.readline()

current_word = ""
word_entry = ""
click_action = ""
dis = ""
orig_words = possible_words

message_box = ""
attempt_box = ""
random_box = ""

letters_no_check = []
correct_letters = []

correctbox = []
green_val = []
green_buttons = []
yellow_val = []
yellow_buttons = []
done_button = ""
play_again_button = ""
random_button = ""
dark_mode = ""
light_mode = ""

wordle_banner = ""
guesser_banner = ""
enter_banner = ""
correct_banner = ""
message_banner = ""
random_banner = ""
attempted_banner = ""


def displays(list_words):
    global dis
    possible_words_scrolbar = Scrollbar(root) 
    possible_words_scrolbar.pack(side = RIGHT, fill = Y) 
    display_words = Listbox(root, yscrollcommand = possible_words_scrolbar.set, background="grey10",fg="white")  
    for words in possible_words: 
        display_words.insert(END, words)
    display_words.pack(side = LEFT, fill = BOTH )    
    word = random.choice(list_words)
    ins_msg(random_box,word)
    possible_words_scrolbar.config(command = display_words.yview)
    dis = display_words
    return display_words

def update_side(display_list,list_words):
    display_list.delete(0,END)
    for words in list_words: 
        display_list.insert(END, words)
    del_msg(random_box)
    try:
        word = random.choice(list_words)
    except:
        word = "No more words"
    ins_msg(random_box,word)
    

def text_entry():
    global word_entry
    global click_action
    global wordle_banner
    global guesser_banner
    global enter_banner
    global correct_banner
    enter_banner = Label(root, text='Your Entered Word:',background="grey20",fg="white")
    enter_banner.place(x=370, y=25 )
    correct_banner = Label(root, text='Correct Sequence:',background="grey20",fg="white")
    correct_banner.place(x=370, y=75 )
    wordle_banner = Label(root, text='Wordle', font = "30", background='gray20', fg="lime green")
    wordle_banner.place(x=165, y=0 )
    guesser_banner = Label(root, text='Guesser', font = "30", background='gray20', fg="gold")
    guesser_banner.place(x=235, y=0 )
    frame = Frame(root)
    frame.pack()
    frame.place(x=375, y=50 )
    message_log()
    attempt_log()
    
    def clicked(text):
        global current_word
        text = word_entry.get()
        if len(text) != 5 or text not in orig_words:
            del_msg(message_box)
            ins_msg(message_box, "Incorrect word choice")
        else:
            del_msg(message_box)
            current_word = text
            l = check_place()
            word_entry.config(state='disabled')
            word_entry.unbind('<Return>')
            ins_msg(attempt_box,text+"\n")
        word_entry.delete(0, END)
        word_entry.insert(0, "")
        
    word_entry = Entry(frame, width = 20)
    word_entry.bind('<Return>',clicked)
    click_action = clicked
    word_entry.pack()

def message_log():
    global message_box
    global message_banner
    frame = Frame(root)
    frame.pack()
    frame.place(x=375, y=150 )
    message_banner = Label(root, text='Message Log:',background="grey20",fg="white")
    message_banner.place(x=370, y=125 )
    my_entry = Entry(frame,width=20,background="grey10",fg="white")
    my_entry.pack()
    my_entry.config(state='disabled')
    message_box = my_entry
    return my_entry

def attempt_log():
    global attempt_box
    global attempt_banner
    frame = Frame(root)
    frame.pack()
    frame.place(x=150, y=200 )
    attempt_banner = Label(root, text='Attempted Words:',background="grey20",fg="white")
    attempt_banner.place(x=150, y=175 )
    my_entry = Text(frame,height=8,width=24,background="grey10",fg="white")
    my_entry.pack()
    my_entry.config(state='disabled')
    attempt_box = my_entry
    return my_entry

def random_word():
    global random_box
    global random_banner
    frame = Frame(root)
    frame.pack()
    frame.place(x=375, y=200 )
    random_banner = Label(root, text='Random Word Left:', background="grey20",fg="white")
    random_banner.place(x=370, y=175 )
    my_entry = Entry(frame,width=20,background="grey10",fg="white")
    my_entry.pack()
    random_box = my_entry
    my_entry.config(state='disabled')


def correctness():
    global correctbox
    for i in range(5):
        frame = Frame(root)
        frame.pack()
        frame.place(x=375 + (26*i), y=100)
        my_entry = Text(frame, width=2, height=1)
        my_entry.pack()
        my_entry.config(state='disabled')
        correctbox.append(my_entry)

def change_correct(my_entry,letter):
    my_entry.configure(background='green')
    my_entry.config(state='normal')
    my_entry.insert(END, letter)
    my_entry.config(state='disabled')

def remove_correct(my_entry):
    my_entry.configure(background='white')
    my_entry.config(state='normal')
    my_entry.delete("1.0", END)
    my_entry.config(state='disabled')

def ins_msg(my_entry, msg):
    my_entry.config(state='normal')
    my_entry.insert(END, msg)
    my_entry.config(state='disabled')

def del_msg(my_entry,num=0):
    my_entry.config(state='normal')
    my_entry.delete(num, END)
    my_entry.config(state='disabled')

def check_box():
    global green_val
    global green_buttons
    global yellow_val
    global yellow_buttons
    global possible_words
    global done_button
    dl = displays(possible_words)
    def dis_other():
        for i in range(5):
            if green_val[i].get() == 1:
                yellow_buttons[i].config(state='disabled')
            else:
                if current_word[i]+str(i) not in letters_no_check:
                    yellow_buttons[i].config(state='normal')

        for i in range(5):
            if yellow_val[i].get() == 1:
                green_buttons[i].config(state='disabled')
            else:
                if current_word[i]+str(i) not in letters_no_check:
                    green_buttons[i].config(state='normal')

    for i in range(5):
        greens = IntVar()
        text_label = "Letter " + str(i+1) + " Green"
        green_check = Checkbutton(root, command = dis_other, text=text_label, variable=greens, background='gray20', fg="lime green")
        green_check.pack()
        green_check.config(state='disabled')
        green_check.place(x=150, y=25 + (25 * i) )
        green_val.append(greens)
        green_buttons.append(green_check)

    for i in range(5):
        yellows = IntVar()
        text_label = "Letter " + str(i+1) + " Yellow"
        yellow_check = Checkbutton(root, command = dis_other, text=text_label, variable=yellows, background='gray20', fg="gold")
        yellow_check.pack()
        yellow_check.config(state='disabled')
        yellow_check.place(x=250, y=25 + (25 * i) )
        yellow_val.append(yellows)
        yellow_buttons.append(yellow_check)
    
    def done_push():
        global word_entry
        global click_action
        global done_button
        global possible_words
        global correct_letters
        new_words = []
        for i in range(5):
            if green_val[i].get() == 1:
                change_correct(correctbox[i],current_word[i])
                correct_letters.append(current_word[i])
        for letter in range(5):
            if current_word[letter]+str(letter) not in letters_no_check:
                letter_right_both = green_val[letter].get()
                letter_right_one = yellow_val[letter].get()
                for words in possible_words:
                    if letter_right_both == 1:
                        if words[letter] == current_word[letter]:
                            new_words.append(words)
                    elif letter_right_one == 1:
                        if current_word[letter] in words and words[letter] != current_word[letter]:
                            new_words.append(words)
                    elif letter_right_both == 0 and letter_right_one == 0:
                        if current_word[letter] not in words:
                            new_words.append(words)
                        elif current_word[letter] in words and words[letter] != current_word[letter] and current_word[letter] in correct_letters:
                            new_words.append(words)
                            
                possible_words = new_words
                new_words = []
            if green_val[letter].get() == 1:
                letters_no_check.append(current_word[letter]+str(letter))

            if yellow_val[letter].get() == 1:
                letters_no_check.append(current_word[letter]+str(letter))

            if green_val[letter].get() == 0 and yellow_val[letter].get() == 0 and current_word[letter]+str(letter) not in letters_no_check:
                letters_no_check.append(current_word[letter]+str(0))
                letters_no_check.append(current_word[letter]+str(1))
                letters_no_check.append(current_word[letter]+str(2))
                letters_no_check.append(current_word[letter]+str(3))
                letters_no_check.append(current_word[letter]+str(4))
        
        update_side(dl,possible_words)

        for i in range(5):
            green_buttons[i].config(state='disabled')
            green_val[i].set(0)
            yellow_buttons[i].config(state='disabled')
            yellow_val[i].set(0)

        word_entry.config(state='normal')
        word_entry.delete(0, END)
        word_entry.bind('<Return>',click_action)
        done_button["state"] = "disabled"
        #print(letters_no_check)
        #print(len(letters_no_check))
        #print(correct_letters)

    button_done = Button(root, text ="Done",width=27,height=1, command = done_push,background="grey10",fg="white")
    button_done.pack()
    button_done.place(x=150, y=150 )
    button_done["state"] = "disabled"
    done_button = button_done

def resuffle_button():
    global random_button
    def clicked():
        global random_box
        global possible_words
        del_msg(random_box)
        try:
            word = random.choice(possible_words)
        except:
            word = "No more words"
        ins_msg(random_box,word)
        
    button_random = Button(root, text ="Random Again",width=16,height=1,command=clicked, background="grey10",fg="white")
    button_random.pack()
    button_random.place(x=375, y=233 )
    random_button = button_random

def reset_button():
    global play_again_button
    def clicked():
        global dis
        global orig_words
        global current_word
        global possible_words
        global letters_no_check
        global attempt_box
        global correct_letters
        correct_letters = []
        current_word = ""
        my_entry = ""
        possible_words = orig_words
        del_msg(attempt_box,"1.0")
        letters_no_check = []
        update_side(dis,orig_words)
        for i in range(5):
            remove_correct(correctbox[i])
        for i in range(5):
            green_buttons[i].config(state='disabled')
            green_val[i].set(0)
            yellow_buttons[i].config(state='disabled')
            yellow_val[i].set(0)
        word_entry.config(state='normal')
        word_entry.delete(0, END)
        word_entry.bind('<Return>',click_action)
        done_button["state"] = "disabled"
        
        
    button_play_again = Button(root, text ="Play Again",width=16,height=1,command=clicked,background="grey10",fg="white")
    button_play_again.pack()
    button_play_again.place(x=375, y=270 )
    play_again_button = button_play_again

def dark_button():
    global dark_mode
    def clicked():
        """
        global root
        global word_entry
        global dis
        global message_box
        global attempt_box
        global random_box
        global correctbox
        global green_buttons
        global yellow_buttons
        global done_button
        global play_again_button
        global random_button
        global wordle_banner
        global guesser_banner
        global enter_banner
        global correct_banner
        global message_banner
        global random_banner
        global attempted_banner
        """
        root.configure(background='gray20')
        enter_banner.configure(background="grey20",fg="white")
        correct_banner.configure(background="grey20",fg="white")
        wordle_banner.configure(background='gray20')
        guesser_banner.configure(background='gray20')
        dis.configure(background="grey10",fg="white")  
        random_banner.configure(bg="grey20",fg="white")
        random_box.configure(background="grey10",fg="white")
        message_banner.configure(background="grey20",fg="white")
        message_box.configure(background="grey10",fg="white")
        attempt_banner.configure(background="grey20",fg="white")
        attempt_box.configure(background="grey10",fg="white")
        random_button.configure(background="grey10",fg="white")
        play_again_button.configure(background="grey10",fg="white")
        done_button.configure(background="grey10",fg="white")
        for i in range(5):
            green_buttons[i].configure(background='gray20')
            yellow_buttons[i].configure(background='gray20')
        
    button_dark = Button(root, text ="Dark",width=7,height=1,command=clicked, background="grey10",fg="white")
    button_dark.pack()
    button_dark.place(x=438, y=307 )
    dark_mode = button_dark

def light_button():
    global light_mode
    def clicked():
        root.configure(background='white')
        enter_banner.configure(background="white",fg="black")
        correct_banner.configure(background="white",fg="black")
        wordle_banner.configure(background='white')
        guesser_banner.configure(background='white')
        dis.configure(background="white smoke",fg="black")  
        random_banner.configure(bg="white",fg="black")
        random_box.configure(background="white smoke",fg="black")
        message_banner.configure(background="white",fg="black")
        message_box.configure(background="white smoke",fg="black")
        attempt_banner.configure(background="white",fg="black")
        attempt_box.configure(background="white smoke",fg="black")
        random_button.configure(background="white smoke",fg="black")
        play_again_button.configure(background="white smoke",fg="black")
        done_button.configure(background="white smoke",fg="black")
        for i in range(5):
            green_buttons[i].configure(background='white')
            yellow_buttons[i].configure(background='white')
        
        
    button_light = Button(root, text ="Light",width=7,height=1,command=clicked, background="white",fg="black")
    button_light.pack()
    button_light.place(x=375, y=307 )
    light_mode = button_light

def check_place():
    global green_buttons
    global yellow_buttons
    global done_button
    for i in range(5):
        if current_word[i]+str(i) not in letters_no_check:
            green_buttons[i].config(state='normal')
            yellow_buttons[i].config(state='normal')

    done_button["state"] = "normal"
    

def main_looped():
    root.mainloop()

def display_menu():
    random_word()
    check_box()
    text_entry()
    correctness()
    resuffle_button()
    reset_button()
    dark_button()
    light_button()
    main_looped()

display_menu()
