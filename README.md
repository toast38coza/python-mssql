# python3.6-mssql
A Python 3.6 Docker image which is capable of talking to MS SQL

This sets up a Python container with freetds, pyodbc and django-pyodbc-azure

See `docker-compose.text.yml` + the `exmaple` Django prject for an example using this with Django.

## Notes:

### Example Django settings:

```
DATABASES = {
    'default': {
        'ENGINE': "sql_server.pyodbc",
        'HOST': "db",
        'PORT':'1433',
        'USER': "sa",
        'PASSWORD': os.environ.get('SA_PASSWORD'),
        'NAME': os.environ.get('DB_NAME', 'lulu'),
        # 'AUTOCOMMIT': True,
        'OPTIONS': {
            "driver": "FreeTDS",
            "host_is_server": True,
            "unicode_results": True,
            "extra_params": "tds_version=8.0",
        }
    }
}
```

### Example pyodbc connection string:

```
db_name = os.environ.get('DB_NAME')
pwd = os.environ.get('SA_PASSWORD')
connection_string = "driver=FreeTDS;server=db;PORT=1433 database=master;UID=sa;PWD={};TDS_Version=8.0;".format(pwd)
```