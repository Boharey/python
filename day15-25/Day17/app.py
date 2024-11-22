from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)



# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Greet route with dynamic parameter
@app.route('/greet')
def greet():
    name = request.args.get('name')
    age = request.args.get('age')
    return f"Hello, {name} happy {age}'th birthday!"

# About page route
@app.route('/about')
def about():
    return "This is the About Page"

# Search page with query parameter
@app.route('/search')
def search():
    query = request.args.get('query', '')
    return render_template('search_results.html', query=query)

# Product page with dynamic parameters
@app.route('/product/<category>/<product_id>')
def product(category, product_id):
    return f"Product {product_id} in category {category}"

# Custom error page (404)
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Static file route
@app.route('/static_demo')
def static_demo():
    return render_template('home.html')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
