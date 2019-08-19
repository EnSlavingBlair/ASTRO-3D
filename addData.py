# keep asking the user for input until the user inputs "end" (without the quotation marks)
# writes input data to file
running = True
while running:
    user_input = input("How many dice rolls to escape the Cosmic Microwave Background?")
    if user_input == "end":
        running = False
    if(user_input.isdigit()):
        with open("histData.txt", "a") as f:
            f.write(str(user_input)+"\n")
