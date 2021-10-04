from datetime import datetime
import sys
import os
#import backend as be

#global variables
session = None
isLoggedIn = False
accounts = []
session_type = ''
valid_account_list_file = ''
transaction_summary_file = ''

class Session:
    #for each function append a string to the transactions list that looks like one line in the summary file
    #CCC AAAA MMMM BBBB NNNN
    transactions = []
    session_type = ""

    def __init__(self, session_type):
        self.session_type = session_type
        self.transactions = []


    #verifies the daily limits for transactions, WDR/XFR/DEP
    def check_daily(self, account_number, amount, transaction_type):

        daily_trans = 0
        for line in Session.transactions:
            data = line.split()
            if data[0] == "XFR" and data[3] == account_number:
                daily_trans += int(data[2])

            elif data[0] == transaction_type and data[1] == account_number:
                daily_trans += int(data[2])
        if transaction_type == "DEP" or transaction_type == "WDR":
            if daily_trans + amount > 500000:
                amount_left = 500000 - daily_trans
                return False, amount_left
            else:
                return True, 0
        elif transaction_type == "XFR":
            if daily_trans + amount > 1000000:
                amount_left = 1000000 - daily_trans
                return False, amount_left
            else:
                return True, 0


    def transfer(self):
        account_number_from = ""
        account_number_from = input("Input an account number which you are withdrawing from")
        if account_number_from not in accounts:
            print("Invalid account number: Transaction Cancelled")
            return
        account_number_to = ""
        account_number_to = input("Input an account number which you are depositing to")
        if account_number_to not in accounts:
            print("Invalid account number: Transaction Cancelled")
            return

        inputName = input("Input account name")
        if len(inputName) < 3 or len(inputName) > 30:
            print("Account names must be between 3-30 characters in length")
            return
        elif inputName[0] is " " or inputName[len(inputName)-1] is " ":
            print("Account name cannot start or end with space character")
            return
        elif not(all(x.isalpha() or x.isspace() for x in inputName)):
            print("Account name can only contain alphanumeric characters ans spaces")
            return

        verified_transfer_amount = False
        transfer_amount = 0
        while not verified_transfer_amount:
            transfer_amount = input("Input a transfer amount (in cents, as an integer)")
            if transfer_amount == "0":
                print("transaction Cancelled")
                return
            elif not str.isdigit(transfer_amount):
                print("Please enter a valid transfer amount (. - + and other characters are not allowed(0 will cancel transaction))")
            else:
                verified_transfer_amount = True

        if (int(transfer_amount) > 1000000 and session.session_type == "machine") or ((int(transfer_amount)) > 99999999 and session.session_type == "agent") or (session.session_type == ""):
            print("Amount is too high to transfer: Transaction Cancelled")
            return

        else:
            answer = input("Transferring "+str(transfer_amount)+" from account: "+str(account_number_from)+" to account: "+str(account_number_to)+"(enter 'cancel' to cancel)")
            if answer == "cancel":
                return
            else:
                limit, amount_left = session.check_daily(account_number_from,int(transfer_amount),"XFR")
                if not limit:
                    print(answer, "surpasses $10000.00 daily limit, you can deposit up to", amount_left, ", try again")
                    return
                else:
                    print("Transaction Success!")
                    session.transactions.append("XFR "+" "+str(account_number_from)+" "+str(transfer_amount)+" "+str(account_number_to)+" "+str(inputName))
                    return

    def createAccount(self):
        global session, accounts, isLoggedIn, valid_account_list_file, session_type
        if session_type == "machine":
            print("This operation is not available in ATM mode")
            return
        elif session_type == "agent":
            inputNumber = input("Enter new account number:\n")
            if len(inputNumber) != 7:
                print("Account numbers must be exactly 7 digits")
                return
            elif int(inputNumber[0]) == 0:
                print("Account numbers cannot start with a zero")
                return
            elif inputNumber in accounts:
                print("Account number is already in use")
                return
            inputName = input("Enter new account name:\n")
            if len(inputName) < 3 or len(inputName) > 30:
                print("Account names must be between 3-30 characters in length")
                return
            elif inputName[0] is " " or inputName[len(inputName)-1] is " ":

                print("Account name cannot start or end with space character")
                return
            elif not (all(x.isalpha() or x.isspace() for x in inputName)):
                print("Account name can only contain alphanumeric characters ans spaces")
                return
            else:
                accounts.append(inputNumber)
                session.transactions.append("NEW "+inputNumber+" 000 0000000 "+inputName)
                return

    def deleteAccount(self):

        global session, accounts, isLoggedIn, valid_account_list_file, session_type

        if session_type == "machine":
            print("This operation is not available in ATM mode")
            return
        else:
            inputNumber = input("Enter id number of account to be deleted:\n")
            if inputNumber not in accounts:
                print("Must enter a valid account number")
                return
            else:
                inputName = input("Enter account name:\n")
                if len(inputName) < 3 or len(inputName) > 30:
                    print("Account names must be between 3-30 characters in length")
                    return
                elif inputName[0] is " " or inputName[len(inputName)-1] is " ":
                    print("Account name cannot start or end with space character")
                    return
                elif not(all(x.isalpha() or x.isspace() for x in inputName)):
                    print("Account name can only contain alphanumeric characters ans spaces")
                    return
                else:
                    accounts.remove(inputNumber)
                    session.transactions.append("DEL "+inputNumber+" 000 0000000 "+inputName)
                    print("Account deleted")
                    return

    def deposit_withdraw(self, trans_type):
        global session, accounts, isLoggedIn, valid_account_list_file, session_type

        account_number = input("Input an account number:\n")

        if len(account_number) != 7:
            print("Invalid account number")
            return
        if account_number not in accounts:
            print("Account doesn't exist")
            return

        inputName = input("Input account name:\n")
        if len(inputName) < 3 or len(inputName) > 30:
            print("Account names must be between 3-30 characters in length")
            return
        elif inputName[0] is " " or inputName[len(inputName)-1] is " ":
            print("Account name cannot start or end with space character")
            return
        elif not(all(x.isalpha() or x.isspace() for x in inputName)):
            print("Account name can only contain alphanumeric characters ans spaces")
            return

        amountIn = input("Input amount (in cents):\n")

        try:
            amount = int(amountIn)
        except ValueError:
            print("Invalid amount")
            return

        if amount < 0:
            print("Invalid amount")
            return

        if trans_type == "DEP":
            if session_type == "machine" and amount > 200000: # input is in cents, constraint it 2000 dollars
                print("Deposits above $2000 rejected in ATM mode")
                return
        elif trans_type == "WDR":
            if session_type == "machine" and amount > 100000:
                print("Withdrawals above $1000 rejected in ATM mode")
                return
        if session_type == "agent" and amount > 99999999:
            print("Transactions above $999 999.99 rejected in Agent mode")
            return

        limit, amount_left = session.check_daily(account_number, amount, trans_type)
        if not limit:
            print(amount, "surpasses $5000.00 daily limit, you have",
                  amount_left, "left")
            return

        for acc in accounts:
            if(int(acc) == int(account_number)):
                session.transactions.append(trans_type+" "+str(account_number)+" "+
                                           str(amount)+" XXXX "+str(inputName))
        return


def login():
    global session, accounts, isLoggedIn, valid_account_list_file, session_type
    valid_type = False
    while not valid_type:
        try:
            session_type = input("Enter session type (machine/agent):\n")
        except EOFError:
            return
        if session_type != "machine" and session_type != "agent":
            print("Invalid session type, please try again")
        else:
            valid_type = True

    try:
        f = open(valid_account_list_file, "r")
    except FileNotFoundError:
        print("Can't find valid accounts list file")
        return

    acc = f.read().splitlines()
    for a in acc:
        if len(a) > 7:
            print('Invalid accounts list file: account number too long')
            return
        elif len(a) < 7:
            print('Invalid accounts list file: account number too short')
            return
        elif not a.isdigit():
            print('Invalid accounts list file: account number containing non-numerical values')
            return
        elif a[0] == '0' and a != '0000000':
            print('Invalid accounts list file: account number starting with zero')
            return
    if acc[-1] != '0000000':
        print('Invalid accounts list file: incorrect end of file account number')
        return
    acc.pop(-1)

    session = Session(session_type)
    accounts = acc
    isLoggedIn = True


def logout():
    global session, isLoggedIn, transaction_summary_file
    #timestamp = datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + ".txt"
    f = open(transaction_summary_file, 'w')

    for t in session.transactions:
        f.write(t+'\n')
    f.write('EOS 0000000 000 0000000 ***')
    f.close()
    print("Logged out")
    session = None
    isLoggedIn = False

#validate commands based on your individual function constraints
def send_command(command):
    if command == "login":
        login() if not isLoggedIn else print("Already logged in")
    elif command == "logout":
        logout() if isLoggedIn else print("No existing session found")
    elif command == "deposit":
        session.deposit_withdraw("DEP") if isLoggedIn else print("Must login first")
    elif command == "transfer":
        session.transfer() if isLoggedIn else print("Must login first")
    elif command == "withdraw":
        session.deposit_withdraw("WDR") if isLoggedIn else print("Must login first")
    elif command == "createAccount":
        session.createAccount() if isLoggedIn else print("Must login first")
    elif command == "deleteAccount":
        session.deleteAccount() if isLoggedIn else print("Must login first")


def main(arg1, arg2):
    global valid_account_list_file, transaction_summary_file
    print('Welcome the Queens ATM machine')

    valid_account_list_file = arg1
    transaction_summary_file = arg2

    while True:
        try:
            print("Enter 'c' to read list of commands")
            command = input("Give a command:\n")
        except EOFError:
            return
        if command == "0":
            break
        if command == "c":
            print("Available commands are:\n")
            print("login - start your session. This is required upon start to continue.")
            print("logout - end your session. Any action you perform while logged \
in while be recorded upon logging out.")
            print("createAccount - enter account number and name while in agent mode to \
create an account. Any actions on this account can only be done the next transaction day.")
            print("deleteAccount - delete existing account in agent mode. This can only be\
done the next transaction day after the account is created")
            print("withdraw - take money out of an existing account")
            print("deposit - put money into an existing account")
            print("transfer - move money from one existing account to another")
        else:
            send_command(command)

def automatedInput(actionsFile, transFile):
    f1 = sys.stdin
    f = open(actionsFile,'r')
    sys.stdin = f
    main("valid_accounts_list.txt", transFile)
    f.close()
    sys.stdin = f1

