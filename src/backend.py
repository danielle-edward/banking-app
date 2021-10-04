import frontend
import sys

#global variables
accounts = {} #key = account number, value = (balance, account name) <- all strings
transactions  = [] #each element is one row in the merged transaction summary file <- string
accounts_filename = '' #name of master accounts file
transactions_filename= '' #name of merged transactions summary file

def read_accounts():
    global accounts_filename, accounts
    try:
        f = open(accounts_filename, "r")
    except FileNotFoundError:
        print("Can't find master accounts list file")
        return

    acc = f.read().splitlines()
    f.close()
    for a in acc:
        line = a.split()
        number, balance, name = line[0], line[1], line[2]
        if number in accounts:
            print("duplicate account" + number + "in master list")
            return
        accounts[number] = (balance, name)

def read_transactions():
    global transactions_filename, transactions
  
    try:
        f = open(transactions_filename, "r")
    except FileNotFoundError:
        print("Can't find merged transactions summary file")
        return

    trans = f.read().splitlines()
    f.close()
    for t in trans:
        if 'EOS' in t:
            break
        transactions.append(t)

def process_transactions():
    global transactions, accounts_filename, accounts

    #for each of your transactions, directly edit the global 'accounts' variable
    #IMPORTANT: keep all the values in accounts to be strings (convert them back from ints if you need to deal with money)

    for t in transactions:
      
        line = t.split()

        command = line[0].strip()
        userAccNum = line[1].strip()
        amount = int(line[2])
        sentAccNum = line[3].strip()
        accountName = line[4].strip()

        if command == "DEP":
            deposit(userAccNum, amount)
        elif command == "WDR":
            withdraw(userAccNum, amount)
        elif command == "XFR":
            transfer(userAccNum,sentAccNum,amount)
        elif command == "NEW":
            create_account(userAccNum, accountName)
        elif command == "DEL":
            delete_account(userAccNum)
        else:
            print('Error: invalid transaction code')

    transactions = []
    f = open(accounts_filename, 'w')
    f2 = open('valid_accounts_list.txt', 'w')
    for key in sorted(accounts, reverse=True):
        acc_num = key
        balance = accounts[key][0]
        name = accounts[key][1]      
        f.write(str(acc_num) + ' ' + str(balance) + ' ' + str(name) + '\n')
        f2.write(str(acc_num) + '\n')

    f.close()
    f2.close()

def create_account(accountNumber, accountName):
    global accounts

    accounts[accountNumber] = ("0", accountName)
    return

def delete_account(accountNumber):
    global accounts

    del accounts[accountNumber]
    return


def transfer(fromAccount, toAccount, money):
    global accounts

    currMoney = int(accounts[fromAccount][0])
    if (money > currMoney):
        #reject transaction not enough money
        return
    else:
        accounts[fromAccount] = (str(currMoney - money), accounts[fromAccount][1])
        currMoney = int(accounts[toAccount][0])
        accounts[toAccount] = (str(currMoney + money), accounts[toAccount][1])
    return

def deposit(accountNum, amount):
    global accounts
    accounts[accountNum] = (str(int(accounts[accountNum][0]) + amount), accounts[accountNum][1])
    return

def withdraw(accountNum, amount):
    global accounts
    try:
        currAcc = accounts[accountNum]
    except:
        print("Account doesn't exist")
        return
        
    currBalance = int(accounts[accountNum][0])
    
    if currBalance - amount < 0:
        print("Account overdrawn, transaction not completed")
    else:
        accounts[accountNum] = (str(int(accounts[accountNum][0]) - amount), accounts[accountNum][1])
    return

def main(acctFile, transFile):
    global transactions, accounts_filename, accounts, transactions_filename
    
    
    accounts_filename = acctFile
    transactions_filename = transFile
    
    read_accounts()
    
    read_transactions()

    process_transactions()
  
