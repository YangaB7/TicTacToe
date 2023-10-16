array1 = ["□", "□", "□", "□", "□", "□", "□", "□", "□"]

xTurn = True

def printBoard():
    for i in range(0, len(array1), 3):
        print(" ".join(array1[i:i+3]))
    
printBoard()

while("□" in array1):

    while True:
        selectSlot = input("Your Turn: ")
        
        if selectSlot.isdigit():  # Check if the input is a digit.
            selectSlot = int(selectSlot)  # Convert the input to an integer.
            
            if 1 <= selectSlot <= 9:  # Check if the input is within the desired range.
                break  # Exit the loop if the input is valid.
            else:
                print("Please enter a number between 1 and 9.")
        else:
            print("Please enter a valid number.")

    index = selectSlot - 1

    if(array1[index] == "□"):
        if(xTurn):
            array1[index] = "X"
            xTurn = False
        elif(not xTurn):
            array1[index] = "O" 
            xTurn = True
    else:
        print("Slot Occupied. Choose another!") 
    
    printBoard()

    if(array1[0] == array1[1] == array1[2] == "O" or 
        array1[3] == array1[4] == array1[5] == "O" or 
        array1[6] == array1[7] == array1[8] == "O" or 
        array1[0] == array1[4] == array1[8] == "O" or 
        array1[2] == array1[4] == array1[6] == "O" or
        array1[0] == array1[3] == array1[6] == "O" or
        array1[1] == array1[4] == array1[7] == "O" or
        array1[2] == array1[5] == array1[8] == "O"):
        print("Circle Wins!!")
        break
    if(array1[0] == array1[1] == array1[2] == "X" or 
        array1[3] == array1[4] == array1[5] == "X" or 
        array1[6] == array1[7] == array1[8] == "X" or 
        array1[0] == array1[4] == array1[8] == "X" or 
        array1[2] == array1[4] == array1[6] == "X" or
        array1[0] == array1[3] == array1[6] == "X" or
        array1[1] == array1[4] == array1[7] == "X" or
        array1[2] == array1[5] == array1[8] == "X"):
        print("Cross Wins!!")
        break

if all(slot != "□" for slot in array1):
    print("Cat's Game!!")

#win logic
# if(array1[0] == array1[1] == array1[2] == "O" or array1[3] == array1[4] == array1[5] == "O" or array1[6] == array1[7] == array1[8] == "O" or array1[0] == array1[4] == array1[8] == "O" or array1[2] == array1[4] == array1[6] == "O"):
#     print("Circle Wins!!")
# if(array1[0] == array1[1] == array1[2] == "X" or array1[3] == array1[4] == array1[5] == "X" or array1[6] == array1[7] == array1[8] == "X" or array1[0] == array1[4] == array1[8] == "X" or array1[2] == array1[4] == array1[6] == "X"):
#     print("Cross Wins!!")

#Old Logic
    # if(selectSlot == 1):
    #     if array1[0] == "C":
    #         if(xTurn):
    #             array1[0] = "X"
    #             xTurn = False
    #         elif(not xTurn):
    #             array1[0] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()
    
    # if(selectSlot == 2):
    #     if(array1[1] == 'C'):
    #         if(xTurn):
    #             array1[1] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[1] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()

    # if(selectSlot == 3):
    #     if(array1[2] == 'C'):
    #         if(xTurn):
    #             array1[2] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[2] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 
        
    #     printBoard()

    # if(selectSlot == 4):
    #     if(array1[3] == "C"):
    #         if(xTurn):
    #             array1[3] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[3] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()
        
    # if(selectSlot == 5):
    #     if(array1[4] == "C"):
    #         if(xTurn):
    #             array1[4] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[4] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()
        
    # if(selectSlot == 6):
    #     if(array1[5] == "C"):
    #         if(xTurn):
    #             array1[5] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[5] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()

    # if(selectSlot == 7):
    #     if(array1[6]):
    #         if(xTurn):
    #             array1[6] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[6] = "O" 
    #             xTurn = True 
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()

    # if(selectSlot == 8):
    #     if(array1[7] == "C"):
    #         if(xTurn):
    #             array1[7] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[7] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()

    # if(selectSlot == 9):
    #     if(array1[8] == "C"):
    #         if(xTurn):
    #             array1[8] = "X"
    #             xTurn = False 
    #         elif(not xTurn):
    #             array1[8] = "O" 
    #             xTurn = True
    #     else:
    #         print("Slot Occupied. Choose another!") 

    #     printBoard()