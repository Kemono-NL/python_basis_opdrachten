import pymysql

con = pymysql.connect(host='localhost',
                      user='root',
                      password='',
                      database='superduper',
                      port=3306,
                      charset='utf8mb4',
                      cursorclass=pymysql.cursors.DictCursor)

id = input("Welk rijnummer wil je zien? ")
sql = "SELECT * FROM persons WHERE id = " + id

#maak een cursor object van de database
with con.cursor() as cur:
    #Voer de qury uit
    cur.execute(sql)
    #loop over elke row
    for row in cur.fetchall():
        #loop door de items in de row
        for key, value in row.items():
            #Print de waardes op het scherm
            print(f"{key}: {value}")