from flask import Flask,render_template,jsonify
import g4f
import time

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/generate/<query>")
def generateResponse(query):
    print(query)
    
    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.Bing,

        messages=[{"role":"user","content":query}],
        stream=False,
    )

    print("Response: \n",response)
    return response  


if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')