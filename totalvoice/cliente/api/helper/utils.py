
import json

def build_header(access_token):
    header = {}
    header.update({'Content-Type' :'application/json' })
    header.update({'Accept' :'application/json' })
    header.update({'Access-Token' : access_token })
    header.update({'User-Agent': 'lib-python/1.7.0' })
    return header

def build_host():
    return 'https://voice-api.zenvia.com'