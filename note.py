# coding=utf-8
import sqlite3
import sys
from address import Address
import re
from model import Model
class Note(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.Address=Address()
        self.cur.execute("""create table if not exists note(
        id integer primary key autoincrement,
        user_id text,
        note text,
            address_id text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def getallbyuserid(self,userid):
        self.cur.execute("select note.*,address.address from note left join address on address.id = note.address_id where note.user_id = ?",(userid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select note.*,address.address from note left join address on address.id = note.address_id")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from note where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,myid):
        self.cur.execute("select * from note where id = ?",(myid,))
        row=dict(self.cur.fetchone())
        print(row["id"], "row id")
        job=self.cur.fetchall()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'address' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        someaddress=Address().create({"address":params["address"]})
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        myhash["address_id"]=someaddress["address_id"]
        try:
          self.cur.execute("insert into note (note,user_id,address_id) values (:note,:user_id,:address_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["note_id"]=myid
        azerty["notice"]="votre note a été ajouté"
        return azerty




