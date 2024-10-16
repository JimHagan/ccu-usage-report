# If the configured since for the report is blank it will use this.
DEFAULT_SINCE_CLAUSE = 'SINCE 7 DAYS AGO'


QUERY_DEFS = [

{
    "name":"top_capabilities",
    "NRQL": "FROM NrConsumption SELECT sum(consumption) AS CCU FACET dimension_productCapability",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_dashboards",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU WHERE dimension_productCapability = 'Dashboards' and dimension_dashboardId IS NOT NULL FACET dimension_dashboardId, dimension_email, dimension_productCapability",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_alerts",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU WHERE dimension_productCapability = 'Alert Conditions' FACET dimension_conditionId, dimension_productCapability",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_event_types_dashboards",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU WHERE dimension_productCapability = 'Dashboards' and dimension_dashboardId IS NOT NULL FACET dimension_eventTypes,dimension_dashboardId",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_event_types_all_caps",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU FACET dimension_eventTypes",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_users_by_cap",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU where dimension_email is not NULL FACET dimension_email, dimension_productCapability",
    "limit": 10,
    "since": "SINCE 1 day ago"
},
{
    "name":"top_users_all_caps",
    "NRQL": "FROM NrComputeUsage SELECT sum(usage) AS CCU where dimension_email is not NULL FACET dimension_email",
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