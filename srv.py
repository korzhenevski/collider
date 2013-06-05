#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, random 

import logging, sys
from flask import Flask, request, make_response 
app = Flask(__name__)

logging.basicConfig(stream=sys.stderr)

def log_to_file( data ):
	with open('/tmp/urls', 'w') as fp:
		fp.write( json.dumps( data ) )

def update( data ):
	pass;

def remove( data ):
	pass;

def add_response_headers( headers={} ):
	resp = make_response(f(*args, **kwargs))
	h = resp.headers
	for header, value in headers.items():
		h[header] = value
	print 'OK~'
	return resp

@app.route("/")
def index():
	action = request.args.get('action')
	YPResponse = 1
	msg = 'ok'
	sid = random.getrandbits(32)  
	if action == 'touch': 
		update( request.args )
	elif action == 'add':
		log_to_file( request.args )
	elif action == 'delete':
		remove( request.args )
	else :
		YPResponse = 0
		msg = 'no action provided'
		sid = -1
				
	response = make_response()
	response.headers['YPResponse'] = YPResponse
	response.headers['YPMessage:'] = msg
	response.headers['SID'] = sid
	return response

if __name__ == '__main__':
	app.run()
