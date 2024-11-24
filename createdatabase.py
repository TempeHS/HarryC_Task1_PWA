import sqlite3 as sql

def create_database():
    con = sql.connect(".database/data_source.db")
    cur = con.cursor()

    # SQL query to create the diary_entries table
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS diary_entries (
        developer TEXT,
        project TEXT,
        start_time TEXT,
        end_time TEXT,
        diary_entry TEXT,
        time_worked TEXT,
        repo TEXT,
        developer_notes TEXT,
        code_additions TEXT
    )
    '''

    cur.execute(create_table_query)
    con.commit()
    con.close()


create_database()