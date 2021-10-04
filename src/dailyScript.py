import frontend as fe
import backend as be

import sys

#Does the transactions and saves the summary in separate files
#filename - unique name for each summary file
#actions - list of actions to perform, start with login and ending with logout
#passes transaction summary file back to main
def transactions(filename, actions):
    if len(actions) == 0:
        #runs program allowing for manual input
        fe.main("valid_accounts_list.txt", filename)
    else:
        #creating a file the system can be used as input
        input_file = open("actions.txt", "w")
        for act in actions:
            input_file.write(act+'\n')
        input_file.close()
        fe.automatedInput("actions.txt", filename)



#creates the new Transaction summary file from all the merged files
#passes this file to main to invoke the backend
def mergedFile(files):
    merged_file = open("merged_transaction_summary_file.txt", "w")
    file_number = len(files)
    count = 0

    for f in files:
        count += 1
        last = True if count == file_number else False
        merged_file = fileHelper(f, merged_file, last)

    merged_file.close()

#writes every line of the transaction file into the merged transaciton file
def fileHelper(f, merged, last):
    if f != None:
        for line in f:
            line = line.strip()
            if line != "EOS 0000000 000 0000000 ***":
                merged.write(line+'\n')

        if last == True:
            merged.write("EOS 0000000 000 0000000 ***")

        return merged

#this method is to be used when using the dailyScript by itself to simulate
#one day of operation.
def oneDay():
    trans1 = ["login", "agent", "createAccount", "1234567", "Emma", "logout"]
    #trans2 will output "Account doesn't exist"
    trans2 = ["login", "machine", "withdraw", "1234567", "logout"]
    trans3 = ["login", "agent", "createAccount", "7654321", "Kathryn", "logout", "0"]

    fileName1 = "transaction_file_1.txt"
    fileName2 = "transaction_file_2.txt"
    fileName3 = "transaction_file_3.txt"

    transactions(fileName1, trans1)
    transactions(fileName2, trans2)
    transactions(fileName3, trans3)

    f1 = open(fileName1, "r")
    f2 = open(fileName2, "r")
    f3 = open(fileName3, "r")

    files = [f1, f2, f3]

    mergedFile(files)

    for f in files:
        f.close()

    be.main("master_accounts_file.txt", "merged_transaction_summary_file.txt")

#calls the transactions and passes a different file name every time
#calls backend for merged file
def main(trans1, trans2, trans3):
    fileName1 = "transaction_file_1.txt"
    fileName2 = "transaction_file_2.txt"
    fileName3 = "transaction_file_3.txt"

    transactions(fileName1, trans1)
    transactions(fileName2, trans2)
    transactions(fileName3, trans3)

    f1 = open(fileName1, "r")
    f2 = open(fileName2, "r")
    f3 = open(fileName3, "r")

    files = [f1, f2, f3]

    mergedFile(files)

    for f in files:
        f.close()

    be.main("master_accounts_file.txt", "merged_transaction_summary_file.txt")
