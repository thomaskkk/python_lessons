from mail_merger import MailMerger
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


mail_merger = MailMerger()
mail_merger.read_template("./Input/Letters/starting_letter.txt")
mail_merger.read_names("./Input/Names/invited_names.txt")
mail_merger.generate_letters("./Output/ReadyToSend/")
