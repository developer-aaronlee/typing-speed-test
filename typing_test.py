from tkinter import *
from tkinter import messagebox
import math


class TypingTest:
    def __init__(self, test):
        self.test = test
        # self.formatted_test = self.format_test()
        self.timer = 60
        self.test_chars = self.get_test_char(self.test)
        self.line_limit = 45
        self.test_lines = math.ceil(self.test_chars / self.line_limit)
        self.test_arr = self.get_test_arr(self.test)
        self.current_index = 0
        self.current_list = 0
        self.writable = True
        self.correct_count = 0
        # self.split_point = 0
        # self.current_word = self.get_current_word()

        self.window = Tk()
        self.window.title("Typing Speed Test")
        self.window.geometry("900x700")
        self.window.config(padx=50, pady=50, bg="pink")
        self.window.option_add("*Label.Font", "Arial 30")

        self.top_label = Label(width=65, text="Press <Return> To Start Test.", bg="pink", fg="purple", highlightbackground="pink")
        self.top_label.place(relx=0.5, rely=0.05, anchor=S)

        self.window.bind("<Return>", self.countdown_timer)

        self.test_label = Label(text=self.test_arr[self.current_list], bg="pink", fg="black", highlightbackground="pink")
        self.test_label.place(relx=0.03, rely=0.2)

        self.word_display = Label(text=self.test_arr[self.current_list][self.current_index], bg="pink", fg="black", highlightbackground="pink")
        self.word_display.place(relx=0.45, rely=0.35)

        self.test_entry = Entry(width=53, font="Arial 25", bg="white", fg="black", highlightbackground="pink")
        self.test_entry.place(relx=0.03, rely=0.55)

        self.restart_button = Button(text="Restart", font="Arial 30", bg="white", fg="pink", highlightbackground="pink", command=self.restart_test)
        self.restart_button.place(relx=0.42, rely=0.85)

        self.window.bind("<Key>", self.detect_keypress)

        self.window.mainloop()

    # def countdown_timer(self, *args, **kwargs):
    #     if self.timer > 0:
    #         self.timer -= 1
    #         self.top_label["text"] = self.timer
    #         self.window.after(1000, lambda: self.countdown_timer())

    def countdown_timer(self, *args, **kwargs):
        self.timer -= 1
        self.top_label["text"] = self.timer
        if self.timer >= 0:
            self.window.after(1000, self.countdown_timer)
        else:
            self.top_label["text"] = "Time's up! You score is {}"

    def get_test_char(self, test):
        count = 0
        for x in test:
            count += len(x)
        return count

    def get_test_arr(self, ori_test):
        test = [x.lower() for x in ori_test]
        test_arr = []
        line_arr = []
        count = 0
        for x in test:
            count += len(x)
            if count < self.line_limit:
                line_arr.append(x)
                if test.index(x) == len(test) - 1:
                    test_arr.append(line_arr)
            elif count == self.line_limit:
                line_arr.append(x)
                test_arr.append(line_arr)
                count = 0
                line_arr = []
            else:
                test_arr.append(line_arr)
                count = len(x)
                line_arr = [x]

        # for y in test_arr:
        #     char = 0
        #     for z in y:
        #         char += len(z)
        #     print(char)
        #
        # print(test_arr)

        return test_arr

    # def format_test(self):
    #     test_arr = [x.lower() for x in self.test]
    #     test_str = " ".join(test_arr)
    #     return test_str

    # def get_current_word(self):
    #     test_arr = self.formatted_test.split(" ")
    #
    #     print(test_arr)

    def detect_keypress(self, event=None):
        (entry_arr, entry_len) = self.get_test_entry()
        test_char_count = len(" ".join(self.test_arr[self.current_list]))
        test_current_len = len(" ".join(self.test_arr[self.current_list][:self.current_index + 1]))
        next_correct_arr = self.test_arr[self.current_list][:self.current_index + 1]
        print(next_correct_arr)

        if entry_arr == next_correct_arr and entry_len == test_current_len:
            self.current_index += 1
            self.word_display["text"] = self.test_arr[self.current_list][self.current_index]
        elif entry_arr != next_correct_arr and entry_len == test_current_len:
            self.current_index += 1
            self.word_display["text"] = self.test_arr[self.current_list][self.current_index]

        if entry_len == test_char_count:
            self.current_list += 1
            self.test_entry.delete(0, "end")
            self.test_label["text"] = self.test_arr[self.current_list]

    def get_test_entry(self):
        test_entry_str = self.test_entry.get()
        test_entry_len = len(test_entry_str)
        test_entry_arr = test_entry_str.split(" ")
        print(test_entry_arr)
        return test_entry_arr, test_entry_len

    def restart_test(self):
        pass


