from flask import Flask, request, make_response, render_template, redirect, url_for, Response, send_from_directory, session
import cv2
import pandas as pd
import os
import uuid

app = Flask(__name__, template_folder="templates")
app.secret_key = '1234'

@app.route("/")
def index():
    

    return render_template("index.html", message="Index")


@app.route("/s")
def s():
    session['name'] = 'Saad'
    session['pass'] = '1234'
    return render_template("index.html", message="Sessionset")

@app.route('/gets')
def gets():
    try:
        name = session['name']
        passw = session['pass']
    except:
        
        return render_template('index.html', message='Error accessing data')    

    
    return render_template('index.html', message=f'Name: {name}, Password: {passw}')

# @app.route('/form', methods=['GET','POST'])
# def form():
#     if request.method == 'GET':
#         return render_template("form.html")
#     elif request.method == 'POST':
#         formData = request.form;

#         if 'username' not in formData.keys() or 'password' not in formData.keys():
#             res =  make_response()    
#             res.status_code = 401
#             return res
        
#         username = formData.get('username')
#         password = formData.get('password')

#         if username == 'saad' and password == '1234':
#             return 'success'
#         else:
#             return 'fail'        


# @app.route("/pfpUpload", methods=['POST'])
# def pfpUpload():
#     pfp = request.files["pfp"]

#     if pfp.content_type.startswith("image/"):
#         pfpPath = f"./{pfp.filename}"

#         pfp.save(pfpPath)

#         im = cv2.imread(pfpPath)
#         cv2.imshow('pfp', im)

#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

#         return "success"
    
#     return "fail"

# @app.route('/tocsv', methods=["POST"])
# def tocsv():

#     file = request.files["excel"]

#     df = pd.read_excel(file)

#     csv = df.to_csv()

#     res = Response(
#         csv,
#         mimetype='text/csv',
#         headers={
#             'Content-Disposition': 'attachment; filename=result.csv'
#         }
#     )

#     return res

# @app.route("/tocsv2", methods=['POST'])
# def tocsv2():
#     file = request.files["excel"]

#     if not file:
#         return "fail"
    
#     df = pd.read_excel(file)

#     if not os.path.exists('downloads'):
#         os.makedirs('downloads')

#     filename = f"{uuid.uuid4()}.csv" 

#     df.to_csv(os.path.join('downloads', filename))
    
#     return render_template("download.html", filename=filename)


# @app.route('/download/<filename>')
# def download(filename):
#     print(os.path.exists(f'downloads/{filename}'))
#     return send_from_directory('downloads', filename, download_name='csvfile.csv')



# @app.route("/filter")
# def filters():
#     text = "hello world"

#     return render_template("filters.html", text=text)

# @app.template_filter('custom')
# def reverseString(s):
#     return s[::-1]

# @app.template_filter('alt')
# def alt(s):
#     return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

# @app.route("/redirect")
# def redirectUrl():
#     return redirect(url_for('filters'))

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