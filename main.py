from flask import Flask
import hashlib
app = Flask('app')

@app.route('/')
#sets the default page, we may remove this later
def hello_world():
  return 'Hello, World!'
#takes a string from the url and converts to a hashcode (Problem 1)
@app.route('/md5/<string>')
def md5machine(string):
  #hashes it
  hashed = hashlib.md5(string.encode())
  return (hashed.hexdigest())

app.run(host='0.0.0.0', port=5080)
