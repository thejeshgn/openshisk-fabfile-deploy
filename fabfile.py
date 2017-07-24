from fabric.api import local

action_name = 'ping'

def setup():	
    local('virtualenv virtualenv')
    local('. virtualenv/bin/activate; pip install -r requirements.txt')


def package():
	#clean
    local('rm -rf virtualenv package.zip')
    #create a zip with all the dependecies
    local('zip -r package.zip __main__.py virtualenv/')


def update():
	cmd = 'wsk action update '+action_name+' --kind python:3 package.zip --web raw' 
	local(cmd)    


def create():
	cmd = 'wsk action create '+action_name+' --kind python:3 package.zip --web raw' 
	local(cmd)    

def delete():
	cmd = 'wsk action delete '+action_name
	local(cmd)    	