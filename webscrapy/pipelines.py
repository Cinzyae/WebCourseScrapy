# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import mysql.connector


class WebscrapyPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='hhh0425',
            database='tinfo'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS TINFO""")
        self.curr.execute("""CREATE TABLE TINFO(
        Name TEXT,
        Title TEXT,
        Phone TEXT,
        Fax TEXT,
        Email TEXT,
        ResearchDirection TEXT
        )""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.curr.execute("""insert into tinfo values (%s,%s,%s,%s,%s,%s)""",
                          (str(item['Name']), str(item['Title']), str(item['Phone']), str(item['Fax']),
                           str(item['Email']), str(item['ResearchDirection']),))
        self.conn.commit()
        return item
