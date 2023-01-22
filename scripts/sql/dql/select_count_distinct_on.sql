SELECT
     DISTINCT ON (o.poll_id) poll_id
    ,o.id
    ,o.option_text
    ,COUNT(v.option_id) AS vote_count
FROM poll.option AS o
LEFT JOIN poll.votes AS v
ON o.id = v.option_id
GROUP BY
    o.id
ORDER BY
     o.poll_id
    ,vote_count DESC
;