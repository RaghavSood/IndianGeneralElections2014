import sqlite3 as lite
import sys
import os

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0


try:
    dbdirectory = "/Users/raghavsood/Downloads/Elections/Delhi/Analysed/Database/"

    con = lite.connect(dbdirectory + "delhielection.db")
    con.execute("DROP TABLE IF EXISTS delhifailed")
    con.execute("CREATE TABLE delhifailed(serialno INTEGER PRIMARY KEY NOT NULL, originalid INTEGER, id TEXT, ac TEXT, part TEXT)")

    cur = con.cursor()  
    
    cur.execute("SELECT * FROM delhivoters WHERE LENGTH(id) = 10")

    while True:
      
        row = cur.fetchone()
        
        if row == None:
            break
            
        number = row[1][3:]
        if not is_luhn_valid(number):
            print row[0], row[1], "is not a valid LUHN number, adding to list"
            con.execute("INSERT INTO delhifailed(originalid, id, ac, part) VALUES (?, ?, ?, ?)", (row[0], row[1], row[2], row[3]))

    con.commit()    
finally:
    con.close()
    pass
