import os
import csv
import sys
import report_config as cfg
from python_graphql_client import GraphqlClient


NEWRELIC_API_ENDPOINT = "https://api.newrelic.com/graphql"
GRAPHQL_NRQL_TEMPLATE = """
                {{
                actor {{
                    account(id: {0}) {{
                    nrql(query: "{1}") {{
                        results
                    }}
                    }}
                }}
                }}
"""


def execute_nrql(api_key, account_id, nrql_query):
    headers = {}
    headers['Api-Key'] = api_key
    headers['Content-Type'] = 'application/json'
    client = GraphqlClient(endpoint=NEWRELIC_API_ENDPOINT)
    client.headers=headers
   
    query = GRAPHQL_NRQL_TEMPLATE.format(account_id, nrql_query)


    response = client.execute(query=query)
    return response['data']['actor']['account']['nrql']['results']




def run_all_reports(report_config, api_key, account_id):
    for rep in report_config:
        query = "{} {} LIMIT {}".format(rep["NRQL"], rep["since"] or cfg.DEFAULT_SINCE_CLAUSE, rep["limit"])
        print("##########{}".format(rep['name']))
        print("##########{}".format(query))
    
        records = execute_nrql(api_key , account_id, query)
        for record in records:
            print(record)





def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Must pass API key and account id in that order.")
    else:
        key = args[0]
        account_id = args[1]
        run_all_reports(cfg.QUERY_DEFS, key, account_id)

if __name__ == "__main__":
    main()

        