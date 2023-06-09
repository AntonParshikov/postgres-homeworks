"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="324214Kross!"
)


def customers_add_data():
    try:
        with connection:
            with connection.cursor() as cursor:
                with open('../homework-1/north_data/customers_data.csv',
                          'r', encoding="utf-8") as f:
                    next(f)
                    cursor.copy_from(f, 'customers', sep=',', null='')
    finally:
        connection.close()


def employees_add_data():
    try:
        with connection:
            with connection.cursor() as cursor:
                with open('../homework-1/north_data/employees_data.csv',
                          'r', encoding="utf-8") as f:
                    next(f)
                    cursor.copy_from(f, 'employees', sep=',', null='')
    finally:
        connection.close()


def orders_add_data():
    try:
        with connection:
            with connection.cursor() as cursor:
                with open('../homework-1/north_data/orders_data.csv',
                          'r', encoding="utf-8") as f:
                    next(f)
                    cursor.copy_from(f, 'orders', sep=',', null='')
    finally:
        connection.close()


if __name__ == '__main__':
    employees_add_data()
