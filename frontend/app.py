    
from flask import Flask, render_template
from datetime import datetime

BACKEND_URL= 'http://0.0.0.0:9000'

app = Flask(__name__)

@app.route('/')
def home():
    
    day_of_week = datetime.today().strftime('%A')
    
    current_time = datetime.now().strftime('%H:%M:%S')
    
    return render_template('index.html', day_of_week = day_of_week, current_time=current_time)



if __name__ == '__main__':
       app.run( host='0.0.0.0',port=8000,debug=True)
    
    