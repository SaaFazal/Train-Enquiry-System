# TrainProject-N1249874-SahadhFazalMohamed
***

# Description:

The Train Enquiry Python project aims to provide 
users with a user-friendly platform to access train details 
and book their journeys. Based in Chennai, Tamil Nadu, 
the project allows users to view train information, including 
speed and schedule. Authorized Users can also add new trains, delete cancelled 
ones, or edit delayed ones. The project is based in Tamil Nadu, India, and is
designed to cater to the needs of travelers in the southern part of the country.
Additionally, the project aims to enhance the overall travel experience by providing
a user-friendly interface for booking journeys seamlessly.
The program primarily focuses on the efficient management of train details in files, 
enabling users to read, write, delete, and edit them as needed.

# Design:

To begin with, I imported a random library for later use, and 
I started my Train Enquiry program by creating

###Class:

I created the class by naming it Train, and after that, 
I created an init function having attributes of train number, 
train name, departure, arrival, arrival time, and departure time.

Then assign a variable for every attribute to make use of 
it throughout the whole program.

After creating the Train class and initializing its attributes, 
I proceeded to implement various methods within the class to handle 
different functionalities of the Train Enquiry program. These methods 
would allow users to search for train information, update train details,
and perform other relevant operations.

###Functions:
After creating classes, I started to create functions, which are the main 
part of the program. First, I created a function, save_train(), to save the
train details in a text file. 

####save_train():-
I have created an empty list called train_list to
save and access the train details whenever needed. To save the details, I have
created a text file (Trains.txt) that stores information about train_number, 
train_name, departure, arrival, arrival_time, and departure_time. I opened 
the file and set the mode to "w," which helps me add data whenever I want.

####load_train():-
The next and most important step is to load the file so that we can get the 
data of the train whenever the user needs something. Loading the file 
ensures that the train data is readily available for the user whenever it is 
required. This step is crucial for seamless access and utilization of the 
train information.
I have inserted a try and except block to check whether the file is uploaded in a folder; if not, it shows a FileNotFoundError.

I opened the file and changed the file mode to "r" in order to read the file.
And then I used the loop to read the train details line by line properly. 
After that, I typed a method [.split()], which reads the word separately. 
Finally, I added every train detail to the list (train_list) by using append function.

####add_train():-
I created an add function that allows users to add a new train if the 
train is coming for the first time or has been replaced by another train.
I created a variable for train number, train name, arrival, departure, arrival time, and departure time and also wrote an input function that allows us to get values from the user and add the details to the train_list.

After getting values, save the details in trains.txt by implementing the save_train() function.

####edit_train():-
Next I created an edit function called "edit_train," which allows 
users to edit the train details if the train gets delayed or arrives
sooner. I asked the user to input the train number that you want to edit, 
and if the train number matches the train number that is in the saved files, 
it asked the user to input new train details and update everything in the 
saved files.

####search_train():-
I created a search function called "search_trains," which allows users to search the train details completely in order to help them with their bookings.

It asks the train number that you want to search for; if the train number 
matches the train number in saved files, it will print you the full details 
of the train, and if not, it will show TRAIN DETAILS NOT FOUND.

####delete_train():-
I created a delete function that allows users to delete the train 
if it has been terminated permanently or cancelled. I asked the user 
for the train number that they want to delete. If the train number matches 
the train number in records, it will delete the whole train details.
I used [.remove()] here to delete the train details from "save_train."
If the train number does not match the record, it shows an error:
"TRAIN DETAILS NOT FOUND."

####display_all_trains():-
I created the next function, which is to display the
train details. This is one of the important functions 
because with it, users can see the train details. 
I have used a loop here to make the order vertically 
proper. And I printed the train number, train name, and
departure arrival. Then I called the load function to read it 
whenever the user wanted.

####book_tickets():-
Next is the main part of this train inquiry program, 
which is creating the "book_tickets" function, which allows
users to book their tickets. I have used the display function
in the first step so that users can see the trains that are 
arriving and departing in Chennai Egmore.

Next, I asked for the train number that they wanted to book,
and after that, the details of the customer, like name, phone number,
and address, were stored in a text file called "BookingDetails.txt.".

I have used a loop and started to write my main function. If the train number
the user typed matches the train number in records, it asks the user 
to put the number of tickets wanted only between (1 and 15) per single booking. 
The next price of the ticket is allocated, which is 1000 rupees in Indian
money. In the next line, I used the random function to allow only limited 
seats from 1 to 60.

After that, by using the if and elif methods, I managed to get the user's 
input successfully, allowing them to book their train tickets. 
And if the train number does not match, it shows an error: "TRAIN DETAILS NOT FOUND."

####speed_train():-
Next is to create the "speed_train" function, 
which allows the user to know the speed of their 
train. If the train number matches the train number 
in records, then it shows the current speed of the particular train.

####main():-
The most important step in this program is the "main()" function. 
This function contains every function, and it is also known as the 
user-interacting function. I have used a while loop here because it
will ask the user unless they break it. I displayed every option, 
from adding the trains to deleting them. It will ask the user to enter 
their choice from 1 to 8, with every number having one function. I used 
the if and elif methods to say he chose number 4 or number 5 for the 
computer, which brings the particular function to action according 
to the user's input. If the user wants to break the program, he can
select 8 to go out of the program or any other number other than 1 to 
7 to get an error message: "Invalid choice. Please try again."

####open_account():-
Now I want to create a username and password login to allow only 
authorized people to access it. So I created a function called 
"open_account()," which asks the user for the username and password. 
If the username or password doesn't match the records that are stored 
in "Access.txt," it will show an error and ask you to create a new username
and password. If the username and password match the record in "Access.txt,"
it will print "LOGIN SUCCESSFUL" and allow you to add a new train.

#USERNAME = Admin
#PASSWORD = admin

####create_account():-
The username and password you typed are incorrect. This "create_account()"
will help you add a new username and password by asking you for the new
username and password. Then it will store the details in the "Access.txt" file.

## USE CASE DIAGRAM
![img.png](img.png)
![image](https://olympuss.ntu.ac.uk/storage/user/1786/files/db9fee66-a098-4835-9080-59ef76e306d1)



## CLASS DIAGRAM
![img_1.png](img_1.png)
![image](https://olympuss.ntu.ac.uk/storage/user/1786/files/7a0c0a16-881a-4969-b427-f2f7673d6378)


#Testing:
Various numbers of tests were gone through, and here are the noted 
results from each test. The results varied significantly, with some
tests showing positive outcomes while others had negative or inconclusive
results. But in the end, I managed to pass everything.

![img_2.png](img_2.png)
![image](https://olympuss.ntu.ac.uk/storage/user/1786/files/c0fcc43d-def3-45dd-9629-28f5a3bc8663)

#Critique:

WHAT WORKED:

When I started this program, I had no idea because I didn't have any
proper planning. So the first thing I did was make a proper plan and
write down whatever I needed in it. Because of that, almost 70% of the
program worked very well on its first try. Like adding train details, 
updating train details, searching for train details, displaying train 
details, deleting train details, and finding the speed of the train. 
And also, I managed to create a text file that saved every detail and 
could be read whenever needed.

WHAT DIDN'T:

The hardest part of this program is creating the booking function, 
which took me way too long to finish. I made three errors in the 
booking function, which took half of my time away. But in the end, 
after finding out what the exact mistake was, I managed to clear up
every problem and finish the booking function. Furthermore, I had problems 
with creating an open account and a create account, which took some time as
well, but after referring to the resources in NOW, I have completed my project
perfectly. This caused the main function to cause an error, and I cleared that
as well.

Anything that could have improved:

I did my project very well, and the only thing I want to improve in my code
is arranging it in a more neat way. And I should have added more options for
users to access it elegantly.



