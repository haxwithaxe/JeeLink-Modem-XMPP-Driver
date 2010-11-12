#!/usr/bin/python2.6

import sys,pytty,threading,sleekxmpp

class device(threading.Thread):
   self.name = 'default_username'
   self.password = 'internal static value'
   self.stylesheet = '/path/to/xslt/stylesheet'
   self.id = 000000
   self.xmpp = None
   self.msg = None

   def init(self):
      # open xmpp
      self.xmpp = sleekxmpp.BaseXMPP(self.name,self.password)
      self.xmpp.sendPresence()

   def run(self):
      # grab xmpp then send it to serial
      self.rxd()

   def rxd(self):
      # take msg (from xmpp) and send it to this device

   def txd(self,msg):
      # take msg (from device) and send it to xmpp
      self.xmpp

