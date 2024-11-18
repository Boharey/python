from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items: list[dict] = []

@app.route("/")
def home():
    return render_template("index.html", items=items)

@app.route('/add-item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':		
        name = request.form.get('name')  # Retrieve 'name' from the form
        if name:
            item = {'id': len(items) + 1, 'name': name}  # Create new item with unique ID
            items.append(item)
            return redirect(url_for('home'))  # Redirect to home page after adding item
    return render_template('add_item.html')

@app.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
def delete_item(item_id):
    item = next((it_em for it_em in items if it_em['id'] == item_id), None)
    if item:
        items.remove(item)  # Remove the item from the list

        # Reassign IDs to maintain order starting from 1
        for index, item in enumerate(items):
            item['id'] = index + 1  # Reassign the id starting from 1

    return redirect(url_for('home'))  # Redirect back to the home page


@app.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    item = next((i for i in items if i['id'] == item_id), None)
    if not item:
        return redirect(url_for('home'))  # Redirect to home if item is not found
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        if new_name:
            item['name'] = new_name  # Update item name
        return redirect(url_for('home'))  # Redirect to home after updating item
    
    return render_template('update_item.html', item=item)  # Render update form with existing item data

if __name__ == "__main__":
    app.run(debug=True)
