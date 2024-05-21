from subprocess import check_output as runmyscript
class Lignecommande:
  def __init__(self,myscript=""):
    self.myscript=myscript
  def ligne(self,lignecommande=""):
    self.hey=lignecommande
    self.someargs=lignecommande.split(" ")
  def myargs(self,a):
    #print(a)
    for x in a:
        print("arg len",len(x))
    self.someargs=a
  def run(self):
    mypwd=runmyscript("pwd").decode()
    str="""xterm -l -hold -e "cd '{mypwd}' & echo '{myscript}' & bash -l -c '{ligne}'" """.format(mypwd=mypwd,myscript=self.myscript,ligne=self.hey.replace('"',"'"))
    runmyscript(str, shell=True)
    
