# 362f_Project
Create a shopping server for multi-clients access
## Set Up
### Create your Own Database Server
1.  Installing: https://dev.mysql.com/downloads/installer/
2. Setup: Follow the instruction in the installer (Others Tutorial: https://jerrynest.io/windows-mysql-installer/)

Please make sure your database server is **running** in your localhost
![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/running_server.jpg)
If not running:
1.  Search `Services.msc` in **Start**
2.  Find your MySQL server name
3. Right click , Click start
![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/start_running.jpg)

### Import Data
Import the data in your database server (My SQL Work brench)
1.  **Server** -> **Data Impot**
2. Choose**Import from Self-Contained File** and load the database file
	*(database file: /database/db.sql)*
3.  Create a new Default target Schema: **362f**
4. Choose **Dump Structure and Data**
5. **Import Progress** -> **Start Impot**

![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/import_data.jpg)

There will be 3 tables in the schema after the import and refresh your database server
![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/tables.jpg)

## Configure
1. Go to `database.py` and `owner.py` :
```python
	db = mysql.connector.connect(user='root',password='root',
                              host='127.0.0.1',database='362f')
```
2. Change your **username, password, host, schema**
>**Database**-> **Mange Connect** (You can test connect to ensure your username, password is correct)

![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/Connection.jpg)

## How to Run
1.  Install python library
```bash
pip install mysql-connector
pip install base64
pip install bottle
pip install selenium
pip install dataclasses
pip install prettytable
pip install re
pip install urllib.parse
```
2. Change to your folder root in cmd 
Example:
```bash
cd C:\Downloads\362f_Project
```
3. Run `app.py`
```bash
python3 app.py
```
You can see below outcome:
> Bottle v0.12.19 server starting up (using PasteServer())...
Listening on http://127.0.0.1:8080/
Hit Ctrl-C to quit.
serving on http://127.0.0.1:8080

4. Run http://127.0.0.1:8080 in your browser
![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/login.jpg)
> Login as customer: username= guest/user  
Login as shop owner: username= owner 
Password is no required

5. After login, you can see the main page. Please enjoy different functions by your own
![](https://github.com/Lukwok/362f_Project/blob/main/ReadMe_image/home.jpg)
6. Run `automic_test.py`
```bash
python3 automic_test.py
```
7. Run `automic_test_customer.py`
```bash
python3 automic_test_customer.py
```

