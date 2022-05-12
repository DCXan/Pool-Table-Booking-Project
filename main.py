from classes import *
import datetime


print("Welcome to the UH Pool Table Booking App!")

##### ONLY EDIT THIS IF THE NUMBER OF TABLES CHANGES #####

number_of_tables = 12
tables = []

for i in range(1, number_of_tables + 1):
    table = PoolTable(i)
    tables.append(table)

##### ONLY EDIT THIS IF THE NUMBER OF TABLES CHANGES #####

while True:

    choice = input("""
Please make a selection from the main menu.

1 - View Tables
2 - Check Out a Table
3 - Check In a Table
Q - Quit Application

Your Selection: """)


    if choice == '1':

        print("\nCURRENTY VIEWING ALL TABLES\n")

        for table in tables:

            if table.occupied == False:
                print(f"{table.name}: \tAVAILABLE")

            if table.occupied == True:
                current_time = datetime.datetime.now().replace(microsecond = 0)
                duration = current_time - table.startTime
                print(f"{table.name}: \tOCCUPIED | Check out time: {table.startTime} | Time played: {duration}")


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
                    print(f"\n{table.name} checked in at {table.endTime}. Total time played is {duration}.")

                    today = datetime.date.today()
                    with open(f"{today}.txt", "a") as file:
                        file.write(f"""
    {table.name}
    Start time: {table.startTime}
    End time: {table.endTime}
    Duration: {duration}
    """)

        except ValueError:
            print("\nPlease enter a valid Table number.")

    elif choice == 'q':
        break

    else:
        print("\nInput not recognized. Please enter a valid selection.")
