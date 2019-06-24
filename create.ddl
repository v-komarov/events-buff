CREATE KEYSPACE IF NOT EXISTS events WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};

CREATE TABLE IF NOT EXISTS events_buff (
evt_id text,
datetime_evt timestamp,
data text,
PRIMARY KEY (evt_id,datetime_evt)
) WITH CLUSTERING ORDER BY (datetime_evt ASC);
