from app import app
from app import cosine_similiar
from flask import request, jsonify

@app.route('/get_sim', methods=['POST'])
def update():
    data = request.get_json()
    s = cosine_similiar.Similiarity()
    s.build_count(data.get("first"), data.get("second"))
    return jsonify({"similiarity":s.cosine()})