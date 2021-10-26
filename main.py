"""
Before you run, login to gcloud: gcloud auth login
Refer to the quickstart Automat App Engine deployments with Cloud Build: https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories
"""
from flask import Flask
from flask import jsonify
from google.cloud import bigquery

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route("/")
@app.route("/home")
@app.route("/index")
@app.route("/welcome")
def home():
    # Instantiate a bigquery client.
    query_client = bigquery.Client()

    # Define the query.
    query = """
        SELECT
        unique_session_id,
        predicted_will_buy_on_return_visit_probs
        FROM `msds434-w5.ecommerce.Predictions`
        LIMIT 100
        """

    # Ask for a query job, convert to dataframe, and return json
    df = query_client.query(query).result().to_dataframe(create_bqstorage_client=True)
    results = df.head(10).to_json()
    return results


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
