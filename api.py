from flask import Flask,jsonify,request
from testing import getprediction
app=Flask(__name__)
@app.route("/predictdigit",methods=["POST"])
def predict():
    image=request.files.get("digit")
    predictions=getprediction(image)
    return jsonify({
        "prediction":predictions
    }),200
if __name__=="__main__":
    app.run(debug=True)