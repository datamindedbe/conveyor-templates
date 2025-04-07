MODEL (
  name sqlmesh_example.incremental_model,
  kind INCREMENTAL_BY_TIME_RANGE (
    time_column event_date
  ),
  start '2020-01-01',
  cron '@daily',
  grain (id, event_date)
);

SELECT
  id,
  item_id,
  event_date,
  price,
FROM
  sqlmesh_example.seed_model
INNER JOIN
  sqlmesh_example.seed2_model
USING (id)
WHERE
  event_date BETWEEN @start_date AND @end_date
  