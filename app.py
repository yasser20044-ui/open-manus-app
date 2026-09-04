from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # For now, just print to console (next we'll save to database)
        print(f"\n--- New Contact Message ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"----------------------------\n")
        
        # Show success message
        return render_template("contact.html", success=True, user_name=name)
    
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
