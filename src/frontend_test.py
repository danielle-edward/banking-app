import tempfile
from importlib import reload
import os
import io
import sys
import frontend as app

path = os.path.dirname(os.path.abspath(__file__))


def test_r1t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'logout'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'No existing session found',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'deposit'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'createacct'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'deleteacct'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'withdraw'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'createacct'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r1t7(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'transfer'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Must login first',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r2t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '12345678'
        ],
        expected_tail_of_terminal_output=[
            'Invalid accounts list file: account number too long',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r2t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '123456'
        ],
        expected_tail_of_terminal_output=[
            'Invalid accounts list file: account number too short',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r2t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '123456a'
        ],
        expected_tail_of_terminal_output=[
            'Invalid accounts list file: account number containing non-numerical values',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r2t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '0123456'
        ],
        expected_tail_of_terminal_output=[
            'Invalid accounts list file: account number starting with zero',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r2t5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '1234567',
            '1000000'
        ],
        expected_tail_of_terminal_output=[
            'Invalid accounts list file: incorrect end of file account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            '123'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Invalid session type, please try again',
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            ' '
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Invalid session type, please try again',
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r3t6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'wrong word'
        ],
        intput_valid_accounts=[
        ],
        expected_tail_of_terminal_output=[
            'Invalid session type, please try again',
            'Enter session type (machine/agent):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r4t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'createacct'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'This operation is not available in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r4t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deleteacct'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'This operation is not available in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r5t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'logout'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Give a command:'
        ],
        expected_output_transactions=[
            'EOS 0000000 000 0000000 ***'
        ]
    )

def test_r6t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'createacct'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'This operation is not available in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r7t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '0111111'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Account numbers cannot start with a zero',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r7t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '123456'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Account numbers must be exactly 7 digits',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r7t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '12345678'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Account numbers must be exactly 7 digits',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r8t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'aa'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Enter new account name:',
            'Account names must be between 3-30 characters in length',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r8t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'abcdefghijklmnopqrstuvwxyzabcde'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Enter new account name:',
            'Account names must be between 3-30 characters in length',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r8t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'Alan+'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Enter new account name:',
            'Account name can only contain alphanumeric characters ans spaces',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )


def test_r8t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            ' Alan'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Enter new account name:',
            'Account name cannot start or end with space character',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r8t5(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'Alan '
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Enter new account name:',
            'Account name cannot start or end with space character',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r8t6(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            'Account number is already in use',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r9t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'test',
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            "Enter new account name:",
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )


def test_r10t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'createacct',
            '1234567',
            'test',
            'logout'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter new account number:",
            "Enter new account name:",
            'Give a command:',
            'Give a command:'
        ],
        expected_output_transactions=[
            'NEW 1234567 000 0000000 test',
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r11t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deleteacct'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'This operation is not available in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r12t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1111111'
        ],
        intput_valid_accounts=[
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter id number of account to be deleted:",
            'Must enter a valid account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r12t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1234567',
            'Test'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter id number of account to be deleted:",
            'Enter account name:',
            'Account deleted',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )


def test_r14t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deleteacct',
            '1234567',
            'Test',
            'logout'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            "Enter id number of account to be deleted:",
            'Enter account name:',
            'Account deleted',
            'Give a command:',
            'Give a command:'
        ],
        expected_output_transactions=[
            'DEL 1234567 000 0000000 Test',
            'EOS 0000000 000 0000000 ***'
        ]
    )


def test_r15t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '1234567',
            '100000010'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Withdrawals above $1000 rejected in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r15t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'withdraw',
            '1234567',
            '100000000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Transactions above $999 999.99 rejected in Agent mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r15t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '1234567',
            '100000',
            'withdraw',
            '1234567',
            '100000',
            'withdraw',
            '1234567',
            '100000',
            'withdraw',
            '1234567',
            '100000',
            'withdraw',
            '1234567',
            '50000',
            'withdraw',
            '1234567',
            '100000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            '100000 surpasses $5000.00 daily limit, you have 50000 left',
            'Give a command:',
        ],
        expected_output_transactions=[
        ]
    )

def test_r16t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '1234567',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )
def test_r17t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '12345678',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r17t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '7654321',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r17t3(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '1234567',
            'abc'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid amount',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r17t4(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'withdraw',
            '1234567',
            '-10'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid amount',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r21t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '7654321',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r22t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1234567',
            'abc'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid amount',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r22t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1234567',
            '-10'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid amount',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )


def test_r23t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1234567',
            '100000010'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Deposits above $2000 rejected in ATM mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r24t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'agent',
            'deposit',
            '1234567',
            '100000000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Transactions above $999 999.99 rejected in Agent mode',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r24t2(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '12345678',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Invalid account number',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )

def test_r25t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1234567',
            '100000',
            'deposit',
            '1234567',
            '100000',
            'deposit',
            '1234567',
            '100000',
            'deposit',
            '1234567',
            '100000',
            'deposit',
            '1234567',
            '50000',
            'deposit',
            '1234567',
            '100000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            '100000 surpasses $5000.00 daily limit, you have 50000 left',
            'Give a command:',
        ],
        expected_output_transactions=[
        ]
    )

def test_r26t1(capsys):
    helper(
        capsys=capsys,
        terminal_input=[
            'login',
            'machine',
            'deposit',
            '1234567',
            '10000'
        ],
        intput_valid_accounts=[
            '1234567',
            '0000000'
        ],
        expected_tail_of_terminal_output=[
            'Enter session type (machine/agent):',
            'Give a command:',
            'Input an account number:',
            'Input amount (in cents):',
            'Give a command:'
        ],
        expected_output_transactions=[
        ]
    )


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        intput_valid_accounts,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # create a temporary file in the system to store output transactions
    temp_fd, temp_file = tempfile.mkstemp()
    transaction_summary_file = temp_file

    # create a temporary file in the system to store the valid accounts:
    temp_fd2, temp_file2 = tempfile.mkstemp()
    valid_account_list_file = temp_file2
    with open(valid_account_list_file, 'w') as wf:
        wf.write('\n'.join(intput_valid_accounts))

    # prepare program parameters
    sys.argv = [
        'frontend.py',
        valid_account_list_file,
        transaction_summary_file]

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('std.in:', terminal_input)
    print('valid accounts:', intput_valid_accounts)
    print('terminal output:', out_lines)
    print('terminal output (expected tail):', expected_tail_of_terminal_output)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output)+1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    with open(transaction_summary_file, 'r') as of:
        content = of.read().splitlines()

        # print out the testing information for debugging
        # the following print content will only display if a
        # test case failed:
        print('output transactions:', content)
        print('output transactions (expected):', expected_output_transactions)

        for ind in range(len(content)):
            assert content[ind] == expected_output_transactions[ind]

    # clean up
    os.close(temp_fd)
    os.remove(temp_file)
