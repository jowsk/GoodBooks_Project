# GoodBooks_Project

## Overview

This project explores various methods for predicting user book preferences and making recommendations. It compares content filtering, collaborative filtering via matrix factorization, and collaborative filtering using a Light Graph Convolution Network (LightGCN).

## Methods

1. *Content Filtering*
    - Uses handcrafted, interpretable features based on book tags.
    - Predicts user preferences by analyzing the categories of books they have rated.

2. *Matrix Factorization*
    - Employs collaborative filtering to learn latent features.
    - Decomposes the user-book matrix into user and book matrices to predict ratings.

3. *Light Graph Convolution Network (LightGCN)*
    - Uses graph convolution to aggregate features from neighboring nodes.
    - Propagates messages through multiple layers to enhance collaborative filtering.

## Dataset

The dataset used is the [goodbooks-10k](https://example.com/dataset), which includes 10,000 books rated by 53,424 users from the GoodReads website. The dataset comprises:
- ratings.csv: Contains user ID, book ID, and rating.
- book_tags.csv and tags.csv: Provide book tags and their corresponding names.

## Installation

To run the project, you need to install the following dependencies:

bash
pip install numpy pandas matplotlib scikit-learn torch torch-geometric networkx tqdm seaborn scipy


## Usage

The project consists of three main files:

1. `content_filtering.ipynb`: Implements content-based filtering using book tags.
2. `matrix_factorization.ipynb`: Implements matrix factorization for collaborative filtering.
3. `LightGCN.ipynb`: Implements LightGCN for collaborative filtering.
4. `preprocess.py`: Contains functions for data preprocessing.
5. `preprocess_categories.ipynb`: Preprocesses book tags and categories for content filtering.
6. `Data_overview.ipynb`: Provides an overview of the dataset.

## Results

- *Content Filtering*: Achieved an RMSE of 1.21, offering interpretable and personalized recommendations.
- *Matrix Factorization*: Achieved a test RMSE of 0.973, leveraging user similarities for accurate predictions.
- *LightGCN*: Achieved precision and recall rates of 60.8% and 60.4%, respectively, showing promise with graph-based techniques.

## Future Work

- Improve LightGCN performance by running more epochs and more data. (Currently 30000 users)
- Explore hybrid models combining content and collaborative filtering for better accuracy.

## References

- Vali, Sadak. "Implementing Matrix Factorization Technique for Recommender Systems from scratch." Medium, March 2023. [Link](https://medium.com/@rebirth4vali/implementing-matrix-factorization-technique-for-recommender-systems-from-scratch-7828c9166d3c)
- He, Xiangnan, et al. "LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation." arXiv preprint arXiv:2002.02126, July 2020. [Link](https://arxiv.org/abs/2002.02126)
- Chen, Denise. "Recommender System — Matrix Factorization." Towards Data Science, July 2020. [Link](https://towardsdatascience.com/recommender-system-matrix-factorization-ce04322c6245)

