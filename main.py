#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""
firstly, we open our invited_names file as read mode, than use the .readlines() method to transform all the name
contents of that file in a list format.
"""
with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_names = names.readlines()


"""
Then we open the starting letter as read mode and use the .read() method to assign it's contents to the letter_model
variable.
"""
with open("./Input/Letters/starting_letter.txt", mode='r') as starting_letter_file:
    letter_model = starting_letter_file.read()

"""
last we create a for loop to loop through every name in the list, strip it, cause when we used the .readlines() method
earlier it included \n in the list cause of the way the invited_name.txt was disposed. Once we have the the name strip
and clean without any other char, we initialise a new variable and use the .replace() method to replace the [name] 
placeholder of the letter model to the name we're looping through. Than we finish it by using the write mode of the open
method to create a new letter and assign the personalized_named_letter contents to this new file
"""
for name in list_of_names:
    name = name.strip()

    personalized_named_letter = letter_model.replace("[name]", name)

    with open(f"Letter_to_{name}.txt", mode="w") as new_letter:
        new_letter.write(personalized_named_letter)
