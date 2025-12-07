from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        products = []
        for r in rows:
            products.append({
                'id': r[0],
                'name': r[1],
                'category': r[2],
                'price': r[3]
            })
        return products
    except sqlite3.Error as e:
        print("Database error:", e)
        return None
    finally:
        conn.close()

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
        if data is None:
            return render_template('product_display.html', error="Database error", products=[])
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    if product_id:
        filtered = [p for p in data if p['id'] == product_id]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=[])
        data = filtered

    return render_template('product_display.html', products=data, error=None)

if __name__ == "__main__":
    app.run(debug=True)
