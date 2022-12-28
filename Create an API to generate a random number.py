from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def generate_random_number():
    # Set the minimum and maximum values to 1 and 5, respectively
    min_value = 1
    max_value = 5
    
    # Generate a random number within the given range
    random_number = random.randint(min_value, max_value)
    
    return str(random_number)

if __name__ == '__main__':
    app.run()
