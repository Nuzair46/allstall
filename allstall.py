#!/usr/bin/env python3
###### Auther: @rednek46 ######
import os,sys,subprocess,re

def debpack(pack):													# for .deb packages
	print ("\nExecuting command : apt install ./%s" % (pack))
	print ("\nInstalling %s on your system.\n" % (pack))
	install = "sudo apt -y install ./%s" % (pack)												
	os.system(install)												
	flag=1

def gitclone(pack):													#for git 
	print ("\nExecuting command : git clone %s" % (pack))
	print ("\nCloning %s on your system.\n" % (pack))
	clone = "git clone %s" % (pack)
	url = pack
	os.system(clone)												
	pUrl = re.split("/",url) 
	pUrl = pUrl[len(pUrl)-1]											
	pUrl = pUrl[:-4]
	os.system("cd %s" % (pUrl))
	
def repo(pack):														#for repo
	print ("\nExecuting command : apt install %s" % (pack))
	print ("\nInstalling %s on your system.\n" % (pack))
	install = "sudo apt-get -y install %s" % (pack)
	os.system(install)	
	
def tarball(pack):
	loc = input("Enter directory to extract to: ")
	makeDir = "sudo mkdir -p %s >/dev/null 2>&1" % (loc)
	os.system(makeDir)
	print ("\nExtracting..."
	if loc == '':
		extract = "sudo tar -xvf %s" % (pack)
	else :	
		extract = "sudo tar -xvf %s -C %s" % (pack,loc)
	os.system(extract)
	
#DEFINE THE INSTALLERS HERE!!!
	
	
def extDet():
	j=2
	while j < xlen:
		name, ext = os.path.splitext(x[j])
		if ext == '':
			repo(x[j])
			j +=1
		else:
			j +=1
			continue
def emp():	
	print ("\nUsage: allstall [option] [package_name(s)]\n\nUse: 'allstall --help' for detailed help\n")
	print ("Exiting...")
	exit(0)
		
def help():														#help section
	print ("\tHelp section\n\nUsage: python3 install.py [option] [package_name(s)]\n\n\n[options] : -p\n\t must use this option while trying to install repository packages\n\nCan install or download multiple file types that are supported at the same time.\n")
	
def dev():
	while True:
		print ("\n\n\n\tDeveloper section\n")
		ch = input("[1] - Fix Apt errors\n[2] - Edit sources.list\n[3] - Exit\n\nOption: ")			#developer section
		if ch == '1':
			print ("\nPlease wait for the process to complete.\n")							
			os.system("sudo apt-get install --fix-broken >/dev/null 2>&1") 					#Fix; attempt to correct a system with broken dependencies in place.
			os.system("sudo apt-get install --fix-missing >/dev/null 2>&1")
			os.system("sudo apt-get auto-remove >/dev/null 2>&1")
			print("\nPerforming 'apt-get update'.\n")
			os.system("sudo apt-get update")
		elif ch == '2':
			os.system("sudo nano /etc/apt/sources.list")
		else:
			print ("\nExiting...")
			exit(0)
		
#DEFINE SUPPORTING CODES HERE!!!	
	
	
	
	
		
xlen = len(sys.argv)
x = [0] * xlen

i = 1
for i in range(xlen):
	x[i]=str(sys.argv[i])
if xlen == 1:
	emp()

#Installation type selector
#add if-else statements for newly defined installations below.
i=1
while i < xlen:
	if x[i] == "-p":
		extDet()
		
	elif x[i].endswith('.deb'):
		debpack(x[i])
	
	elif x[i].endswith('.tar.gz'):
		tarball(x[i])
	
	elif x[i].endswith('.git'):
		gitclone(x[i])
		
	elif xlen == 2:	
		if x[i].startswith('--'): 
			if x[i] == "--dev":
				dev()
			elif x[i] == "--help":
				help()
			else:
				emp()
					
	elif x[i] == "--help":
		continue
	
	elif x[i] == "--dev":
		continue
			
	else :
		name, ext = os.path.splitext(x[i])
		if ext != '':
			print ("Sorry, Extention of %s not supported currently." % x[i])
	i += 1
	
#end
