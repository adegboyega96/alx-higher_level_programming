#!/usr/bin/python3
"""All cities by state"""

import MySQLdb
import sys

db=MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
cur = db.cursor()
cur.execute("""
        SELECT
            cities.id, cities.name, states.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name = '{}';
        """.format(sys.argv[4]))

rows = cur.fetchall()
print(", ".join([row[1] for row in rows]))
cur.close()
db.close()
