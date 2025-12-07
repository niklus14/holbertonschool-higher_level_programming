from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    with open('products.json') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # CSV-dən oxunan qiymətləri float-a çeviririk
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
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
