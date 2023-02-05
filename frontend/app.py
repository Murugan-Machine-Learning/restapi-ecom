from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/store")
def store():
    return render_template("store.html")

@app.route("/product-detail")
def productDetail():
    return render_template("product-detail.html")

@app.route("/products")
def products():
    products = [
        {"id": 1, "name": "Product 1", "price": 10.99},
        {"id": 2, "name": "Product 2", "price": 20.99},
        {"id": 3, "name": "Product 3", "price": 30.99}
    ]
    return render_template("products.html", products=products)

@app.route("/cart", methods=["GET", "POST"])
def cart():
    if request.method == "POST":
        product_id = request.form["product_id"]
        # add product to cart
        # ...
    # display the contents of the cart
    # ...
    return render_template("cart.html")

if __name__ == "__main__":
    app.run()
