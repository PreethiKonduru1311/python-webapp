from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# Route for handling the login form submission
@app.route('/login', methods=['POST'])
def login():
    # Get the name from the form
    user_name = request.form['nm']

    # You can perform any logic here, such as authentication or processing the name
    # For demonstration, let's just return a welcome message
    return f"""
    <div style='display: flex; justify-content: center; align-items: center; height: 100vh;'>
        <p style='font-size: 70px; font-weight:bold; color:red;'>
            Welcome, {user_name}! This is a web application.
        </p>
    </div>
    """

# Optionally, a home route to display the form directly from Flask
@app.route('/')
def home():
    return '''
    <html>
   <head>
      <style>
         p {
            font-size: 40px;
            color: blue;
         }
         input[type="text"] {
            font-size: 30px;
            color: green;
         }
         input[type="submit"] {
            font-size: 20px;
            color: white;
            background-color: blue;
         }
      </style>
   </head>
   <body>      
      <form action="/login" method="post">
         <p>Enter Name:</p>
         <p><input type="text" name="nm" /></p>
         <p><input type="submit" value="submit" /></p>
      </form>      
   </body>
</html>

    '''

if __name__ == "__main__":
    app.run(debug=True)