from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    x = "Hello" 
    y = 4

    myList = [2,43,71,14,651]

    return render_template("index.html", str=x,num=y, l=myList)


# @app.route('/')
# def index():
#     return "Hello world"


# @app.route("/heading", methods=['GET','POST'])
# def heading():
#     if request.method == 'GET':
#         return "<h2>Hello world</h2>",200
#     elif request.method == 'POST':
#         return "<h1>Hello world</h1>",201

# @app.route("/greet/<name>") #parameters are always strings
# def greet(name):
#     return f"<h2>Hello {name}</h2>"

# @app.route("/args")
# def args():
#     if 'name' in request.args.keys():
#         print(request.args.get("name"))
#         print(request.args["name"])
#     return request.args

# @app.route("/res")
# def res():
#     response = make_response("<h1>Response</h1>")
#     response.status_code = 200
#     response.headers['content-type'] = 'text/html'

#     return response



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, port=5000)