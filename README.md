## CCU-USAGE-REPORT

This is a simple utility for extracting CCU status using New Relic's GraphQL API.   It uses a simple report configuration to allow yopu to change the reports that are run without code.  

TODO: Work on refining the output formatting into a series of CSVs.

*Usage*

`python python-usage-report NRAK-ALCCUM2N9**********  1987*****`


*Environment*

Setup a Python3 virtual environment using the provided `requirements.txt` file.


*The query config example is as follows*

```
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
]
```


*Output example*

```
###top_event_types
###FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_eventTypes,dimension_dashboardId  WHERE dimension_productCapability = 'Dashboards' and dimension_dashboardId IS NOT NULL SINCE 1 day ago LIMIT 10
{'facet': ['Log', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjQwODQ1Mzc'], 'CCU': 5.064011520778}
{'facet': ['LoadBalancerSample, MetricRaw', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjUwNzMyMTc'], 'CCU': 3.5665541507680008}
{'facet': ['ApiGatewaySample, MetricRaw', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjUwNzMyMTc'], 'CCU': 3.493817635658}
{'facet': ['Log', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjQzNzY0OTI'], 'CCU': 0.792981666806}
{'facet': ['MetricRaw', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjQxNDM3Mzg'], 'CCU': 0.434504487914}
{'facet': ['Transaction', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjUwNzMyMTc'], 'CCU': 0.33076536540600004}
{'facet': ['SyntheticCheck, Transaction', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjQzNjA5NzA'], 'CCU': 0.293354502154}
{'facet': ['ServiceLevelSnapshot, Transaction', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjQzNjA5NzA'], 'CCU': 0.29030299053}
{'facet': ['InfrastructureEvent, NetworkSample, ProcessSample, StorageSample, SystemSample, K8sClusterSample, K8sContainerSample, K8sControllerManagerSample, K8sCronjobSample, K8sDaemonsetSample, K8sDeploymentSample, K8sEndpointSample, K8sEtcdSample, K8sHpaSample, K8sJobSample, K8sNamespaceSample, K8sNodeSample, K8sPodSample, K8sReplicasetSample, K8sSchedulerSample, K8sServiceSample, K8sStatefulsetSample, K8sVolumeSample', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjY2NzA1NDA'], 'CCU': 0.242426020046}
{'facet': ['FinanceSample, Metric5MINUTES', 'MTYwNjg2MnxWSVp8REFTSEJPQVJEfGRhOjE5NzUxMzc'], 'CCU': 0.22064204842399998}
###top_users
###FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_email, dimension_productCapability where dimension_email is not NULL SINCE 1 day ago LIMIT 10
{'facet': ['demonewrelic@gmail.com', 'APM'], 'CCU': 40.380757671370006}
{'facet': ['wtang+demotron@newrelic.com', 'Network Monitoring'], 'CCU': 20.639478847302}
{'facet': ['mschlapfer+demotron@newrelic.com', 'Logs'], 'CCU': 17.410918088928}
{'facet': ['ehaxton+demotron@newrelic.com', 'APM'], 'CCU': 13.744371905076}
{'facet': ['ywakabayashi+demotron@newrelic.com', 'APM'], 'CCU': 11.898294793338005}
{'facet': ['sskilbred+demotron@newrelic.com', 'APM'], 'CCU': 11.443808626582003}
{'facet': ['ekucuk+demotron@newrelic.com', 'Mobile'], 'CCU': 7.35109492844}
{'facet': ['edmondwalsh+demotron@newrelic.com', 'APM'], 'CCU': 6.972365902222}
{'facet': ['demonewrelic@gmail.com', 'Dashboards'], 'CCU': 6.790709966782001}
{'facet': ['zfouzan+demotron@newrelic.com', 'Serverless'], 'CCU': 5.99479665582}
```
