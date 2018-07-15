import sys
import basics as c

def main(a,b):
  print(a)
  print(b)
  print("tset")
  print('lonng')

  c.try_af.compare(a,b)
if __name__=="__main__":
    print('you are running {script}'.format(script=sys.argv[0]))
    a=int(sys.argv[1])
    b=int(sys.argv[2])
    main(a,b)


