import random
class Train:
    def __init__(self, train_number, train_name, departure, arrival,arrival_time, departure_time):
        self.train_number = train_number
        self.train_name = train_name
        self.departure = departure
        self.arrival = arrival
        self.arrival_time = arrival_time
        self.departure_time = departure_time
def save_train(train_list):
    file = open('Trains.txt', 'w')
    for train in train_list:
        file.write(f"{train.train_number},{train.train_name},{train.departure},{train.arrival},{train.arrival_time},{train.departure_time}\n")

def load_train():
    train_list = []
    try:
        file = open('Trains.txt', 'r')
        for line in file:
            train_data = line.strip().split(',')
            train = Train(*train_data)
            train_list.append(train)
        return train_list
    except FileNotFoundError:
        print("File Does not exist!!!")
def add_train():
    train_number = input("Enter Train Number: ")
    train_name = input("Enter Train Name: ")
    arrival = input("Enter the Arrival destination: ")
    departure = input("Enter the Departure destination: ")
    arrival_time = input("Enter Arrival Time: ")
    departure_time = input("Enter Departure Time: ")

    new_train = Train(train_number, train_name, departure, arrival,arrival_time, departure_time)
    train_list.append(new_train)
    save_train(train_list)
    print("TRAIN ADDED SUCCESSFULLY!!")

def edit_train(train_number,train_list):
    for train in train_list:
        if train.train_number == train_number:
            train.train_name = input("Enter New Train Name: ")
            train.arrival = input("Enter the New Arrival destination: ")
            train.departure = input("Enter the New Departure destination: ")
            train.arrival_time = input("Enter New Arrival Time: ")
            train.departure_time = input("Enter New Departure Time: ")
            save_train(train_list)
            print("TRAIN DETAILS UPDATED SUCCESSFULLY")
            return
    print("TRAIN NOT FOUND")

def search_train(train_number):
    for train in train_list:
        if train.train_number == train_number:
            print(f"Train Number: {train.train_number}")
            print(f"Train Name: {train.train_name}")
            print(f"Departure: {train.departure}")
            print(f"Arrival: {train.arrival}")
            print(f"Arrival Time: {train.arrival_time}")
            print(f"Departure Time: {train.departure_time}")
            return
    print("TRAIN DETAILS NOT FOUND")

def delete_train(train_number, train_list):
    for train in train_list:
        if train.train_number == train_number:
            train_list.remove(train)
            save_train(train_list)
            print("TRAIN DETAILS DELETED SUCCESSFULLY")
            return
    print("TRAIN DETAILS NOT FOUND")

def display_all_trains():
    for train in train_list:
        print(f"{train.train_number}: {train.train_name} : {train.departure} : {train.arrival} ")
train_list = load_train()

def book_ticket(train_list):
    display_all_trains()
    train_number = input("Enter the Train Number you want to book: ")
    name = input("Enter the name for booking ticket: ")
    phone = int(input("Enter Your Contact Details: "))
    address = input("Enter Your Address: ")

    book = open("BookingDetails.txt","w")
    book.write(f"{name} : {phone} : {address}")
    book.close()

    for train in train_list:
        if train.train_number == train_number:
            number_of_tickets = int(input("Enter The Number of Tickets you want to book(1-15): "))

            price_of_ticket = 1000        #price in indian money 1000rs
            Availabe_seats = random.randint(0, 61)
            print(f"There are Currently only {Availabe_seats} seats left")
            if number_of_tickets <= 0:
                print("INVALID SELECTION")
            elif number_of_tickets <= 15:
                total_price = number_of_tickets * price_of_ticket
                print(f"YOUR TRAIN TICKET IS BOOKED !!!\n TOTAL AMOUNT IS {total_price}Rs \n Thank you have a great journey")
                print(f"YOUR COACH NUMBER IS {random.randint(1, 50)}")
                print("A COACH CONTAINS 60 SEATS")
                print("YOUR SEAT NUMBER WILL BE ON YOUR TICKET, THAT WILL BE SENT TO YOUR PHONE ON THE JOURNEY DAY!!!")

            elif number_of_tickets > Availabe_seats:
                print("SORRY THE TRAIN IS CURRENTLY FULL NOW")
            else:
                print("SORRY ONLY 15 TICKETS ARE ALOWED AT ONE SINGLE BOOKING")

            break
    else:
        print("THE TRAIN NUMBER YOU MENTIONED IS NOT FOUND. SORRY!!")

def speed_train(train_number,train_list):
    for train in train_list:
        if train.train_number == train_number:
            print(f"THIS TRAIN {train_number} going in a speed of {random.randint(50,150)} MPH ")
            return
    print("TRAIN DOES NOT EXIT")
def create_account():
    Access = open("Access1.txt","w")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    Access.write(f"{new_username}:{new_password}\n")
    Access.close()
    print("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY")
    #create_account()
    open_account()
def open_account():
    Access=open('Access1.txt','r')
    existing_username=input("Enter your username: ")
    existing_password=input("Enter your password: ")
    for line in Access:
        username, password = line.strip().split(':')
        if existing_username == username and existing_password == password:
            print("LOGIN SUCCESSFUL")
            add_train()
        else:
            print("INCORRECT USERNAME OR PASSWORD")
            new=input("DO YOU WANT TO CREATE A NEW USERNAME AND PASSWORD (yes/no): ")
            if new.lower() in 'yes':
                create_account()
            else:
                print("YOU CANT LOGIN HERE!!! SORRY")
                break


    Access.close()
#open_account()
def main():
    while True:
        print(""
              ""
              ""
              "Welcome to Chennai Egmore Railway Station (சென்னை எழும்பூர் ரயில் நிலையம்) \n Railways makes the arrival faster (ரயில்வே விரைவாக வருகை தருகிறது)\n"
              "TRAIN TIMING BOARD TODAY (04 - 12 - 2023)\n"
              "1. To display all the trains that are arriving and departing from chennai egmore railway station\n"
              "2. To add a new train to the board\n"
              "3. To edit a train from the board\n"
              "4. To search the train from the board\n"
              "5. To Delete a train from the board\n"
              "6. To Book Your Ticket\n"
              "7. To see the speed of train\n"
              "8. EXIT ")
        choice = input("Enter your choice: ")

        if choice == '1':
            display_all_trains()
        elif choice == '2':
            Authorization = input("Are you an authorized person from train community (yes)/(no) : ")
            if Authorization.lower() == 'yes':
                open_account()

            else:
                print("Sorry You cant Add the train details!!")
        elif choice == '3':
            display_all_trains()
            train_number = input("Enter the train number you need to edit: ")
            edit_train(train_number,train_list)
        elif choice == '4':
            display_all_trains()
            train_number = input("Enter Train Number to search: ")
            search_train(train_number)
        elif choice == '5':
            display_all_trains()
            train_number = input("Enter the Train Number you want do delete: ")
            delete_train(train_number,train_list)
        elif choice == '6':
            book_ticket(train_list)
        elif choice == '7':
            display_all_trains()
            train_number = input("Enter the Train Number to see the speed of the Train: ")
            speed_train(train_number,train_list)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


main()