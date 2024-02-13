#!/usr/bin/env python3

Auth = __import__('auth').Auth
excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/'
        ]
auth = Auth()
#print(auth.require_auth('/api/v1/status/*', excluded_paths))
print(excluded_paths[0][:-1])