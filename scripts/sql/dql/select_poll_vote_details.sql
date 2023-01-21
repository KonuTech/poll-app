-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

SELECT
     o.id
    ,o.option_text
    ,COUNT(v.option_id) AS vote_count
    ,COUNT(v.option_id) / (SUM(COUNT(v.option_id)) OVER()) AS vote_percentage
FROM poll.options AS o
LEFT JOIN poll.votes AS v
ON o.id = v.option_id
WHERE o.poll_id = %s
GROUP BY
    o.id
;