from flask import Flask, render_template, request
import redis

app = Flask(__name__)
cache = redis.Redis(host="my_db", port=6379)

@app.route('/', methods=["GET"])
def get_data():
    return "Avg: " + str(float(cache.get("avg")))

@app.route('/', methods=['POST'])
def calc_chars():
    if request.method == 'POST':
        form_data = request.form
        dictionary = dict(list(form_data.items()))
        longest_word = sorted(dictionary["Length"].split(" "), key=lambda x: len(x), reverse=True)[0]
        len_word = str(len(longest_word))

        return len_word


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')