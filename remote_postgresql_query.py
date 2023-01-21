import psycopg2


url = "postgres://onzwlhkt:2WFNbjAoKmzjQByP6slily8nKIAP0fWW@hattie.db.elephantsql.com/onzwlhkt"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute(
    """
        SELECT
            *
        FROM
            "onzwlhkt"."public"."users"
        LIMIT 1
        ;
    """
)
first_user = cursor.fetchall()
print(first_user)
connection.close()
