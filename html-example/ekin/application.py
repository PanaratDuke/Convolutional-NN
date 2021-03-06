# Author: Henry Le
# Date: Jul. 18, 2020
# version 0 - first release
# if you some how find this file of mine on github, please feel free to take and modify it. I wish you the best of luck on what you want to do.
# learning coding is not easy as it's about learning a new language but definitely FUN FUN FUN !!!
# HAVE FUN !

# dependencies
#from  prediction import img_predict
from flask import Flask, jsonify, render_template


################## Flask App set up###############
app = Flask(__name__)
##################################################

####### custome routes for website and data######
# main home page route
@app.route("/")
def home_page():
    ''' Home Page Access Route'''
    return render_template("index_panarat.html")





# country count per year
@app.route("/prediction")
def get_countryCount_Year_Filterable():
    return jsonify(data.get_countryCount_perYear_perCountry())


# if program is run from this file ::
if __name__ == '__main__':
    app.run(debug=True)