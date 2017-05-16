#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import socket
import sys
from contextlib import closing

def main(args):

  bufsize = 4096
  print(args)
  print(len(args))
  if len(args) == 3 :
    localhost=args[1]
    localport=int(args[2])
  else :
    localhost = '10.0.0.1'
    localport = 6000

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    sock.bind((localhost, localport))
    while True:
      recvobj=sock.recvfrom(bufsize)
      message=recvobj[0]
      remotes=recvobj[1]
      remotehost=remotes[0]
      remoteport=remotes[1]
      print(message)
      print(remotes)
      sock.sendto(message,(remotehost,remoteport))
  return

if __name__ == '__main__':
  main(sys.argv)
