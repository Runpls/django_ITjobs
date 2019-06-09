#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
import os

DATABASE = os.path.join(os.pardir, "db.sqlite3")
Json_file = os.path.join(os.pardir, "jobs.json")


def get_data_from_job_table():
    with sqlite3.connect(DATABASE) as db:
        cur = db.cursor()
        cur.execute('''
                    SELECT * FROM Job''')
        result = cur.fetchall()
        return result


def write_Json():
    data = get_data_from_job_table()
    column = ['sequence', 'created_at', 'title', 'description']
    items = [dict(zip(column, row)) for row in data]
    with open(Json_file, 'wt') as f:
        json.dump(items, f, indent=4)


def main():
    write_Json()


if __name__ == "__main__":
    main()
