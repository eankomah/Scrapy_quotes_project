# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import sqllite3 db 
import sqlite3


class ScrapyquotePipeline:
# initalize sqlite3 conn 
    def __init__(self):
        self.create_connection()
        self.create_table()

# create db connection 
    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()

#create table is in db
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tbl""")
        self.curr.execute("""create table quotes_tbl(
            title text,
            author text,
            tag text
        )            
        """)

#process and store response in the db
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    #class to store response in the db
    def store_db(self,item):
        self.curr.execute("""Insert into quotes_tbl values (?,?,?)""", (
            item['title'][0],
            item['author'][0],
            ",".join(item['tag'])
        ))
        self.conn.commit()
