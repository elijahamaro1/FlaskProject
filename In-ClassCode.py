#code we went over in class yesterday (wenesday) in case anyone needs a general understanding of what we will be doing for this project

#this is particulary for replit.com, I have not learned how to use this code for a different website just yet
#the comments in the code were for me personally, but feel free to read them if you like

#also this is just the flask portion of the lab, we did not go over docker just yet, although it is a lab assignment

from flask import Flask, escape, request
import json

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!"

#https://classtestingpy.elijahamaro1.repl.co/name/gerald this exact link will print out
#Hello, gerald!
@app.route('/name/<first_name>')
def hello(first_name):
  #name = request.args.get("first_name", "Marcus")
  name = first_name
  return f'Hello, {name}!'

#https://classtestingpy.elijahamaro1.repl.co/random/seven this link will
#output "my number is: seven" on the screen
@app.route('/random/<string:num>')
def moretesting(num):
  return f"my number is: {num}"

#https://classtestingpy.elijahamaro1.repl.co/number/1466 this prints out
# {"input": 1466, "output": "Distraction"}
@app.route('/number/<int:num>')
def number(num):
  output = {
    "input": num,
    "output": "Distraction"
  }
  return json.dumps(output)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port = '5000')
