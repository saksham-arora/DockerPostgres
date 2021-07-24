select dim_vendors.id, dim_vendors.type,sum(fact_orders.amt) as total_amt_non_successful
from
fact_orders
left join
dim_vendors
on
fact_orders.vendor_id = dim_vendors.id
where
fact_orders.status = '2'  or fact_orders.status='3'
GROUP BY
dim_vendors.id, dim_vendors.type
ORDER BY
total_amt_non_successful;

