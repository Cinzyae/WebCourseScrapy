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
        self.curr.execute("""CREATE TABLE TINFO(TITLE TEXT)""")
        self.conn.commit()

    def process_item(self, item, spider):
        print(item['Title'])
        self.curr.execute("""insert into tinfo values (%s)""", (str(item['Title']),))
        self.conn.commit()
        return item
