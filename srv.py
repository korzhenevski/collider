#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, random 

import logging, sys
from flask import Flask, request, make_response 
app = Flask(__name__)

logging.basicConfig(stream=sys.stderr)

def log_to_file( data ):
	with open('/tmp/urls', 'a') as fp:
		fp.write( json.dumps( data ) )

def update( data ):
	pass;

def remove( data ):
	pass;

def add_response_headers( YPResponse, YPMessage, sid  ):
	headers = { 'YPResponse' : YPResponse, 'YPMessage' : YPMessage, 'SID': sid }  			
	resp = make_response()
	h = resp.headers
	for header, value in headers.items():
		h[header] = value
	return resp

@app.route("/")
def index():
	action = request.args.get('action')
	sid = random.getrandbits(32)  

	if action == 'touch': 
		update( request.args )
		return add_response_headers(1, 'update ok', sid)

	elif action == 'add':
		log_to_file( request.args )
		return add_response_headers(1, 'added ok', sid )

	elif action == 'delete':
		remove( request.args )
		return add_response_headers(1, 'delete ok', sid )

	else :
		return add_response_headers(0, 'no action provided', -1)
				

if __name__ == '__main__':
	app.run()
