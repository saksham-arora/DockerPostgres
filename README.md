# DH_TakeHome
Assignment on Postgres and Docker.

1. Setup to be done using docker.
2. Pull postgres image from the hub.docker.
3. Use compose script to configue and start the container.
4. Use cmd ->  psql -h pg_tag -d test_db -U root -> to connect to DB
5. Run all the DDLs and DMLs.
6. Check the results.
7. For 3rd Solution, use querycsv.py module to run the query using python.
8. use cmd -> querycsv.py -i fact_orders.csv -i dim_vendors.csv -s solution3rd.sql -> to check the result
