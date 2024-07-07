CREATE OR REPLACE PROCEDURE "STG".agg_tripdata()
LANGUAGE plpgsql
as $$
DECLARE
	v_run_time TIMESTAMP;
	v_status TEXT;
	v_error_message TEXT;
	
BEGIN
	v_run_time := NOW();
	v_status := 'SUCCESS';
	v_error_message := NULL;
	
	INSERT INTO "PRD".daily_agg_tripdata
	SELECT cast(pickup_date as date),
		sum(passenger_count) total_passenger_count,
		avg(passenger_count) avg_passenger_count,
		sum(trip_distance) tot_distance,
		avg(trip_distance) avg_trip_distance,
		sum(fare_amount) total_tfare,
		avg(fare_amount) avg_tfare,
		sum(tip_amount) total_tip,
		avg(trip_distance) avg_tip
	from "STG".tripdata
	group by cast (pickup_date as date);

	INSERT INTO "PRD".daily_agg_tripdata_channel
	SELECT cast(pickup_date as date),
			payment_type,
		sum(passenger_count) total_passenger_count,
		avg(passenger_count) avg_passenger_count,
		sum(trip_distance) tot_distance,
		avg(trip_distance) avg_trip_distance,
		sum(fare_amount) total_tfare,
		avg(fare_amount) avg_tfare,
		sum(tip_amount) total_tip,
		avg(trip_distance) avg_tip
	from "STG".tripdata
	group by cast (pickup_date as date), payment_type;
	
	----LOG OUTCOME
	INSERT INTO "STG".procedure_log(run_time, status, error_message)
	VALUES (v_run_time, v_status, v_error_message);

EXCEPTION
	WHEN OTHERS THEN
		v_status := 'FAILED';
		v_error_message := SQLERRM;
		
		INSERT INTO "STG".procedure_log(run_time, status, error_message)
		VALUES (v_run_time, v_status, v_error_message);

		
		
		



END;
$$