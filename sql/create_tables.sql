DROP TABLE IF EXISTS production;
DROP TABLE IF EXISTS quality_checks;
DROP TABLE IF EXISTS downtime;

CREATE TABLE production (
    date DATE,
    line_id INT,
    product_name TEXT,
    units_produced INT,
    shift TEXT
);

CREATE TABLE quality_checks (
    id SERIAL PRIMARY KEY,
    date DATE,
    line_id INT,
    defect_type TEXT,
    defect_count INT
);

CREATE TABLE downtime (
    id SERIAL PRIMARY KEY,
    date DATE,
    line_id INT,
    reason TEXT,
    minutes_lost INT
);

