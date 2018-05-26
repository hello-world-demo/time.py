#!/usr/bin/env python3

import os, sys

def run_command (cmd): #... missing argument
# https://sources.debian.org/src/time/1.7-25.1/time.c/
    pid = os.fork()
    if pid < 0:
        exit("cannot fork")
    elif 0 == pid:
        # If child.
        # Don't cast execvp arguments; that causes errors on some systems,
	      # versus merely warnings if the cast is left off.
        os.execvp(cmd[0], cmd)
        # error (0, errno, "cannot run %s", cmd[0]);
        os._exit(126) # errno == ENOENT ? 127 : 126
    print('pid:_'+str(pid)+'_')
    statusf = open('/proc/'+str(pid)+'/status', 'r') # This is not from time.c
    iof = open('/proc/'+str(pid)+'/io', 'r')
    os.wait4(pid, 0)
    print(statusf.read())
    print(io.read())

run_command("whoami")
