from flask import*
# Flask,render_template,jsonify,session
import random
app = Flask(__name__)
#temp=0
#session["point"]=temp
# Roll dice, if 6 reroll and remove 6.
def roll_dices():
    # How many dice.
    point = 0
    

    while point <= 100:
        point += dice_roll()
        if point%7==0:
            point=0
        
    return "congratulations"
        
    #print("The final sum is: " + str(final_sum))
    return point

def dice_roll():
    value = ((random.randint(1, 6)))
    return value

@app.route('/')
def index():
    return render_template('dice.html')

@app.route('/rollNdice/')
def rollDice():
    return jsonify({"sum":roll_dices()})

app.run(debug=True)