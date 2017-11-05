
import json

def build_header(access_token):
    header = {}
    header.update({'Content-Type' :'application/json' })
    header.update({'Accept' :'application/json' })
    header.update({'Access-Token' : access_token })
    return header

def build_host(host):
    if "http" not in host:
        return "https://"+host
    return host
