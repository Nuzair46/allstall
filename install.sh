#! /bin/bash
## #############################################
## Install allstall application:
## allstall.py         ---> $HOME/.local/bin/
## By Nuzair Rasheed
## #############################################

rm /usr/bin/allstall -r >/dev/null 2>&1
chmod +x allstall.py
cp allstall.py /usr/bin/allstall


echo
echo "------------------------------------------------------------"
echo "Installation complete. Type allstall to run the application."
echo "------------------------------------------------------------"
echo
