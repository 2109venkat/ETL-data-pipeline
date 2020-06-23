import psycopg2

try:
    conn = psycopg2.connect("dbname='retail_dw' user='retail_user' host='34.72.140.44' password='venkatramasai'")
except:
    print("I am unable to connect to the database")


cur = conn.cursor()
try:
    cur.execute("""SELECT * from t1""")
except:
    print("I can't SELECT from t1")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    print("   ", row)
