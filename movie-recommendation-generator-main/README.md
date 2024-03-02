# Movie Recommendation Generator

## Project Overview:

This movie recommendation generator is built on user input and utilizes a dataset labeled as Data1. The process involves calculating movie similarities based on user interactions. The dataset is loaded into Python as Data1, and a matrix is created to calculate cosine similarity between movies paired with user ratings. The recommendation generator function, `get_rec`, is designed to provide movie recommendations based on a chosen movieId from Data1.

## Implementation:

### Data Processing:

- The dataset is loaded into Python as Data1, and similarities are calculated using the cosine similarity method.
- A matrix, `movie_matrix`, is created from Data1, and cosine similarity, `movie_similarity`, is calculated between movies.

### Recommendation Generator:

- The `get_rec` function is implemented to retrieve movie recommendations based on a user-input movieId.
- User input is accepted as a float value, and recommendations are generated using the cosine similarity scores.
- The top recommendations (defaulted to 10) are printed for the user, excluding the originally selected movieId.

## Requirements:

- Python 3.x

## Clone the repository:
git clone https://github.com/tokinsey/portfolio/edit/main/movie-recommendation-generator-main

## Navigate to the project directory: 
cd movie-recommendation-generator

## Requirements 
Python 3.x 
Pandas 
Sklearn
nlargest

## Contributing: 
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

##Contact:
For any inquiries or feedback, please reach out.

Happy movie watching!
