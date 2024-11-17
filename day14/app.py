from flask import Flask, render_template, request, redirect, url_for # type: ignore
from flask import request, jsonify # type: ignore

app = Flask(__name__)

items: list[str] = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/display')
def display_items():
    return render_template('display.html', items=items)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':		
        name = request.form.get('name') #this 'name' is from back one name="name" <input type="text" id="name" name="name" required>
        if name:
            item = {'id': len(items) + 1, 'name': name}
            items.append(item)
    return render_template('add_item.html')


@app.route('/delete-item', methods=['GET', 'POST'])
def delete_item():
    if request.method == 'POST':
        item_id = int(request.form.get('id'))
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            items.remove(item)
    return render_template('delete_item.html')


@app.route('/update-item', methods=['GET', 'POST'])
def update_item():
    if request.method == 'POST':
        item_id = int(request.form.get('id'))
        new_name = request.form.get('name')
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            item['name'] = new_name
    return render_template('update_item.html')




# @app.route("/items",methods = ["POST"])


if __name__ == "__main__":
	app.run(debug= True)
