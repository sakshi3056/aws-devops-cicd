from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS DevOps CI/CD</title>
        </head>
        <body>
            <h1>AWS DevOps CI/CD Pipeline</h1>
            <p>Application deployed successfully through Kubernetes!</p>
            <p>GitHub → Jenkins → Docker → Amazon ECR → Kubernetes</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "healthy"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)