#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask import Flask, request, make_response
app = Flask(__name__)


def log_to_file( data ):
	with open('/tmp/urls', 'w') as fp:
		fp.write( json.dumps( data ) )

def add( data ):
	pass;

def delete( data ):
	pass;

@app.route("/")
def index():
	action = request.args.get('action')
	if action == 'touch': 
		log_to_file( request.args )
	elif action == 'add':
		add( request.args )
	elif action == 'delete':
		delete( request.args )
		
	response = make_response()
	response.headers['YPResponse'] = 1
	response.headers['YPMessage:'] = 'ok'
	response.headers['SID'] = 1
	return response

if __name__ == '__main__':
	app.run()
