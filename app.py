from flask import Flask, request, render_template, jsonify
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Expanded dataset of books with genres
data = {
    'book_id': [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
        11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    ],
    'title': [
        'The Great Gatsby', 'Moby Dick', 'War and Peace', '1984',
        'Pride and Prejudice', 'The Catcher in the Rye', 'To Kill a Mockingbird',
        'The Hobbit', 'Harry Potter and the Philosopher\'s Stone', 'The Lord of the Rings',
        'The Girl on the Train', 'Gone Girl', 'The Alchemist', 'Brave New World', 'Dune',
        'The Silent Patient', 'The Da Vinci Code', 'The Martian', 'The Hitchhiker\'s Guide to the Galaxy', 'It'
    ],
    'author': [
        'F. Scott Fitzgerald', 'Herman Melville', 'Leo Tolstoy', 'George Orwell',
        'Jane Austen', 'J.D. Salinger', 'Harper Lee', 'J.R.R. Tolkien',
        'J.K. Rowling', 'J.R.R. Tolkien', 'Paula Hawkins', 'Gillian Flynn',
        'Paulo Coelho', 'Aldous Huxley', 'Frank Herbert', 'Alex Michaelides',
        'Dan Brown', 'Andy Weir', 'Douglas Adams', 'Stephen King'
    ],
    'genre': [
        'Classics', 'Classics', 'Historical Fiction', 'Dystopian',
        'Romance', 'Classics', 'Southern Gothic', 'Fantasy',
        'Fantasy', 'Fantasy', 'Thriller', 'Mystery',
        'Adventure', 'Dystopian', 'Science Fiction', 'Psychological Thriller',
        'Mystery', 'Science Fiction', 'Science Fiction', 'Horror'
    ],
    'description': [
        'A novel set in the Jazz Age, portraying the mysterious millionaire Jay Gatsby and his obsession with Daisy Buchanan.',
        'The narrative of a sailor named Ishmael and the obsessive quest of Captain Ahab for the white whale, Moby Dick.',
        'A detailed depiction of the French invasion of Russia and the impact on Tsarist society, focusing on five aristocratic families.',
        'A dystopian novel set in a totalitarian future society ruled by Big Brother.',
        'A romantic novel that deals with issues of marriage, morality, and the British class structure in the 18th century.',
        'A rebellious teenage boy narrates his experiences at a boarding school and his disdain for societal norms.',
        'A story of racial injustice in the Deep South, as seen through the eyes of a young girl, Scout Finch.',
        'The epic adventure of Bilbo Baggins, a hobbit, on a quest to win a share of treasure guarded by a dragon.',
        'The first book in the Harry Potter series, chronicling Harry\'s first year at Hogwarts School of Witchcraft and Wizardry.',
        'An epic fantasy trilogy set in Middle-earth, following the quest to destroy the One Ring.',
        'A psychological thriller about a woman who becomes involved in a missing persons investigation.',
        'A thriller about a married couple and the secrets they keep from each other.',
        'A fable about following your dreams, following a shepherd named Santiago.',
        'A dystopian novel exploring a future society where humans are controlled by a drug called soma.',
        'A science fiction novel set in a desert planet, where the protagonist becomes embroiled in a power struggle.',
        'A psychological thriller where a woman stops speaking after committing a violent act.',
        'A mystery involving a symbologist and a secret society.',
        'A story about an astronaut stranded on Mars and his struggle to survive.',
        'A humorous science fiction series about the adventures of an unwitting human.',
        'A horror novel about a group of children facing a malevolent entity.'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Function to recommend books based on genre
def recommend_books_by_genre(genre):
    # Filter books by the given genre
    filtered_books = df[df['genre'].str.lower() == genre.lower()]
    return filtered_books

# Flask Routes
@app.route('/')
def index():
    # Pass an empty DataFrame for recommendations on the initial load
    recommendations = pd.DataFrame(columns=df.columns)  # Ensure columns match
    return render_template('index.html', recommendations=recommendations)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Traditional form submit (non-JS fallback)
    genre = request.form.get('genre', '').strip()
    if not genre:
        recommendations = pd.DataFrame(columns=df.columns)
    else:
        recommendations = recommend_books_by_genre(genre)
    return render_template('index.html', genre=genre, recommendations=recommendations)


@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    """Return JSON recommendations for the provided genre.

    Accepts JSON body {"genre": "..."} or form data. Responds with:
    {"status": "ok", "recommendations": [{title,author,description}, ...]}
    """
    try:
        data = request.get_json(silent=True) or request.form or {}
        genre = (data.get('genre') or '').strip()
        if not genre:
            return jsonify({'status': 'error', 'message': 'Missing genre'}), 400

        recs_df = recommend_books_by_genre(genre)
        recs = recs_df[['title', 'author', 'description']].to_dict(orient='records')
        return jsonify({'status': 'ok', 'recommendations': recs}), 200
    except Exception as exc:
        return jsonify({'status': 'error', 'message': str(exc)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
