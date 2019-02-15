#  This problem uses a class to create a bank account and simulates some
#  typical banking practices.  Read the instructions carefully and you will be
# successful
def main():
    # when you have initialized your object, use the calls below to test
    run_test_init()
    run_test_withdrawal()
    return


class Bank(object):
    """
    A Bank has:
        -- NAME, a string that contains the last name of the bank account holder,
        -- BALANCE, a float that tells the money in the account
        -- ACCOUNT NUMBER, a string that is unique to each account holder.
    """

    def __init__(self, name, initial_deposit, account_number):
        """
        What comes in:
          -- self
          -- A string that is the name of the account holder
          -- A float that is the initial deposit in the account
          -- A string that is the unique account identifier
        What is returned:
          -- A float that is the current balance in the account
        Side effects:
          -- Stores the name, initial_deposit, account_number
             in the instance variables
          -- Also initializes other instance variables as needed
              by other methods.
        Examples:
          b1 = Bank('Brackin',10000.00, A1)
          #   b1.name is 'Brackin'
          #   b1.balance is 10000.00
          #   b1. account_number is 'A1'

          b2 = Bank('Lovelace',10.15, 'A2')
          #   b2.name is 'Lovelace'
          #   b2.balance is 10.15
          #   b2.account_number is 'A2'

        Type hints:
          :type name: str
          :type balance: float
          :type account_number: str
        """
        self.name = name
        self.initial_deposit = initial_deposit
        self.account_number = account_number
        self.balance = initial_deposit
    # ---------------------------------------------------------------------
    # DONE: 1. Implement and test instances of this class.
    #     See the testing code (scroll down near bottom) for more examples.
    # ---------------------------------------------------------------------


    def withdraw(self, amount):
        """
        What comes in:
        -- self
        -- A float that is the amount to be withdrawn
        What is returned:
        -- An error message if there is not enough money in the account
        -- A float that is the current balance in the account if
           there are sufficient funds
        Side effects:
        -- Updates the balance
        Examples:
          b1.withdraw(8000)
          #   b1.name is 'Brackin'
          #   b1.balance is 2000.00
          #   b1. account_number is 'A1'

          b2.withdraw(50.25)
          #   b2.name is 'Lovelace'
          #   b2.balance is 10.15 (no money is withdrawn)
          #   b2.account_number is 'A2'
          #   an error message is printed because there are insufficient funds
        """
    # ---------------------------------------------------------------------
    # DONE: 4. Implement and test the withdraw method
    #     Implement your own test code, before you write your method
    #     Insert your test code for withdraw, where indicated
    #     Scroll down near the bottom of this screen
    # ---------------------------------------------------------------------
    #   Put your code for withdraw below
    #
    # ---------------------------------------------------------------------
        if self.balance <= amount:
            print('There are not sufficient fund for this withdrawal')
            return self.balance
        else:
            self.balance = self.balance - amount
            return self.balance



def run_test_init():
    """ Tests the   __init__   method of the Bank class. """
    print()
    print('-----------------------------------------------------------')
    print('Testing the   __init__   method of the Bank class.')
    print('-----------------------------------------------------------')

    # Test 1:  Contents fit in the Box easily.
    b1= Bank('Brackin', 10000, 'A1')
    expected_name = 'Brackin'
    expected_balance = 10000
    expected_account_number = 'A1'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b1.name, b1.balance, b1.account_number)
    if (expected_name == b1.name) and (expected_balance == b1.balance) and (expected_account_number == b1.account_number):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()
    # ---------------------------------------------------------------------
    # DONE: 2. Add two more test cases for your Bank class below.
    # ---------------------------------------------------------------------

    # Test 2:
    b2 = Bank('Stevenson', 4728364628, '57383')
    expected_name = 'Stevenson'
    expected_balance = 4728364628
    expected_account_number = '57383'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b2.name, b2.balance, b2.account_number)
    if (expected_name == b2.name) and (expected_balance == b2.balance) and (
            expected_account_number == b2.account_number):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()

    # Test 3:
    b3 = Bank('Birck', 1000000000001, '23456')
    expected_name = 'Birck'
    expected_balance = 1000000000001
    expected_account_number = '23456'
    print("Expected:", expected_name, expected_balance, expected_account_number)
    print("Actual:  ", b3.name, b3.balance, b3.account_number)
    if (expected_name == b3.name) and (expected_balance == b3.balance) and (
            expected_account_number == b3.account_number):
        print("Test passed SUCCESSFULLY!")
    else:
        print_failure_message()
    print()

# ---------------------------------------------------------------------
# DONE: 3. Implement your test for the withdraw method below
# ---------------------------------------------------------------------
def run_test_withdrawal():
    # Implement at least two tests.  Use copy and paste to speed your coding.
    # Test 1:
    b1 = Bank('Brackin', 10000, 'A1')
    b1. withdraw(32)
    expected = 10000 - 32
    actual = b1.balance
    print('Expected: ', expected)
    print('Actual: ', actual)
    if expected == actual:
        print('Test passed SUCCESSFULLY')
    else:
        print_failure_message()
    print()

    # Test 2:
    b2 = Bank('Stevenson', 23845739849, '2344354')
    b2.withdraw(5647893)
    expected = 23845739849 - 5647893
    actual = b2.balance
    print('Expected: ', expected)
    print('Actual: ', actual)
    if expected == actual:
        print('Test passed SUCCESSFULLY')
    else:
        print_failure_message()
    print()

    # Test 3: because I didn't do a test where there sin't enough money
    b3 = Bank('Potter', 13, '23423')
    b3.withdraw(34566)
    expected = 13
    actual = b3.balance
    print('Expected: ', expected)
    print('Actual: ', actual)
    if expected == actual:
        print('Test passed SUCCESSFULLY')
    else:
        print_failure_message()
    print()


def print_failure_message():
    print('  *** FAILED the above test. ***')


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ------------------------------------------------------------------------
main()
