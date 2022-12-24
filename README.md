## TalTech VK. Chemical Warehouse WebApp.

#### FastAPI is used on the backend and React-Admin for frontend. For working with database(PostgreSQL) - SQLAlchemy. Tested on python 3.10. 

In database.py check up your credentials for database. The database is located on the college server.

```python
# user 
POSTGRES_USER="user"
# user password
POSTGRES_PASSWORD=password
# host
POSTGRES_SERVER="host"
POSTGRES_PORT=5432
POSTGRES_DB="DB_Chemical_Warehouse"
```

For Backend you need install: <br />
1. FastAPI framework.
```python
pip install "fastapi[all]"
 ```
2. SQLAlchemy. Database Abstraction Library.
```
pip install SQLAlchemy
 ```
3. Uvicorn to work as the server.
```
pip install "uvicorn[standard]"
 ```
4. Psycopg-binary. PostgreSQL database adapter for Python -- C optimisation distribution.
```
pip install psycopg-binary
 ```
For Frontend you only need these commands: <br />
1. Install all dependencies
```
npm install
 ```
2. Start application
```
npm start
 ```
