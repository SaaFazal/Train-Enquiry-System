def create_account():
    Access = open("Access.txt","w")
    new_username = input("Enter the new username: ")
    new_password = input("Enter the new password: ")
    Access.write(f"{new_username}:{new_password}\n")
    Access.close()
    print("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY")
#create_account()

def open_account():
    Access=open('Access.txt','r')
    existing_username=input("Enter your username: ")
    existing_password=input("Enter your password: ")
    for line in Access:
        username = line.strip().split(':')
        password = line.strip().split(':')
        if existing_username == username and existing_password == password:
            print("LOGIN SUCCESSFUL")
            #main()
        else:
            print("INCORRECT USERNAME OR PASSWORD")
            new=input("DO YOU WANT TO CREATE A NEW USERNAME AND PASSWORD (yes/no): ")
            if new.lower() in 'yes':
                create_account()
            else:
                print("YOU CANT LOGIN HERE!!! SORRY")
                break
    Access.close()
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
    file = open('Trains.txt', 'r')
    for line in file:
        train_data = line.strip().split(',')
        train = Train(*train_data)
        train_list.append(train)
    return train_list
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
    print("Train added successfully!")

def delete_train(train_list):
    pass

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
    print("Train not found.")

def display_all_trains():
    for train in train_list:
        print(f"{train.train_number}: {train.train_name} : {train.departure} : {train.arrival} : {train.departure_time} : {train.arrival_time}")
train_list = load_train()

while True:
    print("Welcome to Chennai Egmore Railway Station (சென்னை எழும்பூர் ரயில் நிலையம்) \n Railways makes the arrival faster (ரயில்வே விரைவாக வருகை தருகிறது)\n"
          "1. To display all the trains that are arriving and departing from chennai egmore railway station\n"
          "2. To add a new train to the board\n"
          "3. To edit a train from the board\n"
          "4. To search the train from the board\n"
          "5. EXIT ")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_all_trains()
    elif choice == '2':
        Authorization = input("Are you an authorized person from train community (yes)/(no) : ")
        if Authorization.lower() == 'yes':
            open_account()
            add_train()
        else:
            print("Sorry You cant Add the train details!!")
    elif choice == '3':
        delete_train(train_list)
    elif choice == '4':
        display_all_trains()
        train_number = input("Enter Train Number to search: ")
        search_train(train_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")


