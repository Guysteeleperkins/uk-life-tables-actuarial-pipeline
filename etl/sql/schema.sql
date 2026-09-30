
DROP TABLE IF EXISTS life_tables;

CREATE TABLE life_tables (
    time_period TEXT    NOT NULL,
    start_year  INTEGER NOT NULL,
    end_year    INTEGER NOT NULL,
    sex         TEXT    NOT NULL CHECK (sex IN ('male', 'female')),
    age         INTEGER NOT NULL CHECK (age BETWEEN 0 AND 100),
    mx          REAL    NOT NULL CHECK (mx >= 0),
    qx          REAL    NOT NULL CHECK (qx BETWEEN 0 AND 1),
    lx          REAL    NOT NULL CHECK (lx >= 0),
    dx          REAL    NOT NULL CHECK (dx >= 0),
    ex          REAL    NOT NULL CHECK (ex >= 0),
    PRIMARY KEY (time_period, sex, age)
);

CREATE INDEX idx_sex_age_year ON life_tables (sex, age, start_year);