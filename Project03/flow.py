import httplib
import json
class StaticEntryPusher(object):

    def __init__(self, server):
      self.server = server

    def get(self, data):
      ret = self.rest_call({}, 'GET')
      return json.loads(ret[2])

    def Set(self, data):
      ret = self.rest_call(data, 'POST')
      return ret[0] == 200

    def remove( self, objtype, data ):
      ret = self.rest_call(data, 'DELETE')
      return ret[0] == 200

    def rest_call( self,data,action ):
      path = '/wm/staticentrypusher/json'
      header = {
        'Cantent-type':'application/json',
        'Accept':'application/json'
      }
      body = json.dumps( data )
      Conn = httplib.HTTPConnection( self.server,8080 )
      Conn.request( action,path,body,header )
      response = Conn.getresponse()
      ret = ( response.status,response.reason,response.read() )
      print ret
      Conn.close()
      return ret

pusher = StaticEntryPusher( '127.0.0.1' )

e1 = {
    "switch":"00:00:00:00:00:00:00:02",
    "name":"e1",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2",
}
e2 = {
    "switch":"00:00:00:00:00:00:00:01",
    "name":"e2",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=3",
}
e3 = {
    "switch":"00:00:00:00:00:00:00:03",
    "name":"e3",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=3",
}
e4 = {
    "switch":"00:00:00:00:00:00:00:05",
    "name":"e4",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "actions":"output=5",
}
e5 = {
    "switch":"00:00:00:00:00:00:00:0d",
    "name":"e5",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2",
}
e6 = {
    "switch":"00:00:00:00:00:00:00:08",
    "name":"e6",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"5",
    "active":"true",
    "actions":"output=3",
}
e7 = {
    "switch":"00:00:00:00:00:00:00:0a",
    "name":"e7",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.02",
    "ipv4_dst":"10.0.0.10",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "actions":"output=1",
}
e8 = {
    "switch":"00:00:00:00:00:00:00:0a",
    "name":"e8",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=2",
}
e9 = {
    "switch":"00:00:00:00:00:00:00:07",
    "name":"e9",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"4",
    "active":"true",
    "actions":"output=5",
}
e10 = {
    "switch":"00:00:00:00:00:00:00:0b",
    "name":"e10",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=3",
}
e11 = {
    "switch":"00:00:00:00:00:00:00:09",
    "name":"e11",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "actions":"output=5",
}
e12 = {
    "switch":"00:00:00:00:00:00:00:0c",
    "name":"e12",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=1",
}
e13 = {
    "switch":"00:00:00:00:00:00:00:04",
    "name":"e13",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"5",
    "active":"true",
    "actions":"output=3",
}
e14 = {
    "switch":"00:00:00:00:00:00:00:02",
    "name":"e14",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.10",
    "ipv4_dst":"10.0.0.02",
    "priority":"32768",
    "in_port":"3",
    "active":"true",
    "actions":"output=1",
}
e15 = {
    "switch":"00:00:00:00:00:00:00:07",
    "name":"e15",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.07",
    "ipv4_dst":"10.0.0.01",
    "priority":"32768",
    "in_port":"1",
    "active":"true",
    "actions":"output=3",
}
e16 = {
    "switch":"00:00:00:00:00:00:00:09",
    "name":"e16",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.07",
    "ipv4_dst":"10.0.0.01",
    "priority":"32768",
    "in_port":"2",
    "active":"true",
    "actions":"output=4",
}
e17 = {
    "switch":"00:00:00:00:00:00:00:06",
    "name":"e17",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.07",
    "ipv4_dst":"10.0.0.01",
    "priority":"32768",
    "in_port":"5",
    "active":"true",
    "actions":"output=4",
}
e18 = {
    "switch":"00:00:00:00:00:00:00:05",
    "name":"e18",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.07",
    "ipv4_dst":"10.0.0.01",
    "priority":"32768",
    "in_port":"4",
    "active":"true",
    "actions":"output=2",
}
e19 = {
    "switch":"00:00:00:00:00:00:00:01",
    "name":"e19",
    "eth_type":"0x0800",
    "ipv4_src":"10.0.0.07",
    "ipv4_dst":"10.0.0.01",
    "priority":"32768",
    "in_port":"5",
    "active":"true",
    "actions":"output=1",
}
pusher.Set( e1 )
pusher.Set( e2 )
pusher.Set( e3 )
pusher.Set( e4 )
pusher.Set( e5 )
pusher.Set( e6 )
pusher.Set( e7 )
pusher.Set( e8 )
pusher.Set( e9 )
pusher.Set( e10 )
pusher.Set( e11 )
pusher.Set( e12 )
pusher.Set( e13 )
pusher.Set( e14 )
pusher.Set( e15 )
pusher.Set( e16 )
pusher.Set( e17 )
pusher.Set( e18 )
pusher.Set( e19 )

