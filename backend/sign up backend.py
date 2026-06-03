# SIGN UP (bonus - aapko zaroorat padegi)
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    username = data.get('username', '').strip()
    email    = data.get('email', '').strip()
    password = data.get('password', '').strip()

    if not username or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Password must be at least 6 characters'}), 400

    hashed_password = generate_password_hash(password)

    db = get_db()
    try:
        db.execute(
            'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
            (username, email, hashed_password)
        )
        db.commit()
        user_id = db.execute('SELECT last_insert_rowid()').fetchone()[0]
        db.close()
    except sqlite3.IntegrityError:
        db.close()
        return jsonify({'error': 'Username or email already exists'}), 409

    token = create_token(user_id)

    return jsonify({
        'message': 'Account created successfully',
        'token': token,
        'user': {
            'id': user_id,
            'username': username,
            'email': email
        }
    }), 201


# GET CURRENT USER (protected route example)
@app.route('/me', methods=['GET'])
def me():
    user = get_current_user()
    if not user:
        return jsonify({'error': 'Unauthorized'}), 401

    return jsonify({
        'id': user['id'],
        'username': user['username'],
        'email': user['email'],
        'created_at': user['created_at']
    }), 200


# SIGN OUT (client side token delete hota hai, but server par bhi route rakh sakte hain)
@app.route('/signout', methods=['POST'])
def signout():
    return jsonify({'message': 'Signed out successfully'}), 200


# ==========================
# RUN
# ==========================

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)