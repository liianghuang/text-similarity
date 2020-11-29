from app import app
from app import cosine_similiar, word_vector
from flask import request, jsonify

@app.route('/get_sim/<option>', methods=['POST'])
def update(option='cosine_similiarity'):
    data = request.get_json()

    if option == 'cosine_similiarity':
        s = cosine_similiar.Similiarity()
        s.build_count(data.get("first"), data.get("second"))
        return jsonify({"similiarity":s.cosine(), "method":option})

    if option == 'word2vec':
        path = "/Users/huangliiang/git/text-similarity/data/enwiki_20180420_100d.pkl"
        s = word_vector.WordVec(path)
        score = s.get_similiarity(data.get("first"), data.get("second"))
        return jsonify({"similiarity":score, "method":option})