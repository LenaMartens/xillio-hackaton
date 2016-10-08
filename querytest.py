from bigquery import get_client
import time

#Script to get the data from the bigquery platform

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


# Given a page and amount, returns the github data for the Markov chain
def get_data(page, amount):

    offset = (page - 1) * amount
    # Submit an async query.
    job_id, _results = client.query('SELECT subject as commitMessage, REGEXP_EXTRACT(difference.new_path,r\'([a-zA-Z]*)\..*\') as fileName, REGEXP_EXTRACT(difference.new_path,r\'\.(.*)$\') as extension, ' +
    'author.email == committer.email as isCommitterAuthor, committer.time_sec as commitTime, committer.date as date, (committer.time_sec-author.time_sec) as timeDiff ' +
    'FROM [bigquery-public-data:github_repos.commits] LIMIT ' + str(amount) + ' OFFSET ' + str(offset))


    # Keep checking if the query is complete, when it is, break and return the data
    while True:
        print("entered while")
        # Poll for query completion.
        complete, row_count = client.check_job(job_id)

        # Retrieve the results.
        if complete:
            results = client.get_query_rows(job_id)
            break;
         # Added a short sleep, so we do not make too many requests
        time.sleep(0.2)

    return results
