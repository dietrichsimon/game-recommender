"""Make recommendations for board games"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class Recommender:
    '''Recommender class'''
    def __init__(self, ratings, nmf_model):
        self.ratings = ratings
        self.nmf_model = nmf_model

    def create_rating_matrix(self):
        """
        Parameters: None
        ---------------------
        Returns:
        - rating matrix based on ratings used for initialising the
        Recommender class (user base).
        """
        # create matrix of movie titles and users
        matrix = self.ratings.set_index(["user", "name"])["rating"].unstack()
        # fill NaNs with zeros
        matrix = matrix.fillna(0.0)
        return matrix

    def create_array(self, user_titles, matrix, max_rating=10.0):
        """
        Parameters:
        - user titles: list of titles suggested by the website user
        - matrix: rating matrix from user base
        ---------------------
        Returns:
        - Numpy array
        """
        query = np.zeros(len(matrix.columns))
        for i, title in enumerate(user_titles):
            query[list(matrix.columns).index(title)] = max_rating
        query = query.reshape(-1, 1).T
        return query

    def recommend_nmf(self, input_array, user_titles, matrix, no_recommendations=5):
        """returns a list with recommended games based on nmf"""
        new_pred = self.nmf_model.transform(input_array)
        new_pred = np.dot(new_pred, self.nmf_model.components_)
        recommendations = matrix.columns[
            np.argsort(new_pred)[0][-(no_recommendations * 100) :]
        ]
        recommendations = list(recommendations)
        recommendations.reverse()
        recommendations = [x for x in recommendations if x not in user_titles]
        return recommendations[:no_recommendations]

    def recommend_cosim(self, input_array, user_titles, matrix, no_recommendations=5):
        """returns a list with recommended games based on cosine similarity"""
        cosims = cosine_similarity(matrix, input_array)
        best_match = np.argmax(cosims)
        recommendations = matrix.iloc[best_match].sort_values(ascending=False)
        recommendations = list(recommendations.index)
        recommendations = [x for x in recommendations if x not in user_titles]
        return recommendations[:no_recommendations]
