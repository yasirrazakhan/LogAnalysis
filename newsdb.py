#!/usr/bin/python3

import bleach
import psycopg2
from pprint import pprint
import sys

DBNAME = "news"


def q1():
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.error as e:
        raise e
    c = db.cursor()
    c.execute("select * from PopularArticles")
    posts = c.fetchall()
    print('Q1: What are the most popular articles of all time?')
    print
    for post in posts:
        print(' --- '.join(map(str, post)) + ' ' 'views')
    db.close()
    print


def q2():
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.error as e:
        raise e
    c = db.cursor()
    c.execute("select * from PopularAuthors")
    authors = c.fetchall()
    print('Q2: What are the most popular authors of all time?')
    print
    for author in authors:
        print(' --- '.join(map(str, author)) + ' ' 'views')
    db.close()
    print


def q3():
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.error as e:
        raise e
    c = db.cursor()
    query = "select day, percentage|| '% errors'as percentage from q3query;"
    c.execute(query)
    errors = c.fetchall()
    print('Q3: On which days did more than 1"%" of requests lead to errors?')
    print
    for error in errors:
        fdate = error[0].strftime('%B %d, %Y')
        print(fdate+" " + "---" + error[1])
    db.close()
    print


if __name__ == '__main__':
        q1()
        q2()
        q3()
