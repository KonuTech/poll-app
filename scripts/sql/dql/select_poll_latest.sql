-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
     *
FROM poll.polls
WHERE
    o.poll_id = (
        SELECT
            id
        FROM
            poll.polls
        ORDER BY
            id DESC
        LIMIT 1
        );
