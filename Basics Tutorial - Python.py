#This is a comment.
#Comments are ignored during code activation.

print("The shell will print what is contained within this area.")
var = input("var will now become a variable that can be called upon later. var is now:")
print(var)
#This will print the text in the variable "var" and require a response.
#input asks for a response to the text provided.

if var == "a variable":
    print("Correct! Nice job.")
elif var == "why should I care":
    print("Now, now, you WANT to pass thic class, right? Right???")
else:
    print("Come on, the answer was right there in front of you!")
#This will cause different text to print based on your answer to the input text.
#If you answer correctly, the "if" statement will trigger, if you don't, "else" will trigger.

print("=-" * 30)
#This is a good way to make a divider, which will separate the printed text in the shell between before this point and after this point.

#Now, here's an example of all these components in action!

#Input Section
name = input("Your name:")
color = input("Your favorite color:")
sport = input("Favorite sport, if any:")
hobby = input("Favorite hobby:")
thundurus = input("PokeDex #642:")

#Divider
print("=-" * 60)

#Output
print("Your name is... " + name + "!")
print("Your favorite color is... " + color + "!")
print("Your favorite sport is... " + sport + "!")
print("Your favorite hobby is... " + hobby + "!")

if thundurus == "Thundurus":
    print("That's right! Totally didn't use Google, right? =)")
elif thundurus == "Bulbasaur":
    print("That's #1. You were close, though, only 641 Pokemon off!")
else:
    print("Nope. That's fine, though, I didn't really expect you to know this off the top of your head.")
#Divider
print("=-" * 30)

#When this is used, a fully interactive questionnaire will start, which will ask you about your name, favorite color/sport/hobby, and what #642 in the PokeDex is.
#Try it out if you want!

#With this, you should have a basic understanding of "print", "input", variables and dividers. You should also understand if, elif, and else statements.
