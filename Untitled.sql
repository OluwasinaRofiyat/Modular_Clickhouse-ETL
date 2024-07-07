CREATE TABLE IF NOT EXISTS "PRD".daily_agg_tripdata(
			pickup_date date primary key,
			total_passenger_count int,
			avg_passenger_count float,
			tot_distance float,
			avg_distance float,
			total_tfare float,
			avg_tfare float,
			total_tip float,
			avg_tip float
);

CREATE TABLE IF NOT EXISTS "PRD".daily_agg_tripdata_channel(
			pickup_date date not null,
			payment_type text,
			total_passenger_count int,
			avg_passenger_count float,
			tot_distance float,
			avg_distance float,
			total_tfare float,
			avg_tfare float,
			total_tip float,
			avg_tip float,
			PRIMARY KEY(pickup_date, payment_type)
);