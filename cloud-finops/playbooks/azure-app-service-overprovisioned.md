---
name: azure-app-service-overprovisioned
scope: azure
service: Azure App Service
waste_category: overprovisioned
confidence: likely
---

# Azure App Service Plan Overprovisioned

## Problem

Azure App Service plans are billed by SKU (P1v3, P2v3, etc.) and instance
count, regardless of how many web apps actually run on them. Teams
default to **Premium v3** plans for production apps and never revisit -
even when the app handles low traffic that **Standard** or **Basic**
would serve fine. The cost gap is meaningful: a P1v3 instance is ~$70-90
/month vs ~$73/month for S1, but the auto-scale pattern often runs P1v3
at 4 instances when 2 would suffice.

## Symptoms

- App Service plan CPU < 25% p95 over 30 days
- Memory utilisation < 50% sustained
- Plan is on Premium v3 SKU but the apps deployed have no requirement
  for Premium-only features (deployment slots, VNet integration with
  private endpoints, autoscale on schedule)
- Plan instance count was set during a one-time event (Black Friday,
  product launch) and never scaled back down

## Detection

```kusto
// Azure Resource Graph - App Service plans by SKU and capacity
resources
| where type =~ "microsoft.web/serverfarms"
| extend sku_tier  = tostring(sku.tier)
| extend sku_size  = tostring(sku.size)
| extend capacity  = toint(sku.capacity)
| project subscriptionId, resourceGroup, name, sku_tier, sku_size, capacity, kind
| order by sku_tier desc
```

For utilisation:

```kusto
// CPU + Memory p95 from Azure Monitor over 30 days
AzureMetrics
| where ResourceProvider == "MICROSOFT.WEB"
  and ResourceType == "SERVERFARMS"
  and TimeGenerated > ago(30d)
  and MetricName in ("CpuPercentage", "MemoryPercentage")
| summarize p95 = percentile(Average, 95) by Resource, MetricName
| evaluate pivot(MetricName, max(p95))
| where CpuPercentage < 25 or MemoryPercentage < 50
| order by CpuPercentage asc
```

## Fix

1. **Right-size SKU first** (P1v3 -> S1 saves ~$60/month/instance and
   most apps don't need the Premium-only features).
2. **Reduce instance count to match observed p95 + safety margin**. Use
   **scheduled autoscale** to keep production at 2 instances during
   peak hours and 1 off-hours rather than a flat 4.
3. **Consolidate low-traffic apps** onto a single shared plan. Each App
   Service plan you eliminate saves a flat hourly. Test isolation
   carefully if apps have different security boundaries.
4. **Move dev / test environments to Basic or Free tier**. The cost
   delta vs production is meaningful and dev/test rarely need
   Premium-only features.

## Anti-pattern

- Resizing a Premium v3 plan to Basic on the same instances - some
  Premium-only features (Always On default, deployment slots, custom
  domains with SSL on every slot) silently disable. Verify the app's
  actual feature usage first.
- Aggressive consolidation onto a shared plan in production. Plan-level
  scaling boundaries are real - one badly-behaving app can starve the
  others. Reserve consolidation for dev / test / low-stakes prod.

## See also

- `references/finops-azure.md` - Azure compute rightsizing methodology,
  App Service vs AKS vs Container Apps trade-offs
- `references/finops-waste-detection-playbooks.md` - "overprovisioned"
  category rubric
