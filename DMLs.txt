INSERT INTO dim_users(id,name,phone_no,added_at,deactivated_at,email_id,is_active) VALUES(1,'John',420298154,'2020-07-21 14:01:10-08',null,'john.doe@gmail.com',True);
INSERT INTO dim_users(id,name,phone_no,added_at,deactivated_at,email_id,is_active) VALUES(2,'Ross',420298189,'2020-05-20 15:02:10-08',null,'ross.geller@gmail.com',True);
INSERT INTO dim_users(id,name,phone_no,added_at,deactivated_at,email_id,is_active) VALUES(3,'Rachele',420900199,'2019-02-20 15:02:10-08',null,'rachele.green@gmail.com',false);
INSERT INTO dim_users(id,name,phone_no,added_at,deactivated_at,email_id,is_active) VALUES(4,'Ted',420902363,'2019-07-05 17:07:12-10',null,'ted.morris@gmail.com',True);
INSERT INTO dim_users(id,name,phone_no,added_at,deactivated_at,email_id,is_active) VALUES(5,'Barney',420902378,'2018-05-05 17:07:12-10','2018-09-05 17:07:12-10','barney_stinson@gmail.com',false);





INSERT INTO dim_vendors(id,type,added_at,removed_at,is_active,is_platform_online) VALUES(1001,2,'2017-12-01 17:07:12-10',null,true,true);
INSERT INTO dim_vendors(id,type,added_at,removed_at,is_active,is_platform_online) VALUES(1002,2,'2019-11-12 17:07:12-10',null,true,true);
INSERT INTO dim_vendors(id,type,added_at,removed_at,is_active,is_platform_online) VALUES(1003,1,'2019-01-04 17:07:12-10',null,false,true);






INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10001,0,50,'2020-01-04 17:07:12-10',null,null,null,1001,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10002,0,42,'2020-02-04 17:07:12-10',null,null,null,1001,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10003,-1,42,'2020-02-04 17:07:12-10',null,null,null,1003,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10004,0,35,'2020-02-04 17:10:12-10',null,null,null,1003,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10005,0,67,'2019-08-08 17:10:12-10',null,null,null,1003,4);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10006,0,89,'2019-01-01 17:10:12-10',null,null,null,1001,5);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10007,2,127,'2020-12-01 17:10:12-10',null,null,null,1002,2);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10008,0,132,'2020-12-01 17:11:12-10',null,null,null,1002,2);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10009,0,32,'2021-12-01 17:11:12-10',null,null,null,1001,1);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10010,0,12,'2021-12-02 17:11:12-10',null,null,null,1002,1);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10011,0,99,'2021-12-02 17:11:12-10',null,null,null,1003,4);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10012,0,78,'2021-01-07 17:11:12-10',null,null,null,1002,5);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10013,0,20,'2021-08-04 17:07:12-10',null,null,null,1001,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10014,0,87,'2021-02-04 17:07:12-10',null,null,null,1001,3);
INSERT INTO fact_orders(id,status,amt,placed_at,cancelled_at,returend_at,failed_at,vendor_id,user_id) VALUES(10015,0,25,'2021-02-06 17:07:12-10',null,null,null,1003,3);

