CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    items TEXT,
    timestamp TEXT,
    status TEXT
);
