import sys

from boardeval import boardeval
from getmove import getmove
from gameover import gameover
from printboard import printboard

if __name__ == "__main__":

   try:

      fd = open("boards.save", "r")    # this file is my responsibility
   except:
      print("no board file")
      sys.exit(0)

   for line in fd.readlines():
      line = line.strip()
      s,t = line.split(" ")
      b = [int(c) for c in s]
      who = int(t)

      #print(boardeval(b, who))
      print(getmove(b, who))
      print(printboard(b))
