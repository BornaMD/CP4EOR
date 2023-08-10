from random import randint


# The amount of money that will be processed each time
# taken from randint()
CHECKING_MONEY = randint(0, 1000)
SAVINGS_MONEY = randint(0, 1000)


def die(why):

    """Kill the program."""

    print("{} Exiting..")
    quit(1)


def broke(excuse, money):

    """You're broke!"""

    print("{}. ${} available in account.".format(excuse, money))


def formatter():

    """Shouldn't have to explain this.."""

    return '-' * 50


def prompt(info):

    """Prompt for information"""

    return raw_input(info)


def check_if_true(money):

    """Make sure there's money in the accounts."""

    if money > 0:
        return True
    else:
        return False


def check_account(money):

    """Function to check account balance."""

    print ("${} currently available in account".format(money))
    choice = prompt("Main Menu? ").lower()
    if 'yes' in choice:
        welcome_screen()
    else:
        die("Goodbye.")


def transfer_funds(checking, savings):

    """Function to transfer funds back and forth from accounts."""

    total = checking + savings
    check = check_if_true(total)
    # If the check returns true then continue with the function
    if check == True:
        print("""
    [ 1 ] Checking account to Savings account
    [ 2 ] Savings account to Checking account
    [ 3 ] Return to Main Menu
        """)

        choice = int(prompt("Which account: "))
        print(formatter())  # formatting makes everything pretty

        if choice == 1:
            print("Currently ${} in Checking account.".format(checking))
            amount = int(prompt("Enter amount to transfer to Savings account: $"))
            if amount > checking:  # Only allow an amount less than the amount in checking
                print("You do not have that much money.")
                transfer_funds(checking, savings)
            else:
                checking -= amount
                savings += amount
                print "${} withdrawn from Checking and added to Savings.".format(amount)
                print "${} left in Checking account.".format(checking)
                print "${} now in Savings account.".format(savings)
                choice = prompt("Transfer more funds? ").lower()
                print formatter()
                if 'no' in choice:
                    die("Goodbye.")
                    print formatter()
                else:
                    transfer_funds(checking, savings)  # recursively loop back to the function

        elif choice == 2:
            print "Currently ${} in Savings account.".format(savings)
            amount = int(prompt("Enter amount to transfer to Checking account: $"))
            if amount > savings:
                print "You do not have that much money."
                print formatter()
                transfer_funds(checking, savings)
            else:
                savings -= amount
                checking += amount
                print "${} withdrawn from Savings and added to Checking.".format(amount)
                print "${} left in Savings account.".format(savings)
                print "${} now in Checking account.".format(checking)
                choice = prompt("Transfer more funds? ").lower()
                print formatter()
                if 'no' in choice:
                    die("Goodbye.")
                    print formatter()
                else:
                    print formatter()
                    transfer_funds(checking, savings)

        elif choice == 3:
            welcome_screen()
        else:
            die("Invalid option.")
    else:
        broke("You do not have enough money.", total)


def withdraw_funds(checking, savings):

    """Function to withdraw funds from the accounts."""

    money_in_checking = check_if_true(checking)
    money_in_savings = check_if_true(savings)

    print """
    [ 1 ] Withdraw from Checking account
    [ 2 ] Withdraw from Savings account
    [ 3 ] Return to Main Menu
    """

    choice = int(prompt("Which account would you like to withdraw from? "))
    print formatter()

    if choice == 1:

        if money_in_checking == True:
            print "${} currently available in Checking account.".format(checking)

            while checking > 0:  # While the accounts balance isn't 0.
                amount = int(prompt("Enter amount to withdraw from Checking account: $"))
                if amount <= checking:
                    checking -= amount
                    print "${} withdrawn from Checking. ${} left.".format(amount, checking)
                    again = prompt("Withdraw more funds? ").lower()
                    print formatter()
                    if 'no' in again:
                        die("Goodbye")
                    else:
                        withdraw_funds(checking, savings)
                else:
                    print "You do not have that much money."
                    print formatter()
                    withdraw_funds(checking, savings)
            else:
                print "Unable to withdraw anymore ${} currently available in account.".format(checking)
        else:
            broke("Unable to withdraw anymore money", checking)
            welcome_screen()  # recursively loop back to the welcome screen

    elif choice == 2:
        if money_in_savings == True:

            while savings > 0:
                print "${} currently available in Savings account.".format(savings)
                amount = int(prompt("Enter amount to withdraw from Savings account: $"))
                if amount <= savings:
                    savings -= amount
                    print "${} withdrawn from Savings. ${} left.".format(amount, savings)
                    again = prompt("Withdraw more funds? ").lower()
                    print formatter()
                    if 'no' in again:
                        die("Goodbye")
                    else:
                        amount = int(prompt("Enter amount to withdraw from Savings account: $"))
                else:
                    print "You do not have that much money."
                    print formatter()
                    withdraw_funds(checking, savings)
            else:
                print "Unable to withdraw anymore ${} currently available in account.".format(savings)
        else:
            broke("Unable to withdraw anymore money", savings)
            welcome_screen()

    elif choice == 3:
        welcome_screen()
    else:
        die("Invalid option.")


def deposit_funds(checking, savings):

    """Function to deposit funds into the accounts."""

    print """
    [ 1 ] Deposit into Checking account
    [ 2 ] Deposit into savings account
    [ 3 ] Return to Main Menu
    """

    choice = int(prompt("Which account: "))
    print formatter()

    if choice == 1:
        amount = int(prompt("Enter amount to deposit into Checking: "))
        checking += amount
        print "${} now available in Checking account.".format(checking)
        more = prompt("Deposit more? ")
        if 'no' in more:  # If you say no it will exit.
            die("Goodbye")
        else:
            print formatter()
            deposit_funds(checking, savings)
    elif choice == 2:
        amount = int(prompt("Enter amount to deposit into Savings: "))
        savings += amount
        print "${} now available in Savings account.".format(savings)
        more = prompt("Deposit more? ")
        if 'no' in more:
            die("Goodbye")
        else:
            print formatter()
            deposit_funds(checking, savings)
    elif choice == 3:
        welcome_screen()
    else:
        die("Invalid choice")


def welcome_screen():

    """Main function of the program"""

    print formatter()
    print """
    Welcome to the Bank!
    Options include:
    [ 1 ] View Checking account
    [ 2 ] View Savings account
    [ 3 ] Transfer funds
    [ 4 ] Withdraw funds
    [ 5 ] Deposit funds
    """

    choice = int(prompt("What would you like to do: "))
    print formatter()
    if choice == 1:
        check_account(CHECKING_MONEY)
    elif choice == 2:
        check_account(SAVINGS_MONEY)
    elif choice == 3:
        transfer_funds(CHECKING_MONEY, SAVINGS_MONEY)
    elif choice == 4:
        withdraw_funds(CHECKING_MONEY, SAVINGS_MONEY)
    elif choice == 5:
        deposit_funds(CHECKING_MONEY, SAVINGS_MONEY)
    else:
        die("Invalid option.")


if __name__ == '__main__':
    welcome_screen()