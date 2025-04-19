import datetime

def update_total_budget(amount, operations='add'):
    global total_budget
    if operations == "add":
        total_budget += amount
    elif operations == "subtract":
        total_budget -= amount


def edit_record(entry):
    while True:
        edit_rec_menu = int(input("Insert '1' to edit amount, '2' to edit category, '3' to edit description, '4' to edit payment method, '5' to exit out of record: "))
        
        if edit_rec_menu == 1:
            new_amt_enter = float(input("Insert amount spent or added: "))
            new_amt_value = {'Amount Entered': new_amt_enter}
            entry['Amount Entered'] = new_amt_value['Amount Entered']
            print("Action sucessful.")

        elif edit_rec_menu == 2:
            new_cat = input("Insert a category (e.g. food, transport, utilities): ")
            new_cat_value = {'Category': new_cat}
            entry['Category'] = new_cat_value['Category']
            print("Action sucessful.")

        elif edit_rec_menu == 3:
            new_desc = input("Insert a description for entry: ")
            new_desc_value = {'Description': new_desc}
            entry['Description'] = new_desc_value['Description']
            print("Action sucessful.")

        elif edit_rec_menu == 4:
            new_pay = input('Insert a pay method (e.g. cash, card, check): ')
            new_pay_value = {'Payment Method': new_pay}
            entry['Payment Method'] = new_pay_value['Payment Method']
            print("Action sucessful.")

        elif edit_rec_menu == 5:
            quit_edit = input("Are you sure you want to exit out of the edit menu (Y/N)?: ")
            if quit_edit == 'Y' or quit_edit == 'y':
                main_app()
            elif quit_edit == 'N' or quit_edit == 'n':
                edit_record()

        else:
            print("Invalid command.")


entries = []
total_budget = 0.0

def main_app():
    while True:
        global total_budget
        print("Expense Tracker")
        print(f"Total Budget: {total_budget:.2f}")

        menu_input = int(input("Insert '1' to add a record, '2' to delete a record, '3' to show records, '4' to edit records, '5' to exit application: "))

        if menu_input == 1:
            amt_enter = float(input("Insert amount spent or added: "))
            category = input("Insert a category (e.g. food, transport, utilities): ")
            desc = input("Insert a description for entry: ")
            pay_method = input("Insert a pay method (e.g. cash, card, check): ")
            current_date = datetime.date.today()
            formatted_date = current_date.strftime("%Y-%m-%d") #Formats the date as YYYY-MM-DD
            update_total_budget(amt_enter, "add")  # Update total budge
            entry = {'Amount Entered': amt_enter, 'Category': category, 'Description': desc, 'Payment Method': pay_method, 'Formatted Date': formatted_date}
            entries.append(entry)
            print(f"-- ENTRY ADDED --\nFormatted Date: {entry['Formatted Date']}\nAmount Entered: {entry['Amount Entered']}\nCategory: {entry['Category']}\nDescription: {entry['Description']}\nPayment Method: {entry['Payment Method']}")
        elif menu_input == 2:
            try:
                if not entries:
                    print("You have nothing to delete.")
                elif entries:
                    for i, entry in enumerate(entries,1):
                        print(f"Entry {i}.\nFormatted Date: {entry['Formatted Date']}\nAmount Entered: {entry['Amount Entered']}\nCategory: {entry['Category']}\nDescription: {entry['Description']}\nPayment Method: {entry['Payment Method']}")
                    index = int(input("Select record with the corresponding number to delete: "))
                    if  1 <= index <= len(entries):
                        del_entry = entries.pop(index-1)
                        update_total_budget(del_entry['Amount Entered'], "subtract")  # Update total budget
                        print(f"Entry Deleted.\nFormatted Date: {del_entry['Formatted Date']}\nAmount Entered: {del_entry['Amount Entered']}\nCategory: {del_entry['Category']}\nDescription: {del_entry['Description']}\nPayment Method: {del_entry['Payment Method']}")
                    else:
                        print(f"Must be a number between 1 and {len(entries)}.")
                else:
                    print("Command must be a number.")
            except ValueError:
                print("Invalid.")
        elif menu_input == 3:
            if not entries:
                print("You have no records.")
            elif entries:
                for i, entry in enumerate(entries, 1):
                    print(f"Entry {i}.\nFormatted Date: {entry['Formatted Date']}\nAmount Entered: {entry['Amount Entered']}\nCategory: {entry['Category']}\nDescription: {entry['Description']}\nPayment Method: {entry['Payment Method']}")
            else:
                print("Invalid command.")

        elif menu_input == 4:
            if not entries:
                print("You have no entries to edit.")
            elif entries:
                for i, entry in enumerate(entries, 1):
                    print(f"Entry {i}.\nFormatted Date: {entry['Formatted Date']}\nAmount Entered: {entry['Amount Entered']}\nCategory: {entry['Category']}\nDescription: {entry['Description']}\nPayment Method: {entry['Payment Method']}")
                index = int(input("Select corresponding number of entry that you would like to edit: "))
                if 1 <= index <= len(entries):
                    select_entry = entries[index-1]
                    print(f"Entry {i}.\nFormatted Date: {select_entry['Formatted Date']}\nAmount Entered: {select_entry['Amount Entered']}\nCategory: {select_entry['Category']}\nDescription: {select_entry['Description']}\nPayment Method: {select_entry['Payment Method']}")
                    edit_record(entry)

                else:
                    print("Invalid command.")
            else:
                print("Invalid command.")
            
        elif menu_input == 5:
            exit_app = input("Are you sure you want to exit application (Y/N)?: ")
            if exit_app == 'Y' or exit_app == 'y':
                print("See you next time.")
                exit()
            elif exit_app == 'N' or exit_app == 'n':
                break
        
        else:
            print("Invalid command.")

main_app()