-- noinspection SpellCheckingInspectionForFile

-- noinspection SqlNoDataSourceInspectionForFile

INSERT INTO poll.options (
	 option_text
	,poll_id
) VALUES (%s, %s) RETURNING id
;
