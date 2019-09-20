#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import requests
import threading
import json
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def yenitask(urllink):
    
    veri= requests.get('http://127.0.0.1:8775/task/new')
    veri= json.loads(veri.text)
    taskid = veri['taskid'] 
    print "yeni task "+taskid
    veri= requests.post("http://127.0.0.1:8775/scan/"+taskid+"/start",data=json.dumps({'url':urllink}),headers = {'Content-Type':'application/json'})
    veri= json.loads(veri.text)
    
    if veri['success'] :
        while  True:
            time.sleep(20)
            veri= requests.get("http://127.0.0.1:8775/scan/"+taskid+"/status")
            veri= json.loads(veri.text)
            if veri['returncode'] == 0  :
                veri= requests.get("http://127.0.0.1:8775/scan/"+taskid+"/data")
                veri= json.loads(veri.text)
                print veri['data']
                #print len(veri['data'])
                if len(veri['data']) == 0:
                    print urllink+" --->BULAMADI"
                else:
                    print urllink+" --->BULDU"
                    

if __name__ == "__main__":
    Url = sys.argv[1]
    print Url
    yenitask(Url)    

