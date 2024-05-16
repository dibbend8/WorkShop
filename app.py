from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
data = {
    1: {"title": "First Post", "body": "This is the first post", "userId": 1},
    2: {"title": "Second Post", "body": "This is the second post", "userId": 2},
}

# GET all posts
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(data)

# GET a single post by ID
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = data.get(post_id)
    if post:
        return jsonify(post)
    else:
        return jsonify({"error": "Post not found"}), 404

# CREATE a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_id = max(data.keys()) + 1 if data else 1
    post = request.json
    data[new_id] = post
    return jsonify({"id": new_id, **post}), 201

# UPDATE a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    if post_id in data:
        post = request.json
        data[post_id] = post
        return jsonify(post)
    else:
        return jsonify({"error": "Post not found"}), 404

# DELETE a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    if post_id in data:
        del data[post_id]
        return jsonify({"message": "Post deleted"}), 200
    else:
        return jsonify({"error": "Post not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
