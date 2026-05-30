from flask import Flask, render_template, request

app = Flask(__name__)

# Stores current expression and result
expression = ""
result = ""


@app.route("/", methods=["GET", "POST"])
def home():

    global expression, result

    # Check if user clicked any button
    if request.method == "POST":

        button = request.form.get("button")

        if button:

            # Clear everything
            if button == "AC":

                expression = ""
                result = ""

            # Remove last character
            elif button == "⌫":

                expression = expression[:-1]

            # Toggle positive / negative sign
            elif button == "+/-":

                if expression.startswith("-"):
                    expression = expression[1:]
                else:
                    expression = "-" + expression

            # Calculate final result
            elif button == "=":

                try:
                    result = str(eval(expression))

                except:
                    result = "Error"

            # Add clicked button to expression
            else:

                expression += button

    # Send data to HTML page
    return render_template(
        "index.html",
        expression=expression,
        result=result
    )

# Run Flask application
if __name__ == "__main__":
    app.run(debug=True)