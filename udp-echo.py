#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import socket
import sys
from contextlib import closing

def main(args):

  bufsize = 4096

  # 引数に設定がある場合は引数を使う
  # 第一引数:受信ipアドレス
  # 第二引数:受信ポート
  if len(args) == 3 :
    localhost=args[1]
    localport=int(args[2])
  else : # 引数がない場合はループバックアドレス等を設定
    localhost = '127.0.0.1'
    localport = 6000
  print('Started listening ' + localhost + ':' + str(localport) )
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    sock.bind((localhost, localport))
    while True:
      #バッファサイズ内のデータを取得
      #return : (bytes,address)
      recvobj=sock.recvfrom(bufsize)
      #udp payload取得
      message=recvobj[0]
      #送信元アドレス取得
      address=recvobj[1]
      
      #送信元アドレス取得
      remotehost=address[0]
      remoteport=address[1]
      #print(message)
      #print(remotes)
      sock.sendto(message,(remotehost,remoteport))
  return

if __name__ == '__main__':
  main(sys.argv)
