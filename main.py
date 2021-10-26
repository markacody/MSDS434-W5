"""
Before you run, login to gcloud: gcloud auth login
Refer to the quickstart Automat App Engine deployments with Cloud Build: https://cloud.google.com/source-repositories/docs/quickstart-triggering-builds-with-source-repositories
"""
from flask import Flask
from google.cloud import bigquery

app = Flask(__name__)


@app.route("/")
def hello_world():
    greeting = '{"greeting":"hello world"}'
    return greeting


# Instantiate a bigquery client.
query_client = bigquery.Client()

# Describe the query.
query = """
      SELECT
      unique_session_id,
      predicted_will_buy_on_return_visit_probs
      FROM `msds434-w5.ecommerce.Predictions`
      LIMIT 100
    """

# Ask for a query job
query_job = query_client.query(query)
print("The prediction:")
print(type(query_job))
print(query_job)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
