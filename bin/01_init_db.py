__author__ = 'raksingh'
import sqlite3
DATABASE = '/tmp/portal.db'
try:
    conn = sqlite3.connect(DATABASE)
    curr =conn.cursor()
    curr.execute('drop table if exists entries;')
    curr.execute(
        '''
    create table entries (
      id integer primary key autoincrement,
      date text not null,
      url text not null,
      type text,
      title text,
      description text,
      rank  integer
    );
    '''
    )
except Exception as e:
    print(e)
finally:
    conn.close()

