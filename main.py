import os
import pathlib
import pickle

class acc:
    accountID = 0
    accountName = ''
    accountBal = 0
    accountType = ''
    
    def makeAccount(self):
        self.accountID = int(input('Enter account ID: '))
        self.AccountName = input('Enter account name: ')
        self.accountType = input('Checking or savings account? ')
        self.accountBal = int(input('How much would you like to deposit today? '))
        print("\nAccount Created!")
        
    def displayAccount(self):
        print('Account: ', self.accountID, ': ', self.accountName, ': ', self.accountType)
        print('Balance: ', self.accountBal)
        
    def modifyAccount(self):
        print('Changing account: ', self.accountID)
        self.AccountName = input('Change account name: ')
        self.accountType = input('Change to savings/checking: ')
        print('')
        
    