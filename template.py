template = '''
UPDATE {d[0]}
SET {d[1]} = 
(
    SELECT TIMESTAMP WITHOUT TIME ZONE 'epoch' +
    ( SELECT EXTRACT( EPOCH FROM {d[1]}::timestamptz ) * 1000 ) * INTERVAL '1 second'
)
WHERE {d[1]} < '1980-01-01'::date;
'''

# template = '''SELECT COUNT(*) FROM {d[0]} WHERE {d[1]} IS NULL; --'''

# template = '''SELECT COUNT(*) FROM {d[0]} WHERE {d[1]} < '1980-01-01'::date; --'''