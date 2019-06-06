# -*- coding: utf-8 -*-

import requests
import sqlite3
import os

api_url_base = 'https://api.github.com'
headers = {'Content-Type': 'application/json',
           'User-Agent': 'Python Student',
           'Accept': 'application/vnd.github.v3+json'}
DATABASE = os.path.join(os.pardir, "db.sqlite3")


def get_issues_to_db(owner, repo):

    api_url = '{}/repos/{}/{}/issues'.format(api_url_base, owner, repo)
    with requests.session() as sess:
        response = sess.get(api_url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            while 'next' in response.links:
                response = requests.get(response.links.get(
                                        'next').get('url'), headers=headers)
                data.extend(response.json())
            for job in data:
                insert_to_job_table(
                    job.get('number'),
                    job.get('created_at'),
                    job.get('title'),
                    job.get('body'))
        else:
            print('[!] HTTP {0} calling [{1}]'.format(
                response.status_code, api_url))
            return None


def create_db():
    with sqlite3.connect(DATABASE) as db:
        cur = db.cursor()
        cur.execute('''CREATE TABLE if not exists Job
              (sequence INTEGER PRIMARY KEY, created_at text, title text,
               description text)''')


def insert_to_job_table(job_order, created_at, title, body):
    with sqlite3.connect(DATABASE) as db:
        cur = db.cursor()
        cur.execute('''
                    INSERT OR IGNORE INTO Job VALUES(?,?,?,?)''',
                    (job_order, created_at, title, body))


def main():
    print("Running crawler...")
    create_db()
    get_issues_to_db('awesome-jobs', 'vietnam')


if __name__ == '__main__':
    main()
