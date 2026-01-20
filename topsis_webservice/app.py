from flask import Flask, render_template, request
import os
import re
import subprocess
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    table = None

    if request.method == "POST":
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]  # validated but not used

        # Email validation (as required in assignment)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            message = "Invalid email format"
            return render_template("index.html", message=message)

        input_path = os.path.join(UPLOAD_FOLDER, "input.csv")
        output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

        file.save(input_path)

        try:
            result = subprocess.run(
                ["python", "-m", "topsis", input_path, weights, impacts, output_path],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                raise Exception(result.stderr)

            # Read result and convert to HTML table
            df = pd.read_csv(output_path)
            table = df.to_html(classes="result-table", index=False)

            message = "TOPSIS result generated successfully."

        except Exception as e:
            message = f"Error: {e}"

    return render_template("index.html", message=message, table=table)

if __name__ == "__main__":
    app.run(debug=True)
