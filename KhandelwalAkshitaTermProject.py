#!/usr/bin/env python
# coding: utf-8

# In[3]:


# using try and except block so as to handle all potential errors which might be encountered during query execution
try:
    # using this command to view the contents of the student data file 
    f=open('Students.txt', 'r')
    
    # using readline method to read each line of student data file
    f.readline()
    
    # creating an empty list that will store students data
    list_of_students=[]
    
    #creating a for loop to iterate all the records 
    for line in f:
        
        # using strip method to remove trailing and leading spaces from each record 
        line=line.strip()
        
        # using split method to separate one record from another
        student= line.split('\t')
        
        # using append function to keep inserting the student records into the student data list
        list_of_students.append(student)
        
    # using this to display the list storing student data   
    print(list_of_students)
    
#checking for any exemption if the user uploaded the incorrect file, then the error message pops up
except:
    print('Please enter a valid file name')


# In[4]:



# creating a main function
def Main():
    # print statement to welcome user to the student query tool
    print('Welcome to SQT - A user friendly Student Query Tool\n')
    
    print('-------------------------------------------------------------------------------------------------------')
    
    # print statement to display list of available student data related functions which the tool can perform based on user choice 
    print('Press 1 to display all, Press 2 to students by sirname, Press 3 to display students with grad year, Press 4 to display summary,Press 0 to quit')
    
    
    
    print('-------------------------------------------------------------------------------------------------------')
    
    
    # using input function to ask user which query out of the above 5 they would like to perform
    user_choice=input('Please enter your choice: ')
    
    
    # using try and except block so as to handle all potential errors which might be encountered during query execution
    try:
        # assigning variable choice to the integer value of the query option chosen by the user
        choice= int(user_choice)
        
    # checking for any exception wherein if user enters a negative value by mistake then error message should pop up
    except:
        choice=-1
    return choice

# creating a function to display all student records 
def display_all():
    
    # using for loop to iterate each list value
    for x in list_of_students: #x=['101010', 'Lee', 'Shane', '2019', 'Spring', 'MSA']
        
        # using print statement to display all student data attributes using indices
        print(x[0],x[1],x[2],x[3],x[4],x[5])
        
# creating a function to display students whose last name begins with a certain string (case insensitive) 
def display_sirname():
    
    # using input function to ask user to enter a part of their last name as a string value
    letter= input('Enter the letter: ') 
    
    # using for loop to iterate over student data list
    for x in list_of_students: 
        
        # using lower function to convert last name string entered by user into lowercase so that it is case insensitive
        letter=letter.lower()
        
        # converting the entire last name value to lower case and saving it in a new variable
        low_x=x[1].lower()
        
        # using if condition to check if last name value matches with the entered string by user
        if low_x.startswith(letter): 
        
            # using print statement to display all student data attributes using indices
            print(x[0],x[1],x[2],x[3],x[4],x[5])
       
        
# creating a function to display all records for students whose graduating year is a certain year 
def display_gradyear():
    
    # using input function to ask user about the graduating year 
    year= input('Enter the graduating year from 2019 to 2021: ') #2019
    
    #if condition to have a range for year that user can input for the given data
    if int(year)>2018 and int(year)<2022: 

    # using for loop to iterate over the student data list
        for x in list_of_students:

            # if condition to check if the 4 index position of the list matches with the year value entered by the user
            if x[3]==year: 

                # using print statement to display all student data attributes using indices
                print(x[0],x[1],x[2],x[3],x[4],x[5])

    #giving message to inform user there is no data found for year mentioned by him mistakenly
    else: 
            print('You entered the year out of range.')
    

# creating a function to display a summary report of number and percent of students in each program, for students graduating on/afte            
def display_summary():
    
    # using input function to ask user about the graduating year
    year= input('Enter the year from 2019 to 2021: ')
    
    #if condition to have a range for year that user can input for the given data
    if int(year)>2018 and int(year)<2022:
    
        # assigning initial values of 0 to the number of students in a particular program
        count_MSA=0
        count_MSBA=0
        count_MSSD=0
        count_MSGF=0
        count_MSIT=0
        count_MSM=0
        count_MSMI=0
        count_MSMM=0
        count_MST=0
        count_MSSC=0
        count_MBA=0
        count_MBAP=0
        count_MBAE=0
        total=0
        # using for loop to iterate over student data list
        for x in list_of_students:

            # if condition to check if graduation year from the student data matches with the year entered by the user
            if x[3]>=year:
                total+=1

                # when program value matches then number of students count is increased by 1 for the respective program
                if x[5]=='MSA':
                    count_MSA+=1
                elif x[5]=='MSBA':
                    count_MSBA+=1
                elif x[5]=='MSSD':
                    count_MSSD+=1
                elif x[5]=='MSGF':
                    count_MSGF+=1
                elif x[5]=='MSIT':
                    count_MSIT+=1
                elif x[5]=='MSM':
                    count_MSM+=1
                elif x[5]== 'MSMI':
                    count_MSMI+=1
                elif x[5]== 'MSMM':
                    count_MSMM+=1
                elif x[5]=='MST':
                    count_MST+=1
                elif x[5]== 'MSSC':
                    count_MSSC+=1
                elif x[5]== 'MBA':
                    count_MBA+=1
                elif x[5]=='MBAP':
                    count_MBAP+=1
                elif x[5]=='MBAE':
                    count_MBAE+=1

        # using print statements to display number of students and the percentage of students in a particular program            
        print('the number of students in MSA:',count_MSA,'the percentage of MSA students:', count_MSA/total)
        print('the number of students in MSBA:',count_MSBA,'the percentage of MSBA students:', count_MSBA/total)
        print('the number of students in MSSD:',count_MSSD,'the percentage of MSSD students:', count_MSSD/total)
        print('the number of students in MSGF:',count_MSGF,'the percentage of MSGF students:', count_MSGF/total)
        print('the number of students in MSIT:',count_MSIT,'the percentage of MSIT students:', count_MSIT/total)
        print('the number of students in MSM:',count_MSM,'the percentage of MSM students:', count_MSM/total)
        print('the number of students in MSMI:',count_MSMI,'the percentage of MSMI students:', count_MSMI/total)
        print('the number of students in MSMM:',count_MSMM,'the percentage of MSMM students:', count_MSMM/total)
        print('the number of students in MST:',count_MST,'the percentage of MST students:', count_MST/total)
        print('the number of students in MSSC:',count_MSSC,'the percentage of MSSC students:', count_MSSC/total)
        print('the number of students in MBA:',count_MBA,'the percentage of MBA students:', count_MBA/total)
        print('the number of students in MBAP:',count_MBAP,'the percentage of MBAP students:', count_MBAP/total)
        print('the number of students in MBAE:',count_MBAE,'the percentage of MBAE students:', count_MBAE/total)
    
    #giving message to inform user there is no data found for year mentioned by him mistakenly
    else:
        print('Invalid year')

        
        
        
# checking the value of input given by user for running a query using the student query tool
final_choice=Main()

# using while loop to check which function to run when based on the input given by the user
while final_choice!=0:
    #assigning a message to handle a error if by mistake user input negative values
    if final_choice==-1:
        print('Invalid choice')
    elif final_choice==1:
        display_all()
    elif final_choice==2:
        display_sirname()
    elif final_choice==3:
        display_gradyear()   
    elif final_choice==4:
        display_summary()    
    #assigning the range where user cannot use all the interger value, if a user pressed a wrong number
    elif final_choice>4 or final_choice<-1:
        #error message for not choosing the range provided above
        print('Invalid input choice.Enter again.')
    final_choice=Main()
    
# using print statement to give send a thank you note to the user for using the SQT tool        
print('Thank you for using SQT - Student Query Tool')     


# In[ ]:





# In[ ]:




