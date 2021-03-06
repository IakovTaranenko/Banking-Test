import os
import pathlib
import pickle

class Account:
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
        print('All Changes Saved!')
        
    def deposit(self, amount):
        self.accountBal += amount
        
    def withdraw(self, amount):
        self.accountBal -= amount
        
    def returnAccountID(self):
        return self.accountID
    
    def returnAccountName(self):
        return self.accountName
    
    def returnAccountBalance(self):
        return self.accountBal
    
    def returnAccountType(self):
        return self.accountType
    
"""
def verifyLogin(accountID, givenPass):
    #check if login request password and id match a stored account
    
def verifyLogout(accountID):
    #make sure that the account is removed from the currently opened accounts
    
def openAccount(accountID):
    #take account from storage and place it in opened account storage 
    
def storeAccount(accountID):
    #take account from opened account storage and place it in storage

"""