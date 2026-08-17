# This is Day 37 project : Personal Blog Website

from flask import Flask, render_template, request

app = Flask(__name__)

posts = [
    {"id": 1, "title": "Introduction to Flask", "content": "Learn Flask basics.", "author": "Alice"},
    {"id": 2, "title": "Advanced Flask Routing", "content": "Understand dynamic routes", "author": "Bob"},
    {"id": 3, "title": "Python Basics", "content": "Learn the fundamentals of Python.", "author": "Charlie"},
    {"id": 4, "title": "HTML and CSS", "content": "Learn how to build web pages.", "author": "David"},
    {"id": 5, "title": "Flask Templates", "content": "Learn Jinja2 templates in Flask.", "author": "Alice"},
    {"id": 6, "title": "Python Functions", "content": "Understand functions in Python.", "author": "Bob"},
    {"id": 7, "title": "Flask Forms", "content": "Learn how to handle forms in Flask.", "author": "Charlie"},
    {"id": 8, "title": "Web Development", "content": "Introduction to web development.", "author": "David"},
    {"id": 9, "title": "Flask Error Handling", "content": "Learn how to handle errors in Flask.", "author": "Alice"},
    {"id": 10, "title": "Python File Handling", "content": "Learn how to work with files in Python.", "author": "Bob"},
    {"id": 11, "title": "Flask Routing", "content": "Learn about Flask routes.", "author": "Charlie"},
    {"id": 12, "title": "Python Lists", "content": "Learn how to use lists in Python.", "author": "David"}
]

@app.route('/')
def home():
    search = request.args.get('search', '').strip()
    if search:
        filtered_posts = [post for post in posts
                          if search.lower() in post["title"].lower()
                          or search.lower() in post["content"].lower()
                          or search.lower() in post["author"].lower()]
    else:
        filtered_posts = posts
        
    per_page = 5
    page = request.args.get('page', 1, type=int)
    total_posts = len(filtered_posts)
    total_pages = (total_posts + per_page - 1)
    
    if page < 1:
        page = 1
        
    if total_pages > 0 and page > total_pages:
        page = total_pages
        
    start = (page - 1) * per_page
    end = start + per_page
    paginated_posts = filtered_posts[start:end]
    
    return render_template('index.html', posts=paginated_posts, search=search, page=page, total_pages=total_pages)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((post for post in posts if post["id"] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    return "<h1>Post Not Found</h1>", 404

@app.route('/about')
def about():
    return render_template('about_us.html')

if __name__ == "__main__":
    app.run(debug=True)
    
# Done