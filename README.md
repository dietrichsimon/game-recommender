# Board Game Recommender

Accessible [here](https://board-game-recommender.herokuapp.com/)

![](recommender_preview_1.gif)



### A website that recommends board games based on users' inputs

Users can choose to get recommendations either through Non-negative Matrix Factorization or Collaborative Filtering (Cosine Similarity).

Also provides information on all-time favorite games and games to avoid.

Technologies used: Python, Flask, Pandas, Scikit-learn, SQL, some HTML, JavaScript and CSS

Website hosted on heroku (webapp) and AWS (database).

![](recommender_preview_2.gif)



### Dataset

Reviews from boardgamegeek.com users published on [Kaggle](https://www.kaggle.com/jvanelteren/boardgamegeek-reviews?select=2019-05-02.csv). The recommender uses a sample of 100k reviews from the dataset (which contains 13 million reviews in total) with the sampling done at the user level.

### TO DO:

- ~~clean up code~~
- use large sample
- allow for undefined number of user inputs

