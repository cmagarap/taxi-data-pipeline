USE taxidb;

CREATE TABLE trip(
    VendorID INT NOT NULL,
    tpep_pickup_datetime DATETIME NOT NULL,
    tpep_dropoff_datetime DATETIME NOT NULL,
    passenger_count BIGINT NOT NULL,
    trip_distance DOUBLE NOT NULL,
    RatecodeID BIGINT NOT NULL,
    store_and_fwd_flag VARCHAR(255) NOT NULL,
    PULocationID INT NOT NULL,
    DOLocationID INT NOT NULL,
    payment_type BIGINT NOT NULL,
    fare_amount DOUBLE NOT NULL,
    extra DOUBLE NOT NULL,
    mta_tax DOUBLE NOT NULL,
    tip_amount DOUBLE NOT NULL,
    tolls_amount DOUBLE NOT NULL,
    improvement_surcharge DOUBLE NOT NULL,
    total_amount DOUBLE NOT NULL,
    congestion_surcharge DOUBLE NOT NULL,
    Airport_fee DOUBLE NOT NULL
);
