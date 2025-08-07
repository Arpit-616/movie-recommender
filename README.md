# Movie Recommender System

A modern web application that recommends movies based on user-selected genres using machine learning techniques.

## Features

- 🎬 **Genre-based Recommendations**: Get movie recommendations based on your favorite genres
- 🎨 **Modern UI**: Beautiful, responsive design with smooth animations
- ⚡ **Fast Performance**: Optimized with TF-IDF vectorization and cosine similarity
- 📱 **Mobile Friendly**: Responsive design that works on all devices
- 🔍 **Smart Search**: Intelligent movie matching using machine learning

## Project Structure

```
movie-recommender/
│
├── app.py              # Main Flask application
├── templates/
│   └── index.html     # HTML template
├── static/
│   └── style.css      # CSS styling
├── vectorizer.pkl     # TF-IDF vectorizer (auto-generated)
├── vectors.pkl        # Similarity vectors (auto-generated)
├── movies.csv         # Movie dataset (auto-generated)
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:

   ```bash
   python app.py
   ```

4. **Open your browser** and go to `http://localhost:5000`

## How It Works

### Machine Learning Pipeline

1. **Data Processing**: The system uses a sample dataset of 100 movies with titles, genres, and tags
2. **Feature Extraction**: TF-IDF vectorization combines movie titles, genres, and descriptions
3. **Similarity Calculation**: Cosine similarity finds the most similar movies to user input
4. **Recommendation**: Returns top 10 most similar movies based on genre preferences

### Technology Stack

- **Backend**: Flask (Python web framework)
- **Machine Learning**: scikit-learn (TF-IDF, Cosine Similarity)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with gradients and animations
- **Icons**: Font Awesome

## Usage

1. **Select a Genre**: Choose from the dropdown menu of available genres
2. **Get Recommendations**: Click "Get Recommendations" to see similar movies
3. **Explore Results**: Browse through the recommended movies with their genres and descriptions

## Customization

### Adding Your Own Movie Data

To use your own movie dataset:

1. Create a `movies.csv` file with columns:

   - `Title`: Movie title
   - `tags`: Keywords/descriptions
   - `genres`: Comma-separated genres

2. The system will automatically regenerate the model files when you restart the application.

### Modifying the Model

You can customize the recommendation algorithm by editing `app.py`:

- Change `max_features` in TfidfVectorizer for different vocabulary sizes
- Modify the feature combination in `combined_features`
- Adjust the number of recommendations returned

## Features in Detail

### Responsive Design

- Works seamlessly on desktop, tablet, and mobile devices
- Adaptive grid layout for movie cards
- Touch-friendly interface elements

### User Experience

- Loading animations and smooth transitions
- Clear visual feedback for user interactions
- Intuitive genre selection interface

### Performance

- Efficient TF-IDF vectorization
- Optimized similarity calculations
- Fast page loading and response times

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py`:

   ```python
   app.run(debug=True, port=5001)
   ```

2. **Missing dependencies**: Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

3. **Model files not generating**: Check file permissions and ensure you have write access to the directory.

## Future Enhancements

- [ ] User authentication and personalized recommendations
- [ ] Movie ratings and reviews integration
- [ ] Advanced filtering options (year, rating, etc.)
- [ ] Movie poster images and detailed information
- [ ] Collaborative filtering algorithms
- [ ] Real-time recommendation updates

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the movie recommendation system.

## License

This project is open source and available under the MIT License.

---

**Built with ❤️ using Flask and Machine Learning**
