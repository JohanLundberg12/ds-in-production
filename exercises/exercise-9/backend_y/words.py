from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def calc_words():
    if request.method == 'POST':
        form_data = request.form
        dictionary = dict(list(form_data.items()))
        n_words = str(len(dictionary["Length"].split(" ")))

        return n_words


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')