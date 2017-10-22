
import json

def buildHeader(access_token):
    header = {}
    header.update({'Content-Type' :'application/json' })
    header.update({'Accept' :'application/json' })
    header.update({'Access-Token' : access_token })
    return header

def buildHost(host):
    if "http" not in host:
        return "https://"+host
    return host
