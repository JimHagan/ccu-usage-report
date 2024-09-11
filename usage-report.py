import os
import csv
import sys
from python_graphql_client import GraphqlClient



REPORT_CONFIGS = [

{
    "name":"top_capabilities",
    "NRQL": "FROM NrConsumption SELECT sum(consumption) AS CCU FACET dimension_productCapability",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_dashboards",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_dashboardId, dimension_email, dimension_productCapability WHERE dimension_productCapability = 'Dashboards' and dimension_dashboardId IS NOT NULL",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_event_types", 
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_eventTypes,dimension_dashboardId  WHERE dimension_productCapability = 'Dashboards' and dimension_dashboardId IS NOT NULL",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_users",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_email, dimension_productCapability where dimension_email is not NULL",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
#{
#    "name":"top_queries_by_avg_inspected_count",
#    "NRQL": "FROM NrdbQuery SELECT average(inspectedCount), average(durationMs), max(timeWindowMinutes), median(timeWindowMinutes) facet query, productCapability",
#    "limit": 10,
#    "since": "SINCE 7 days ago"
# },

]
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
        query = "{} {} LIMIT {}".format(rep["NRQL"], rep["since"], rep["limit"])
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
        run_all_reports(REPORT_CONFIGS, key, account_id)

if __name__ == "__main__":
    main()

        