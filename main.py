from classes import *
import json

print("Welcome to the UH Pool Table Booking App!")

##### ONLY EDIT THIS IF THE NUMBER OF TABLES OR PRICE PER HOUR CHANGES #####

number_of_tables = 12
cost_per_hour = 30

##### ONLY EDIT THIS IF THE NUMBER OF TABLES OR PRICE PER HOUR CHANGES #####

#Create Pool Table objects with PoolTable class and add each tavle to the tables list

tables = []
log = []

for i in range(1, number_of_tables + 1):
    table = PoolTable(i)
    tables.append(table)

while True:

#Present user with a main menu

    choice = input("""
Please make a selection from the main menu.

1 - View Tables
2 - Check Out a Table
3 - Check In a Table
Q - Quit Application

Your Selection: """)

    #Option 1: Allow user to view all tables and their status. If the table is occupied, display the start time and duration of play.

    if choice == '1':

        print("\nCURRENTY VIEWING ALL TABLES\n")

        for table in tables:

            if table.occupied == False:
                print(f"{table.name}: \tAVAILABLE")

            if table.occupied == True:
                current_time = datetime.datetime.now().replace(microsecond = 0)
                duration = current_time - table.startTime
                print(f"{table.name}: \tOCCUPIED | Check out time: {table.startTime} | Time played: {duration}")

    #Option 2: Display available tables and allow user to enter a Table # to check out. If selected table is occupied, prevent user from checking out and display a message.
    #When checking out a table, change availability status and record start time.

    elif choice == '2':

        print("\nViewing All AVAILABLE Tables\n")

        for table in tables:

            if table.occupied == False:
                print(f"{table.name}")

        try:
            index = int(input("\nEnter Table # to check out: ")) - 1

            if index >= len(tables):
                print("\nPlease enter a valid Table number.")

            else:
                table = tables[index]

                if table.occupied == True:
                    print(f"\n{table.name} is currently occupied. Please choose a different table.")

                else:
                    table.check_out()
                    print(f"\n{table.name} checked out at {table.startTime}.")

        except ValueError:
            print("\nPlease enter a valid Table number.")

    #Option 3: Display occupied tables and allow user to enter a Table # to check in. If selected table is not currently checked out, display message. 
    #When checking in a table, change availability status, record end time, and calculate total cost rounded up to the nearest quarter hour.
    #Create a log in .txt and/or .json format with reservation details (table #, start and end times, duration of play, and cost).

    elif choice == '3':

        print("\nViewing All OCCUPIED Tables\n")

        for table in tables:

            if table.occupied == True:
                print(f"{table.name}")

        try:
            index = int(input("\nEnter Table # to check in: ")) - 1

            if index >= len(tables):
                print("\nPlease enter a valid Table number.")

            else:
                table = tables[index]

                if table.occupied == False:
                    print(f"\n{table.name} is not currently checked out.")

                else:
                    table.check_in()

                    duration = table.endTime - table.startTime
                    minutes = duration.total_seconds() / 60
                    rounded_hours = (15 - (minutes % 15) + minutes) / 60
                    total_cost = format(rounded_hours * cost_per_hour, '.2f')

                    print(f"\n{table.name} checked in at {table.endTime}. Total time played is {duration}.")
                    print(f"Total amount due is ${total_cost}.")
                    
                    today = datetime.date.today()
                    with open(f"{today}.txt", "a") as file:
                        file.write(f"""
{table.name}
Start time: {table.startTime}
End time: {table.endTime}
Duration: {duration}
Cost: ${total_cost}
                        """)

                    reservation = {
                    "tableName": f"{table.name}",
                    "Start time": f"{table.startTime}",
                    "End time": f"{table.endTime}",
                    "Duration": f"{duration}",
                    "Cost": f"${total_cost}"
                    }

                    log.append(reservation)
                    with open(f"{today}.json", "w") as file:
                        json.dump(log, file)
                        

        except ValueError:
            print("\nPlease enter a valid Table number.")

    #Option 4: Quit application

    elif choice == 'q':
        break

    #Print error message if input is not valid.

    else:
        print("\nInput not recognized. Please enter a valid selection.")
