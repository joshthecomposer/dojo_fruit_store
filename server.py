from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    student_id = request.form.get('student_id')
    strawberry = request.form.get('strawberry')
    raspberry = request.form.get('raspberry')
    apple = request.form.get('apple')
    fruits = int(strawberry) + int(raspberry) + int(apple)
    current_time = datetime.datetime.now()
    print(f'Charging {first_name} for {fruits} fruits')
    
    return render_template("checkout.html", first_name=first_name, last_name=last_name, student_id=student_id, fruits=fruits, current_time=current_time, strawberry=strawberry, raspberry=raspberry,apple=apple)

@app.route('/fruits')         
def fruits():
    fruits_imgs = ['apple', 'blackberry', 'raspberry', 'strawberry']
    return render_template("fruits.html", fruits_imgs = fruits_imgs)

if __name__=="__main__":
    app.run(debug=True)