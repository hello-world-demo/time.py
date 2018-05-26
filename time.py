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
    print('ppid:_'+str(os.getpid())+'_')
    print('pid:__'+str(pid)+'_')
    pcmdlinef = open('/proc/'+str(os.getpid())+'/cmdline', 'r')
    cmdlinef = open('/proc/'+str(pid)+'/cmdline', 'r') # This is not from time.c
    statusf = open('/proc/'+str(pid)+'/status', 'r')
    iof = open('/proc/'+str(pid)+'/io', 'r')
    print(pcmdlinef.read())
    print(cmdlinef.read())
    os.wait4(pid, 0)
    print("Child just terminated.")
    # print(statusf.read()) # ProcessLookupError: [Errno 3] No such process
    # print(io.read())

run_command(["cat", "/proc/self/cmdline"])
run_command(["grep", "Pid:", "/proc/self/status"])
run_command(["sleep", "1"])
run_command(["whoami"])
