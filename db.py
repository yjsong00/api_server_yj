import mysql.connector
from mysql.connector import Error

def get_db():
    return mysql.connector.connect(
        host="mysql-service",  # Minikube에서 생성된 MySQL 서비스 이름
        user="root",
        password="password",
        database="testdb"
    )

