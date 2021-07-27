CREATE TABLE dim_users(
id INT PRIMARY KEY,
name TEXT NOT NULL UNIQUE,
phone_no BIGINT UNIQUE,
added_at timestamp NOT NULL,
deactivated_at timestamp,
email_id char(30) UNIQUE NOT NULL,
is_active boolean DEFAULT false
);

CREATE TABLE dim_vendors(
id INT PRIMARY KEY,
type smallint NOT NULL,
added_at timestamp NOT NULL,
removed_at timestamp,
is_active boolean DEFAULT false,
is_platform_online boolean DEFAULT false
);


CREATE TABLE fact_orders(
id INT PRIMARY KEY,
status smallint NOT NULL,
amt money NOT NULL,
placed_at timestamp NOT NULL,
cancelled_at timestamp,
returend_at timestamp,
failed_at timestamp,
vendor_id int REFERENCES dim_vendors(id),
user_id int REFERENCES dim_users(id)
);