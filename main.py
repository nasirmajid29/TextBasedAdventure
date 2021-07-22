# def intro():
#   print('You log off and leave labs. It is 2am and after a very long session of debugging, '
#        'you finally found the bug. (It was a 1 instead of a 0 :/)\n'
#       'Making your way to the exit you are filled with happiness at the thought of sleep. You attempt to open'
#      ' the door, but it is locked\n')
#
#   print()
#  print('----------------------------')
# print('| WELCOME TO HUXLEY HORROR |')
# print('----------------------------')

# 308
# 311 - abbas writing on the board

import time
import simple
import advanced

answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Grabbing objects
sword = 0
flower = 0

homework = 0
exit_key = 0

required = ("\nUse only A, B, or C\n")


# Cutting down on duplication

# The story is broken into sections, starting with "intro"
def intro():
    print("After a very long session of debugging, you log off and leave labs. It is 2am and\n" +
          "you finally found the bug. Making your way to the exit you are filled with happiness\n" +
          "at the thought of sleep. A cloud of terror wafts over you as you realised there is\n" +
          "discrete maths homework due tomorrow and you haven't even started.\n"
          "What do you do?:")
    time.sleep(1)
    print("""
    A. Do homework now
    B. Wake up early tomorrow to do it
    C. Don't do homework.
    """)
    choice = input(">>> ")  # Here is your first choice.
    if choice in answer_A:
        option_HWnow()
    elif choice in answer_B:
        option_HWlater()
    elif choice in answer_C:
        print("\nYou go home and get some well deserved rest\n"
              "You walk into your discrete maths lecture and\n"
              "Steffen asks for your homework. You tell him\n"
              "you haven't done it. He is not mad just disappointed.\n"
              "\nRethink your life choices.\n")
    else:
        print(required)

        intro()


def option_rock():
    print("\nThe orc is stunned, but regains control. He begins "
          "running towards you again. Will you:")
    time.sleep(1)
    print("""
      A. Run
      B. Throw another rock
      C. Run towards a nearby cave
      """)
    choice = input(">>> ")
    if choice in answer_A:
        option_run()
    elif choice in answer_B:
        print("\nYou decided to throw another rock, as if the first "
              "rock thrown did much damage. The rock flew well over the "
              "orcs head. You missed. \n\nYou died!")
    elif choice in answer_C:
        option_cave()
    else:
        print(required)
        option_rock()


def option_cave():
    print("\nYou were hesitant, since the cave was dark and "
          "ominous. Before you fully enter, you notice a shiny sword on "
          "the ground. Do you pick up a sword. Y/N?")
    choice = input(">>> ")
    if choice in yes:
        sword = 1  # adds a sword
    else:
        sword = 0
    print("\nWhat do you do next?")
    time.sleep(1)
    print("""  A. Hide in silence
      B. Fight
      C. Run""")

    choice = input(">>> ")
    if choice in answer_A:
        print("\nReally? You're going to hide in the dark? I think "
              "orcs can see very well in the dark, right? Not sure, but "
              "I'm going with YES, so...\n\nYou died!")
    elif choice in answer_B:
        if sword > 0:
            print("\nYou laid in wait. The shimmering sword attracted "
                  "the orc, which thought you were no match. As he walked "
                  "closer and closer, your heart beat rapidly. As the orc "
                  "reached out to grab the sword, you pierced the blade into "
                  "its chest. \n\nYou survived!")
        else:  # If the user didn't grab the sword
            print("\nYou should have picked up that sword. You're "
                  "defenseless. \n\nYou died!")
    elif choice in answer_C:
        print("As the orc enters the dark cave, you sliently "
              "sneak out. You're several feet away, but the orc turns "
              "around and sees you running.")
        option_run()
    else:
        print(required)
        option_cave()


def option_run():
    print("\nYou run as quickly as possible, but the orc's "
          "speed is too great. You will:")
    time.sleep(1)
    print("""  A. Hide behind boulder
        B. Trapped, so you fight
        C. Run towards an abandoned town""")
    choice = input(">>> ")
    if choice in answer_A:
        print("You're easily spotted. "
              "\n\nYou died!")
    elif choice in answer_B:
        print("\nYou're no match for an orc. "
              "\n\nYou died!")
    elif choice in answer_C:
        option_town()
    else:
        print(required)
        option_run()


def option_town():
    print("\nWhile frantically running, you notice a rusted "
          "sword lying in the mud. You quickly reach down and grab it, "
          "but miss. You try to calm your heavy breathing as you hide "
          "behind a delapitated building, waiting for the orc to come "
          "charging around the corner. You notice a purple flower "
          "near your foot. Do you pick it up? Y/N")
    choice = input(">>> ")
    if choice in yes:
        flower = 1  # adds a flower
    else:
        flower = 0
    print("You hear its heavy footsteps and ready yourself for "
          "the impending orc.")
    time.sleep(1)
    if flower > 0:
        print("\nYou quickly hold out the purple flower, somehow "
              "hoping it will stop the orc. It does! The orc was looking "
              "for love. "
              "\n\nThis got weird, but you survived!")
    else:  # If the user didn't grab the sword
        print("\nMaybe you should have picked up the flower. "
              "\n\nYou died!")


# intro()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    intro()
    # choice = input("Simple or Advanced?")

    # steffen with homework
    # do it now, wake up early tommorrow and do it, don't do it.

# i got dropped on my head as a child - exit or stay in labs
# easy - svb
# medium - mark
# hard - kgk
# expert - tony
# insane - alice herslef
