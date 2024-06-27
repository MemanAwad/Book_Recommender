#mini project by raghad al zoughbi and meman awad
from flask import Flask, render_template, request

app = Flask(__name__)

#  book data organized by categories and interests
books = [
    {
        'id': 1,
        'title': 'It',
        'author': 'Stephen King',
        'category': 'films',
        'interests': ['Horror','Fantasy'],
        'cover_image': '/static/it.jpeg',
        'publication_date': '1986',
        'synopsis': 'A terrifying clown terrorizes the town of Derry, Maine.'
    },
    {
        'id': 2,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'category': 'films',
        'interests': ['Romance','Drama'],
        'cover_image': '/static/pride_and_prejudice.jpeg',
        'publication_date': '1813',
        'synopsis': 'A classic novel about the misunderstandings and romance between Elizabeth Bennet and Mr. Darcy.'
    },
    {
        'id': 3,
        'title': 'Watchmen',
        'author': 'Alan Moore',
        'category': 'films',
        'interests': ['Fantasy', 'wars'],
        'cover_image': '/static/watchmen.jpeg',
        'publication_date': '1986',
        'synopsis': 'A graphic novel exploring the psychological complexities of masked vigilantes.'
    },
    {
        'id': 4,
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'category': 'films',
        'interests': 'Fantasy',
        'cover_image': '/static/the_hobbit.webp',
        'publication_date': '1937',
        'synopsis': 'The adventures of Bilbo Baggins as he journeys with a group of dwarves to reclaim their homeland.'
    },
    {
        'id': 5,
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'category': 'films',
        'interests': ['Adventure'],
        'cover_image': '/static/moby_dick.jpeg',
        'publication_date': '1851',
        'synopsis': 'The voyage of the whaling ship Pequod, commanded by Captain Ahab.'
    },
    {
        'id': 6,
        'title': 'Dune',
        'author': 'Frank Herbert',
        'category': 'films',
        'interests': 'Science Fiction',
        'cover_image': '/static/dune.jpeg',
        'publication_date': '1965',
        'synopsis': 'A desert planet, political intrigue, and a messiah figure in a sprawling epic.'
    },
    {
        'id': 7,
        'title': 'Principia Mathematica',
        'author': 'Isaac Newton',
        'category': 'Academic books',
        'interests': 'Academic',
        'cover_image': '/static/principia_mathematica.jpeg',
        'publication_date': '1687',
        'synopsis': 'One of the most important works in the history of science, laying the groundwork for classical mechanics.'
    },
    {
        'id': 8,
        'title': 'Mastering the Art of French Cooking',
        'author': 'Julia Child',
        'category': 'Books',
        'interests': ['Cooking'],
        'cover_image': '/static/mastering_french_cooking.jpeg',
        'publication_date': '1961',
        'synopsis': 'A cookbook that brought French cuisine to American households with detailed instructions and recipes.'
    },
    {
        'id': 9,
        'title': 'Understanding Exposure',
        'author': 'Bryan Peterson',
        'category': 'Books',
        'interests': ['Photography'],
        'cover_image': '/static/understanding_exposure.jpeg',
        'publication_date': '1990',
        'synopsis': 'A guidebook for photographers on mastering the art of exposure and capturing great photos.'
    },
    {
        'id': 10,
        'title': 'The Art of War',
        'author': 'Sun Tzu',
        'category': 'Books',
        'interests': ['Wars'],
        'cover_image': '/static/art_of_war.jpeg',
        'publication_date': '5th century BC',
        'synopsis': 'Ancient Chinese military treatise attributed to Sun Tzu, offering strategies and tactics for warfare.'
    },
    {
        'id': 11,
        'title': 'The Innovators: How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution',
        'author': 'Walter Isaacson',
        'category': 'Books',
        'interests': ['Technologies'],
        'cover_image': '/static/the_innovators.jpeg',
        'publication_date': '2014',
        'synopsis': 'A narrative of the people who created the computer and the Internet.'
    },
    {
        'id': 12,
        'title': 'Freakonomics: A Rogue Economist Explores the Hidden Side of Everything',
        'author': 'Steven D. Levitt, Stephen J. Dubner',
        'category': 'Books',
        'interests': ['Economics'],
        'cover_image': '/static/freakonomics.jpeg',
        'publication_date': '2005',
        'synopsis': 'An exploration of economic theories and their application to everyday life.'
    },
    {
        'id': 13,
        'title': 'The Intelligent Investor',
        'author': 'Benjamin Graham',
        'category': 'Books',
        'interests': ['Finance'],
        'cover_image': '/static/intelligent_investor.jpeg',
        'publication_date': '1949',
        'synopsis': 'A classic investment book offering principles for value investing.'
    },
    {
        'id': 14,
        'title': '1984',
        'author': 'George Orwell',
        'category': 'Novel',
        'interests': ['Wars'],
        'cover_image': '/static/1984.jpeg',
        'publication_date': '1949',
        'synopsis': 'A dystopian novel about a totalitarian regime and thought control.'
    },
    {
        'id': 15,
        'title': 'Jane Eyre',
        'author': 'Charlotte Brontë',
        'category': 'Novel',
        'interests': ['Romance', 'Drama'],
        'cover_image': '/static/jane_eyre.jpeg',
        'publication_date': '1847',
        'synopsis': 'The story of a young orphan, Jane Eyre, who grows up in unfortunate circumstances.'
    },
    {
        'id': 16,
        'title': 'Sandman',
        'author': 'Neil Gaiman',
        'category': 'Novel',
        'interests': ['Fantasy', 'Horror', 'Comics'],
        'cover_image': '/static/sandman.jpeg',
        'publication_date': '1989',
        'synopsis': 'A graphic novel series that blends mythology and modern horror.'
    },
    {
        'id': 17,
        'title': 'A Game of Thrones',
        'author': 'George R.R. Martin',
        'category': 'films',
        'interests': ['Fantasy','wars'],
        'cover_image': '/static/a_game_of_thrones.jpeg',
        'publication_date': '1996',
        'synopsis': 'The first novel in the epic fantasy series A Song of Ice and Fire.'
    },
    {
        'id': 18,
        'title': 'Neuromancer',
        'author': 'William Gibson',
        'category': 'Novel',
        'interests': ['Technologies'],
        'cover_image': '/static/neuromancer.jpeg',
        'publication_date': '1984',
        'synopsis': 'A cyberpunk novel that explores the world of artificial intelligence and hacking.'
    },
    {
        'id': 19,
        'title': 'The Wealth of Nations',
        'author': 'Adam Smith',
        'category': 'Books',
        'interests': ['Economics'],
        'cover_image': '/static/wealth_of_nations.jpeg',
        'publication_date': '1776',
        'synopsis': 'An inquiry into the nature and causes of the wealth of nations, considered the first modern work of economics.'
    },
    {
        'id': 20,
        'title': 'Rich Dad Poor Dad',
        'author': 'Robert T. Kiyosaki',
        'category': 'Books',
        'interests': ['Finance'],
        'cover_image': '/static/rich_dad_poor_dad.jpeg',
        'publication_date': '1997',
        'synopsis': 'Personal finance book advocating the importance of financial education.'
    },
]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all_books')
def all_books():
    return render_template('all_books.html', books=books)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    category = request.form.get('category')
    interests = request.form.getlist('interests')  # Get multiple interests
    
    recommended_books = books
    
    if category:
        recommended_books = [book for book in recommended_books if category.lower() in book['category'].lower()]
    
    if interests:
        recommended_books = [book for book in recommended_books if any(interest.lower() in [i.lower() for i in book['interests']] for interest in interests)]
    
    return render_template('recommendations.html', books=recommended_books)


@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('book_details.html', book=book)
    else:
        return 'Book not found', 404

if __name__ == '__main__':
    app.run(debug=True)
