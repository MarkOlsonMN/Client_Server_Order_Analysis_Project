from flask import Flask, request, jsonify
import sqlite3
import random
from datetime import datetime

app = Flask(__name__)

# Connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect('orders.db')
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    conn.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        items TEXT,
        timestamp TEXT,
        status TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Endpoint to receive orders
@app.route('/api/orders', methods=['POST'])
def receive_order():
    order_data = request.json
    conn = get_db_connection()
    conn.execute('''
    INSERT INTO orders (customer_id, items, timestamp, status)
    VALUES (?, ?, ?, ?)''',
    (order_data['customerId'], str(order_data['items']), order_data['timestamp'], 'Pending'))
    conn.commit()
    order_id = conn.execute('SELECT last_insert_rowid()').fetchone()[0]
    conn.close()
    
    return jsonify({'orderId': order_id, 'status': 'Pending'}), 201

# Process orders (simulated background processing)
def process_orders():
    conn = get_db_connection()
    orders = conn.execute('SELECT * FROM orders WHERE status = "Pending"').fetchall()
    for order in orders:
        new_status = random.choice(['Processed', 'Failed', 'In Progress'])
        conn.execute('UPDATE orders SET status = ? WHERE id = ?', (new_status, order['id']))
    conn.commit()
    conn.close()

# Endpoint to get order status
@app.route('/api/orders/<int:order_id>/status', methods=['GET'])
def get_order_status(order_id):
    conn = get_db_connection()
    order = conn.execute('SELECT * FROM orders WHERE id = ?', (order_id,)).fetchone()
    conn.close()
    if order:
        return jsonify({'orderId': order_id, 'status': order['status']})
    return jsonify({'error': 'Order not found'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
  
