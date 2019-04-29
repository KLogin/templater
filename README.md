# Templater

Util to create text by template

You can use this simple script as you whant, but generally usage lookse like this:

## 1. Write your template
Write your template in file **template.py**

```python
template = '''SELECT COUNT(*) FROM {d[0]} WHERE {d[1]} IS NULL;'''
```

`{d[id]}` - id means id of data from **data.py**

## 2. Fill your data
Write your data in file **data.py**

```python
data = [
    ['agent', 'created_at'],
    ['agent', 'updated_at']
]
```
You can add as much data as you whant, but be cearful order is metter.

## 3. Run script
```cmd
python generate.py > tmp.txt
```

## 4. Fin
Check output file **tmp.txt**

```sql
SELECT COUNT(*) FROM agent WHERE created_at IS NULL;

SELECT COUNT(*) FROM agent WHERE updated_at IS NULL;
```
