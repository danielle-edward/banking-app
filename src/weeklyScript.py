import dailyScript as daily

#create each of the days information that will be passed to the daily main script
def main():
    #day1
    d1_trans1 = ["login", "agent", "createAccount", "1234567", "Emma", "logout"]
    #trans2 will print "Account doesn't exist"
    d1_trans2 = ["login", "machine", "withdraw", "1234567", "logout"]
    d1_trans3 = ["login", "agent", "createAccount", "7654321", "Kathryn", "logout", "0"]
    daily.main(d1_trans1, d1_trans2, d1_trans3)
    print("---------------------End of Day 1--------------------------")

    #day2
    d2_trans1 = ["login", "machine", "deposit", "1234567", "Emma", "500", "logout"]
    #trans2 will print "Account overdrawn, transaction not completed"
    d2_trans2 = ["login", "machine", "withdraw", "1234567", "Emma", "200" "logout"]
    d2_trans3 = ["login", "agent", "deposit", "7654321", "Kathryn", "1000", "logout", "0"]
    daily.main(d2_trans1, d2_trans2, d2_trans3)
    print("---------------------End of Day 2--------------------------")
    
    #day3
    d3_trans1 = ["login", "agent", "withdraw", "1234567", "Emma", "10", "logout"]
    d3_trans2 = ["login", "machine", "transfer", "7654321", "1234567", "Kathryn", "150", "y", "logout"]
    d3_trans3 = ["login", "agent", "createAccount", "1105980", "Mary", "logout", "0"]
    daily.main(d3_trans1, d3_trans2, d3_trans3)
    print("---------------------End of Day 3--------------------------")

    #day4 - one transaction of manual input
    d4_trans1 = [] #manual input has to end with exit code 0
    d4_trans2 = ["login", "agent", "deleteAccount", "1105980", "Mary", "logout"]
    #trans3 will print "This operation is not available in ATM mode"
    d4_trans3 = ["login", "machine", "deleteAccount", "1234567", "logout", "0"]
    daily.main(d4_trans1, d4_trans2, d4_trans3)
    print("---------------------End of Day 4--------------------------")

    #day5
    #trans1 will print "Account doesn't exist"
    d5_trans1 = ["login", "agent", "deposit", "1105980", "logout"]
    #trans2 will print "Withdrawals above $1000 rejected in ATM mode"
    d5_trans2 = ["login", "machine", "withdraw", "1234567", "Emma", "15000000000", "logout"]
    d5_trans3 = ["login", "agent", "createAccount", "1000101", "QueensCS", "logout", "0"]
    daily.main(d5_trans1, d5_trans2, d5_trans3)
    print("---------------------End of Day 5--------------------------")
    
    '''
    After 5 days (If manual input doesn't change accounts or amounts)
    valid accounts list -
        1234567
        7654321
        1000101
        0000000
    master accounts file -
        7654321 850 Kathryn
        1234567 640 Emma
        1000101 0 QueensCS
        0000000 000 XXXX
        
    '''
