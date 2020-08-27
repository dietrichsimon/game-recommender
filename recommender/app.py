"""Flask application"""

import pickle

from flask import Flask, render_template, request

from recommender import recommender, sql_handling

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# read in ratings from sql database
ratings = sql_handling.db_to_df("reviews_small")

# load nmf model
infile = open("recommender/static/nmf", "rb")
nmf = pickle.load(infile)

# instantiate recommender
rec = recommender.Recommender(ratings, nmf)

# create ratings matrix
matrix = rec.create_rating_matrix()


@app.route("/")
@app.route("/index")
def index():
    """Route to index (main) page"""
    num = 3
    return render_template("index.html", num_html=num)


@app.route("/favorites")
def favorites():
    """Route to favourites (best-of) page"""
    return render_template("favorites.html")


@app.route("/worst_of")
def worst():
    """Route to worst-of page"""
    return render_template("worst_of.html")


@app.route("/results")
def results():
    """Calculate results and route to results page"""
    # get user input
    user_input = dict(request.args)
    user_titles = []
    for x in user_input.keys():
        if x == "algo":
            algo_choice = user_input[x]
        else:
            user_titles.append(user_input[x])
    # construct array
    input_array = rec.create_array(user_titles, matrix)
    # provide recommendations
    if algo_choice == "NMF":
        recommendations = rec.recommend_nmf(input_array, user_titles, matrix)
    elif algo_choice == "CoSim":
        recommendations = rec.recommend_cosim(input_array, user_titles, matrix)

    return render_template("results.html", movies_html=recommendations)
