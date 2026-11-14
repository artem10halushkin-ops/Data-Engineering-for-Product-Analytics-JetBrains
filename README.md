# Data-Engineering-for-Product-Analytics-JetBrains

### `metadwh.py`
Contains the structure for our star schema tables:
* **`Facts`** — assembles all the information about the technical usage of queries by a particular user, along with metadata regarding the event.
* **`User`** — contains important information about each user. For the sake of a single source of truth, this information is not embedded directly in `Facts`, but stored in dimension tables like `User`.
* **`Dates`** — stores dates in `YYYY-MM-DD` format. Its ID is distinct and formed by a simple arithmetic operation (for example: `2026-01-01` -> `20260101`).
* **`Tables`** — stores distinguishable database tables accordingly.
* **`HRDB`** — simulates an existing database containing personnel information, from which we retrieve attributes like the `Team name` in our analytical queries.

### `seed.py`
Represents the class for seeding the created tables: populates `Dates` for 5 years ahead and fills the simulated `HRDB` table with personnel information.

### `etl_pipeline.py`
Implements the extraction, transformation, and loading of daily usage statistics into our meta data warehouse:
* **`extract`** — fetches data from the S3 data lake and the HR database for a given date.
* **`transform`** — prepares the data according to the schema described in `metadwh.py` for uploading, avoiding the creation of duplicate records.
* **`load`** — loads the transformed data into the meta DWH.

### `extract_trino.sql`
Contains the SQL query used for the extraction part of the ETL process.

### `queries.sql`
Contains two analytical queries for the given task, tailored to this specific schema implementation.