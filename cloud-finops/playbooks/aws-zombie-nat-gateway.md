---
name: aws-zombie-nat-gateway
scope: aws
service: AWS NAT Gateway
waste_category: idle
confidence: obvious
---

# AWS Zombie NAT Gateway

## Problem

An AWS NAT Gateway is billed at roughly $0.045/hr per gateway plus
$0.045/GB of data processed (rate varies slightly by region). The hourly
charge alone is about $32/month per gateway, accrued whether traffic flows
or not. A NAT Gateway processing near-zero data still pays the full hourly.
Multiply across accounts, AZs, and forgotten migration leftovers and the
waste compounds quickly.

## Symptoms

- CloudWatch `BytesOutToSource` + `BytesOutToDestination` < 5 GB / month
- Private subnet has few or no running workloads
- The NAT was created during a migration project that has ended months ago
- An account has multiple NAT Gateways but only one or two AZs see real
  egress
- The owning team / cost-centre tag is empty or stale

## Detection

```sql
-- Athena over CUR 2.0: NAT Gateway hours vs data processed last full month
SELECT
  line_item_resource_id           AS nat_id,
  line_item_availability_zone     AS az,
  SUM(CASE WHEN line_item_usage_type LIKE '%NatGateway-Hours' THEN line_item_usage_amount END) AS hours,
  SUM(CASE WHEN line_item_usage_type LIKE '%NatGateway-Bytes' THEN line_item_usage_amount END) / 1024 / 1024 / 1024 AS gb_processed,
  SUM(line_item_unblended_cost)   AS cost_month
FROM cur2
WHERE line_item_usage_start_date >= date_trunc('month', current_date - interval '1' month)
  AND line_item_usage_start_date <  date_trunc('month', current_date)
  AND product_servicecode = 'AmazonEC2'
  AND line_item_usage_type LIKE '%NatGateway%'
GROUP BY 1, 2
HAVING SUM(CASE WHEN line_item_usage_type LIKE '%NatGateway-Bytes' THEN line_item_usage_amount END) / 1024 / 1024 / 1024 < 5
ORDER BY cost_month DESC;
```

For real-time validation, the canonical CloudWatch metrics are
`NATGateway/BytesOutToSource` and `NATGateway/BytesOutToDestination` at
1-minute granularity.

## Fix

1. Confirm the gateway has < 5 GB / month over a 60-day window (one month
   can be misleading - some workloads run quarterly).
2. Identify the route table(s) pointing at the gateway. If no private
   subnet routes to it, deletion is safe.
3. Delete the NAT Gateway. Release the associated Elastic IP if no other
   resource needs it (otherwise it accrues its own $3.60/month idle charge).
4. If a residual workload still needs occasional internet egress, evaluate
   whether **VPC Endpoints** (S3, DynamoDB, common AWS services) can
   replace the NAT entirely - VPC Endpoints have no hourly charge.

## Anti-pattern

- Deleting a NAT Gateway during a migration cutover window without
  confirming the new path. Lambda warmups, cron jobs, and external
  webhooks fail silently and only surface in operational alerts hours
  later.
- Replacing a per-AZ NAT Gateway with a single cross-AZ NAT to "save
  money" - cross-AZ data transfer ($0.01-0.02/GB each direction) often
  outweighs the saved NAT hours, AND introduces a single-AZ failure mode.

## See also

- `references/finops-aws.md` - AWS billing mechanics, CUR / FOCUS export
  setup
- `playbooks/aws-cross-az-egress.md` - the related cross-AZ chatterbox
  pattern
- `references/finops-waste-detection-playbooks.md` - the seven-category
  taxonomy this pattern fits ("idle")
