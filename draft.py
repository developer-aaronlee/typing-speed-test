# from tkinter import *
# import random
# import tkinter
#
# # Setup
# root = Tk()
# root.title('Type Speed Test')
#
# # Setting the starting window dimensions
# root.geometry('700x700')
#
# # Setting the Font for all Labels and Buttons
# root.option_add("*Label.Font", "consolas 30")
# root.option_add("*Button.Font", "consolas 30")
#
# def resetWritingLabels():
#     # Text List
#     possibleTexts = [
#         'For writers, a random sentence can help them get their creative juices flowing. Since the topic of the sentence is completely unknown, it forces the writer to be creative when the sentence appears. There are a number of different ways a writer can use the random sentence for creativity. The most common way to use the sentence is to begin a story. Another option is to include it somewhere in the story. A much more difficult challenge is to use it to end a story. In any of these cases, it forces the writer to think creatively since they have no idea what sentence will appear from the tool.',
#         'The goal of Python Code is to provide Python tutorials, recipes, problem fixes and articles to beginner and intermediate Python programmers, as well as sharing knowledge to the world. Python Code aims for making everyone in the world be able to learn how to code for free. Python is a high-level, interpreted, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.',
#         'As always, we start with the imports. Because we make the UI with tkinter, we need to import it. We also import the font module from tkinter to change the fonts on our elements later. We continue by getting the partial function from functools, it is a genius function that excepts another function as a first argument and some args and kwargs and it will return a reference to this function with those arguments. This is especially useful when we want to insert one of our functions to a command argument of a button or a key binding.'
#     ]
#     # Chosing one of the texts randomly with the choice function
#     text = random.choice(possibleTexts).lower()
#
#     # defining where the text is split
#     splitPoint = 0
#     # This is where the text is that is already written
#     global labelLeft
#     labelLeft = Label(root, text=text[0:splitPoint], fg='grey')
#     labelLeft.place(relx=0.5, rely=0.5, anchor=E)
#
#     # Here is the text which will be written
#     global labelRight
#     labelRight = Label(root, text=text[splitPoint:])
#     labelRight.place(relx=0.5, rely=0.5, anchor=W)
#
#     # This label shows the user which letter he now has to press
#     global currentLetterLabel
#     currentLetterLabel = Label(root, text=text[splitPoint], fg='grey')
#     currentLetterLabel.place(relx=0.5, rely=0.6, anchor=N)
#
#
# resetWritingLabels()


even_arr = [lambda arg=x: arg * 10 for x in range(1, 5)]
even_lst = [x() for x in even_arr]
# print(even_lst)

max_num = lambda a, b: a if a > b else b
# print(max_num(1, 2))

lst = [5, 3, 1]
# print(sorted(lst))

li1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list1 = filter(lambda x: (x % 2 != 0), li1)
lst1 = [x for x in final_list1]
# print(lst1)

li2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list2 = list(map(lambda x: x * 2, li2))
# print(final_list2)

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum_num = reduce(lambda x, y: x + y, li)
# print(sum_num)

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

listToStr = " ".join(map(str, s))
print(listToStr)



