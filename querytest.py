from bigquery import get_client
import time
#DRIES VERSION

# BigQuery project id as listed in the Google Developers Console.
project_id = 'rational-diode-145807'

# Service account email address as listed in the Google Developers Console.
service_account = 'querymachine@rational-diode-145807.iam.gserviceaccount.com'

# PKCS12 or PEM key provided by Google.
key = 'key.p12'
#notasecret

client = get_client(project_id, service_account=service_account,
                    private_key_file=key, readonly=True)

# JSON key provided by Google
json_key = 'key.json'

client = get_client(json_key_file=json_key, readonly=True)

# Submit an async query.
job_id, _results = client.query('SELECT commits.difference FROM [bigquery-public-data:github_repos.commits] GROUP BY encoding')

# Check if the query has finished running.
complete, row_count = client.check_job(job_id)

time.sleep(5)

# Retrieve the results.
results = client.get_query_rows(job_id)

print(results)