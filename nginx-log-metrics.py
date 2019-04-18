import re
import threading
import graphyte
import socket
import time
import argparse
from prometheus_client import start_http_server
from prometheus_client import Counter

parser = argparse.ArgumentParser()
parser.add_argument("ip", type=str, help="print your_ip for Graphite 2003_UDP or port_number for Prometheus with flag p")
parser.add_argument("-p", "--prometheus", action="count", default=0)
args = parser.parse_args()

total_requests = 0
upstream_requests = 0
total_bytes = 0

s = socket.gethostname()
name_total_requests ='nginx.'+ s + '.nginx-log-metrics.total_requests'
name_upstream_requests ='nginx.'+ s + '.nginx-log-metrics.upstream_requests' 
name_total_bytes ='nginx.'+ s + '.nginx-log-metrics.total_bytes'

graphyte.init(args.ip, prefix='', protocol='udp')
def metr_send():
    graphyte.send(name_total_requests, total_requests)
    graphyte.send(name_upstream_requests, upstream_requests)
    graphyte.send(name_total_bytes, total_bytes)
    time.sleep(10)
    
def count():
    c1.inc(total_requests)
    c2.inc(upstream_requests)
    c3.inc(total_bytes) 
    time.sleep(10)
    
if args.prometheus == 1: 
    p = int(args.ip)
    start_http_server(p)
    c1 = Counter('name_total_requests', 'Description of counter')
    c2 = Counter('name_upstream_requests', 'Description of counter')
    c3 = Counter('name_total_bytes', 'Description of counter')

while True:
    
    text = input()
    total_requests += 1
    
    pat1 = ('("\d+.\d+.\d+.\d+")'
            '(.+\[.+\])'
            '([^"]+"[^"]+")\s' 
            '([^\s]+)'
            ) 
    h1 = re.search(pat1, text)
    if h1 != None :
        t1 = text.replace(h1.group(0),"")
        pat2 = ('(\d+)') 
        h2 = re.search(pat2, t1)
        total_bytes += int(h2.group(0))
        t2 = t1.replace(h2.group(0),"")
        
        
        pat3 = ('([^"]+"[^"]+")\s' '("[^"]+")\s' '([^\s]+)\s') 
        h3 = re.search(pat3, t2)
        t3 = t2.replace(h3.group(0),"")
  
        pat4 = ('([^\s]+)') 
        h4 = re.search(pat4, t3)
        if h4.group(0) != '-' : upstream_requests += 1
    if args.prometheus == 0:
            if __name__ == '__main__':
                my_thread = threading.Thread(target=metr_send, args=())
                my_thread.start()
    elif args.prometheus == 1:
           if __name__ == '__main__':
                my_thread = threading.Thread(target=count, args=())
                my_thread.start() 
    else:
            print("error flag")
        

        

     

       
 
