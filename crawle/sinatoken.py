#-*- encoding: utf-8 -*-
'''
Created on 2013-1-17

@author: Zoe
'''
import urllib2
import urllib
import json
from util.weibo import APIClient
import time

class SinaToken():
    
    def __init__(self):
        pass
    
    def reg_apiclients(self, tokens):
        '''
        tokens: a tuple list,contain (app_key, token string, expires_in integer)
                or
                a list,contain token string
        '''
        clients = []
        temp_expires = int(time.time()) + (3600*24*60)
        for token in tokens:
            if not token:
                continue
            if isinstance(token, tuple):
                client = APIClient(token[0], '')
                if token[2] > 0:
                    et = token[2]
                else:
                    et = temp_expires
                client.set_access_token(token[1], et)
            if isinstance(token, dict):
                client = APIClient(token.get('app_key', ''), '')
                if token.get('token', ''):
                    client.set_access_token(token.get('token', ''), token.get('expires_in', temp_expires))
            else:
                client = APIClient('', '')
                client.set_access_token(token, temp_expires)
            clients.append(client)
        return clients
        
    def get_token(self, login_un, login_pw, app_key, app_sec=''):
        AUTHORIZE_URL = "https://api.weibo.com/oauth2/authorize"
        #ACCESS_TOKEN_URL = "https://api.weibo.com/oauth2/access_token"
        ref_url = 'https://api.weibo.com/oauth2/authorize?redirect_uri=&response_type=code&client_id=%s&display=default' % app_key
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Connection": "keep-alive",
                   'Referer'  :  ref_url,}
        data = {'action': 'submit',
                'withOfficalFlag': 0,
                'ticket': '',
                'isLoginSina': '',
                'response_type': 'token',
                'regCallback': '',
                'redirect_uri': '',
                'client_id': app_key,
                'state': '',
                'from': '',
                'userId': login_un,
                'passwd': login_pw,
                'display': 'js',}
        url = AUTHORIZE_URL
        request = urllib2.Request(url=url.strip(), headers=headers)
        request.add_data(urllib.urlencode(data))
        try:
            response = urllib2.urlopen(request, timeout=15)
            code = response.getcode()
        except urllib2.HTTPError, e:
            code = e.code
        if "200" in str(code):
            try:
                html = response.read()
                sindex = html.find('({"')
                html = json.loads(html[sindex+1: html.rfind('})', sindex)+1])
                
                return html.get('access_token'), int(html.get('expires_in')) + int(time.time()), html.get('uid')
            except:
                pass
        return None

if __name__ == '__main__':
    print 'start.'
    st = SinaToken()
    #211160679    appscrect:63b64d531b98c2dbff2443816f274dd3
   # APP_KEY = u'2735371158'
   # APP_SECRET = u'fa2318d3281101f0c9b1be38f499dda4'
    APP_KEY=u'211160679'
    APP_SECRET=u'63b64d531b98c2dbff2443816f274dd3'

    #print st.get_token('zoe0316@live.cn', 'zzbb02090417', APP_KEY, APP_SECRET)
    #print st.get_token('cidians@126.com', 'guoxingyu1234', APP_KEY, APP_SECRET)
    #(u'2.008bhtYC06XASO8d4222c0abw5bqbE', 1382900402, u'2347936741')
    clients=st.reg_apiclients([{'app_key':211160679 , 'token': "2.008bhtYC06XASO8d4222c0abw5bqbE", 'expires_in':1382900402 }])
    #print clients
    
    #r= clients[0].statuses.update.post(status=u'fuck ,go!!')
    #print r
   # r=clients[0].statuses.public_timeline.get()
    #print  json.dumps(r).decode("unicode_escape");
    
    
    '''
    for i in range(100):
        r=clients[0].users.show.get(uid=2187711961)
        print  json.dumps(r).decode("unicode_escape");
    '''    
    
    r=clients[0].statuses.timeline_batch.get(uids=2187711961)
    print i, len(r.get('statuses'))
    
        
    
