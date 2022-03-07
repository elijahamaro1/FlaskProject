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

#makes factorials of a positive integer (Problem 2)
@app.route(
    '/factorial/<num>'
)  #i don't know how to make exceptions WITHIN the url, so what i'm going to do is take any possible item from the user and then see if it works within normal python code
def fact(num):
    try:  #this exists incase they put in a string, and catches it and makes a different error message then if they had inserted a bad number.
        num = float(num)
    except:
        return "ERROR: The value you have inserted is not a number! Please insert a integer greater then 0"
    #okay so in order to check if its a int, we actually do need to make it a float which i know is weird but trust me
    intcheck = num.is_integer()
    if num >= 0 and intcheck:  #for this i'm going to say that 0 counts as a positive, since 1 is the factorial of 0
        fact = 1
        if num == 0:
            return "Since your number is 0, its factorial is 1 by default"
        else:
            for i in range(1, int(num) + 1):
                fact = fact * i
            #in order to exist in the stame return statement, values are shifted from a number to a string, with num having int first so it loses its decimal places
            return "The factorial of " + str(int(num)) + " is " + str(fact)

    else:
        return "ERROR: That is not a appropriate value! It must be greater then 0 and be a whole number (a integer)"


app.run(host='0.0.0.0', port=5080)

#returns boolean value on whether the input is a prime number or not
@app.route('/is-prime/<int>')
def prime(number)
    # reusing some parts of the code from the factorial section, as it is effective and useful for the prime section
    try: 
        number = int(number)
    except:
        return "ERROR: The value you have inserted is NOT a number! Please insert an INTEGER greater than 0"
    if number >1:
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                return False
                break
        else:
            return True
    else:
        return "ERROR: The value you have inserted is not a PRIME number! Please insert an integer GREATER than 1"
    
app.run(host='0.0.0.0', port=5080)
    
