#!/usr/bin/python

## MixTe Is A Simple Script For Make A Great Fonts On Your Text
## By: Oseid Aldary

try:

 import pyfiglet,optparse

except:

  print("[!] Error: Please Install PyFiglet Library Use Command:> \033[1;32mpip install pyfiglet")
  exit(1)

parse = optparse.OptionParser("""
Usage: python MixTe.py [OPTION..]

OPTIONS:
--------
  J    | -t --text    >> Your Name Or Nickname Or Any Text
      <^>
  O    | -s --show    >> SHOW All Fonts You Can Use With Example
      <^>
  K    | -f --font    >> Set Font Name You Want
      <^>
  E    | -a --all     >> Use all Fonts With Your Text
       |
  R    Examples:
       ---------
  1	       | python MixTe.py --show
	       | python MixTe.py -t Python -f speed
  1	       | python MixTe.py -t Oseid --all
----------------
""",version='1.0')
def Main():
  parse.add_option("-t",'-T','--text','--TEXT',dest="tex",type="string")
  parse.add_option('-f','-F','--font','--FONT',dest='font',type="string")
  parse.add_option('-s','-S','--show','--SHOW',action='store_true',dest='show',default=False)
  parse.add_option('-a','-A','--all','--ALL',action='store_true',dest='all',default=False)
  (options, args) = parse.parse_args()
  if options.show:
	text = "Your Text"
	fonts = pyfiglet.FigletFont.getFonts()
	loop = 1
	try:
	 for f in fonts:
	    print("\033[1;32m[\033[1;37m{}\033[1;32m] Font Name: \033[1;33m{}".format(loop,f))
	    loop +=1
	    print("\033[1;32m[#] Example:\n\033[1;36m")
	    pyfiglet.print_figlet(text,f)
	    print("\033[1;35m")
	    print("="*60)
	except KeyboardInterrupt:
		print("\n\033[1;31m[Ctrl+c]\033[1;33m Exit!")
		exit(1)

  elif options.tex !=None and options.font !=None:
	text = options.tex
	font = options.font
	fonts = pyfiglet.FigletFont.getFonts()
	if font in fonts:
            print("\033[1;32m[\033[1;37m~\033[1;32m] Font Name: \033[1;33m{}".format(font))
            print("\033[1;32m[T]\033[1;37m Your Text:\033[1;33m {}\n\033[1;37m\nOutput:\n".format(text))
            pyfiglet.print_figlet(text,font)
	else:
	   print("\n\033[1;31m[!]\033[1;33m Error:\033[1;37m Unknown \033[1;33m[{}]\033[1;37m Font Name\n\033[1;32m[*]\033[1;37m Please Try Use:\033[1;32m --show >\033[1;37m For Show All Fonts Names You Can Set With Examples".format(font))
	   exit(1)
  elif options.tex !=None and options.all:
        text = options.tex
        fonts = pyfiglet.FigletFont.getFonts()
        loop = 1
        try:
         for f in fonts:
            print("\033[1;32m[\033[1;37m{}\033[1;32m] Font Name: \033[1;33m{}".format(loop,f))
            loop +=1
            print("\033[1;32m[T]\033[1;37m Your Text:\033[1;33m {}\n\033[1;37m\nOutput:\n".format(text))
            pyfiglet.print_figlet(text,f)
            print("\033[1;35m")
            print("="*60)
        except KeyboardInterrupt:
                print("\n\033[1;31m[Ctrl+c]\033[1;33m Exit!")
                exit(1)
  else:
	print(parse.usage)
	exit(1)


if __name__=="__main__":
	Main()

##############################################################
##################### 		     #########################
#####################   END OF TOOL  #########################
#####################                #########################
##############################################################
#This Tool by Oseid Aldary
#Have a nice day :)
#GoodBye


