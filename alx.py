import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Robi@2024",
    database="alx_book_store"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Order_Details(orderdetail_id INT PRIMARY KEY, order_id INT, book_id INT, quantity DOUBLE, FOREIGN KEY (order_id) REFERENCES Orders(order_id), FOREIGN KEY (book_id) REFERENCES Books(book_id))");
