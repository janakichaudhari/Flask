from asyncio import tasks
from flask import Flask,jsonify,request
app=Flask(__name__)

tasks=[
    {
        'Contact':"9987644456",
        'Name':u'Raju',
        'id': 1,
        'done':False
    },
    {
        'Contact':"9876543222",
        'Name':u'Rahul',
        'id': 2,
        'done':False
    }
]

@app.route("/add-data",methods=["POST"])
def addtask():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        },400)

    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['Name'],
        'description': request.json.get('Contact',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "status":"Success",
        "message":"successfully task added"
    })


@app.route("/get-data")
def gettask():
    return jsonify({
        "data":tasks
    })

if(__name__=="__main__"):
    app.run(debug=True)