CREATE TABLE IF NOT EXISTS "onzwlhkt"."public"."users" (
     id INTEGER PRIMARY KEY
    ,name TEXT
);

-- ON CONFLICT: https://www.postgresql.org/docs/current/sql-insert.html
INSERT INTO "onzwlhkt"."public"."users" (
     id
    ,name
)
VALUES (1, 'Bob Smith')
ON CONFLICT (id) DO NOTHING;

SELECT
    *
FROM "onzwlhkt"."public"."users"
LIMIT 100
;