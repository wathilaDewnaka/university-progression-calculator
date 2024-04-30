# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20220955, w2052736

# Date: 12/12/2023
#--------------------------------------------PROGRAMME-----------------------------------------------------
#Importing the graphics module
from graphics import *
import datetime

#Creating the function to display the main menu
def main_menu():
    print("-"*90)
    print("\nHi, Welcome to University predict progression calculator\n") #Display user greeting message
    print("-"*90 + "\n")

    while True: #Getting user input wheather student or staff member
        user = input("Enter who you are (Student / Staff) : ").strip().lower()
        if user == 'staff' or user == 'student':
            print(f"You are logged in as : {user.capitalize()}")
            break
        else: #If invalid input asking again
            print("Invalid Input !, Please enter again wheather you are Student or Staff") 
            print("-"*90 + "\n")
            
    print("-"*90 + "\n")
    return user

#Creating the function to get the user inputs
def get_user_inputs(count,input_type,input_list,list_outcome_store,progress_count,trailer_count,retriever_count,exclude_count):
    while count < 3:
        try:
            get_input = int(input(f"Please enter your credits at {input_type[count]}: "))
        except ValueError:
            print("Integers required\n")
            continue
        outcome,get_input, count, input_list,progress_count,trailer_count,retriever_count,exclude_count = input_validity_check(list_outcome_store,get_input,count,input_list,progress_count,trailer_count,retriever_count,exclude_count)
    return list_outcome_store,progress_count,trailer_count,retriever_count,exclude_count
    
#Creating the function to check the validity of the inputs
def input_validity_check(list_outcome_store,get_input,count,input_list,progress_count,trailer_count,retriever_count,exclude_count):
    outcome = None
    if get_input < 0 or get_input > 120 or get_input % 20 != 0: #Checking whether inputs are in the range
        print("Out of range\n")

    else: #If input is valid appending the input to a list
        input_list.append(get_input)
        count += 1

    if count == 3: #If count = 3 (which means after last input) check for the outcome
        progress_count,trailer_count,retriever_count,exclude_count,outcome = check_outcome(input_list,progress_count,trailer_count,retriever_count,exclude_count) #Calling funtion to get outcome
        if outcome == None or sum(input_list) != 120 :
            print("Totally incorrect\n")
            input_list = []
            count = 0
        else:
            list_outcome_store.append(f"{outcome} - {str(input_list).replace('[','').replace(']','')}")
            print(f"{outcome}\n")
    return outcome,get_input,count,input_list,progress_count,trailer_count,retriever_count,exclude_count

#Creating the function containing all the credit criteria's
def check_outcome(input_list,progress_count,trailer_count,retriever_count,exclude_count):
    if input_list[0] == 120:
        outcomes = "Progress"
        progress_count += 1
    elif input_list[0] == 100:
        outcomes = "Progress (module trailer)"
        trailer_count += 1
    elif 0 <= input_list[2] <= 60:
        outcomes = "Module retriever"
        retriever_count += 1
    elif input_list[2] >= 80:
        outcomes = "Exclude"
        exclude_count += 1
    else:
        outcomes = None
    return progress_count,trailer_count,retriever_count,exclude_count,outcomes #Returning the outcome based on credits

#Creating a function to restart and ask another data set
def get_new_set():
    while True:
        try:
            #Asking for input to enter another data set
            new_set = input("Would you like to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results: ").strip().lower()
            if new_set == 'y' or new_set == 'q':
                break #Breaking loop if user entered y or q
            else:
                raise Exception()  #If wrong input raising an Exception
        except:
            print("\n" + "-"*90 + "\nPlease enter 'y' or 'q' again\n" + "-"*90 + "\n") #If an exception continuing the loop again
            continue
    return new_set 

#Creating a function to display the histogram
def display_histogram(bar_height):#Getting the bar_height as input parameters
    label = ["Progress","Trailer","Retriever","Exclude"] #Creating the bar labels
    label_point = [130,290,455,617] #Creating the label cordinates
    bar_points_x = [200,360,520,680] #Creating the bar cordinates
    bar_points_y = [70,230,390,550]
    bar_colors = [(174,248,161),(160,198,137),(167,188,119),(210,182,181)] #Creating the colors
    count_points = [130,290,455,615] #Creating the count text cordinates
    
    max_number = max(bar_height[0],bar_height[1],bar_height[2],bar_height[3]) #Scaling the graph according to Max Height
    
    graph_window = GraphWin("Histogram", 750, 580) #Creating the window
    header = Text(Point(184, 40), "Histogram Results") #Creating the header
    header.setSize(20) #Setting the text size to 20
    header.setStyle("bold") #Setting to Bold text
    header.setFill(color_rgb(98,98,98)) #Filling the text with color using RGB values
    header.draw(graph_window) #Displaying the header

    line = Line(Point(730,501),Point(30,501)) #Creating the line at bottom
    line.setWidth(2) #Increasing the line widht
    line.draw(graph_window) #Displaying the line
    
    for i in range(len(bar_height)): #Running a loop till bar height           
        label_text = Text(Point(label_point[i],515),label[i]) #Creating the label text
        label_text.setStyle("bold") #Setting it to bold
        label_text.setSize(14) #Setting size
        label_text.setFill(color_rgb(125,135,151)) #Adding color

        count_text = Text(Point(count_points[i],488 - bar_height[i] * 400 / max_number), f"{bar_height[i]}")
        count_text.setStyle("bold")
        count_text.setSize(14)
        count_text.setFill(color_rgb(125,135,151))

        bar = Rectangle(Point(bar_points_x[i],500),Point(bar_points_y[i],500 - bar_height[i] * 400 / max_number))
        bar.setFill(color_rgb(*bar_colors[i]))
        
        bar.draw(graph_window)
        count_text.draw(graph_window)
        label_text.draw(graph_window)

    total_outcome = Text(Point(210, 540), f"{sum(bar_height)} outcomes in total.") #Displaying the total outcomes
    total_outcome.setSize(18) #Setting the text size to 18
    total_outcome.setStyle("bold")
    total_outcome.setFill(color_rgb(125,135,151))
    total_outcome.draw(graph_window) #Display the total outcome

    try:
        graph_window.getMouse()
        graph_window.close()
    except:
        graph_window.close()

#Creating the function to display summary
def display_console(list_outcome_store):
    print("Part 2 : ") #Displaying the summary to the user by list
    for element in list_outcome_store:
         print(element)

#Creating the function to read and write the data to the text file
def read_write_textfile(list_outcome_store):
    current_datetime = datetime.datetime.now() #Getting the curret datetime
    formatted_datetime = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") 
    #Writing to textfile
    with open(f"{formatted_datetime}.txt", "w") as file: #Opening the text file and writing the data
        file.write(f"Part 3 : \n")
        for element in list_outcome_store:
            file.write(f"{element}\n")

    #Reading the text file
    print("\n" + "-"*90 + "\n")
    file = open(f"{formatted_datetime}.txt","r")
    print(file.read().strip())
    file.close()
    
#----------------------------------------------------MAIN PROGRAMME------------------------------
def main():
    list_outcome_store = [] #List to store all the outputs
    input_type = ["PASS", "DEFER", "FAIL"] #List contain of input criteria
    progress_count = 0 #Total count of Progre #ss
    trailer_count = 0 #Total count of Trailer
    retriever_count = 0 #Total count of Retriever
    exclude_count = 0 #Total count of Exclude

    user = main_menu() #Calling for function to print the main menu
    
    #Starting the main loop
    while True: 
        input_list = [] #List to store the relavent user inputs
        count = 0 #Main count

        #Part 1 - Calculating and displaying the Progression outcome
        list_outcome_store,progress_count,trailer_count,retriever_count,exclude_count = get_user_inputs(count,input_type,input_list,list_outcome_store,progress_count,trailer_count,retriever_count,exclude_count) #Calling the main function and getting the user inputs

        if user == 'staff': #If user is staff can enter another data set
            new_set = get_new_set() #Calling for function to restart the calculator
        else:
            print("-"*90 + "\n")
            print("You Terminated the Programme (Student)\n")
            #Even a student giving the summary in Text file and displaying it
            #Part 2 - Displaying the data in console window
            display_console(list_outcome_store) #Calling for the function to display outcome summary

            #Part 3 - Calling for the function to write the data into text file and display summary
            read_write_textfile(list_outcome_store) #Calling for the function to read and write summary to text file   
            break

        if new_set == 'y': #If 'y' entered restating the programme
            print("\n" + "-"*90 + "\n" + "You enterted 'y' and you can enter another set of data\n" + "-"*90 + "\n")
            continue
            
        elif new_set == 'q': #If 'q' entered quiting the programme and showing summary
            print("\n" + "-"*90 + "\n" + "You enterted 'q' and you are quiting the program\n" + "-"*90 + "\n")
            print("You Terminated the Programme (Staff)\n")
            #Histogram 
            bar_heights = [progress_count,trailer_count,retriever_count,exclude_count] #Adding the elements to List
            display_histogram(bar_heights) #Calling for the function to display the Histogram
            
            #Part 2 - Displaying the data in console window
            display_console(list_outcome_store) #Calling for the function to display outcome summary

            #Part 3 - Calling for the function to write the data into text file and display summary
            read_write_textfile(list_outcome_store) #Calling for the function to read and write summary to text file
            break #Exiting the main loop
        
    print("\n" + "-"*90 + "\n")
    print("You have quited the program") #Printing to the user that user quited the programme successfully
    print("\n" + "-"*90)
    
main() #Calling for the main function
