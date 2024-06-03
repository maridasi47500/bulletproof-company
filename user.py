# coding=utf-8
import sqlite3
import sys
import re
from model import Model
import requests
from bs4 import BeautifulSoup
import urllib.request
from country import Country
from chercherimage import Chercherimage
class User(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists user(
        id integer primary key autoincrement,
        username text,
        country_id text,
        sex text,
        job text,
        facebooktoken text,
        phone text,
        email text,
latitude text,
longitude text,
            password text
                    );""")
        self.con.commit()
        #self.con.close()
    def getall(self):
        self.cur.execute("select * from user")

        row=self.cur.fetchall()
        return row
    def updatelocation(self,latitude,longitude,myid):

        self.cur.execute("update user set latitude = ?, longitude = ? where id = ?",(latitude, longitude, myid,))

        self.con.commit()
        job=self.cur.lastrowid
        self.cur.execute("select * from user where id = ?",(myid,))
        job1=self.cur.fetchone()
        print(dict(job1))
        
        return job1["latitude"] == latitude and job1["longitude"] == longitude
    def deletebyid(self,myid):

        self.cur.execute("delete from user where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyphonepw(self,email,pw):
        self.cur.execute("select * from user where phone like ? and password = ?",(email,pw,))
        azerty=self.cur.fetchone()
        row=dict({})
        if azerty:
          row=dict(azerty)
          row["user_id"]=row["id"]
          row["notice"]="Vous êtes connecté(e)"
          print(row["id"], "row id")
        else:
          row=dict({})
          row["notice"]="le numero de téléphone ou le mot de passe ne sont pas bon"
          row["user_id"]=""
        return row
    def getbyid(self,myid):
        try:
           self.cur.execute("select * from user where id = ?",(myid,))
           row=dict(self.cur.fetchone())
           print(row["id"], "row id")
           job=self.cur.fetchall()
           return row
        except:
           return None
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        azerty={}



        try:
            if params["password"] == params["passwordconfirmation"]:
                 del myhash["passwordconfirmation"]
                 del myhash["someurl"]
                 self.cur.execute("insert into user (job,facebooktoken,sex,username,email,country_id,phone,password) values (:job,:facebooktoken,:sex,:username,:email,:country_id,:phone,:password)",myhash)
                 self.con.commit()
                 myid=str(self.cur.lastrowid)
                 opener=urllib.request.build_opener()
                 opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
                 urllib.request.install_opener(opener)
                 urllib.request.urlretrieve(params["someurl"], f'./uploads/'+str(myhash["country_id"])+"_"+str(myhash["sex"])+'_'+str(myid)+'_Profilepic.jpg')

                 azerty["notice"]="votre user a été ajouté"
            else:
                 myid=None
                 azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"
            azerty["user_id"]=myid
            q="woman man "+(Country().getbyid(params["country_id"])["name"])+" musician"
            xx=Chercherimage(q).search()
            y=0
            while y<10:

                opener=urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(("https://images.google.com" if "http" not in xx[y]["src"] else "")+xx[y]["src"], f'./uploads/'+str(myhash["country_id"])+"_"+'musician'+'_'+str(y)+'_pic.jpg')
                y+=1

        except Exception as e:
            print("my error"+str(e))
            azerty["user_id"]=None
            azerty["notice"]="votre user n'a pas été ajouté les mots de passe ne sont pas identiques"+str(e)


        return azerty




