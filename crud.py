def create_item(db, item):
    cursor = db.cursor()
    query = "INSERT INTO items (name, description) VALUES (%s, %s)"
    cursor.execute(query, (item.name, item.description))
    db.commit()
    return {"message": "Item created successfully"}

def get_items(db):
    cursor = db.cursor()
    query = "SELECT * FROM items"
    cursor.execute(query)
    result = cursor.fetchall()
    return [{"name": row[0], "description": row[1]} for row in result]

