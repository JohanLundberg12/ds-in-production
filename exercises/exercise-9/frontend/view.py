from flask import Flask, render_template, request
import requests
import redis

app = Flask(__name__)
cache = redis.Redis(host="my_db", port=6379)
cache.set('avg', 0)

# @app.route serves to direct the request to a mapped URL
# / represents the homepage.
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["POST"])
def data():
    if request.method == "POST":
        form_data = request.form
        r1 = requests.post(url='http://backend_y:5000', data=form_data)
        r2 = requests.post(url='http://backend_z:5000', data=form_data)
        avg = str((int(r1.text) + int(r2.text)) / 2)


        current_avg = float(cache.get("avg"))
        cache.set("avg", (current_avg+float(avg)) / 2)

        return avg

        #dictionary = dict({'Length': np.mean(int(r1.text) + int(r2.text))})
        #return render_template('data.html', form_data=dictionary)
        


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')