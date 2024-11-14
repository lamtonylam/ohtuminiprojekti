# ohtuminiprojekti

### [Product backlog](https://github.com/users/lamtonylam/projects/4)

### [Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/bbsebast_ad_helsinki_fi/Ee2nabIYHuRJuohTCCOQPcYBBL0G3sMeIiiRyvB-SzPxGQ?e=jA78dm)

## Local development

Clone to local machine

```
git clone git@github.com:lamtonylam/ohtuminiprojekti.git
```

install dependencies

```
poetry install
```

go to poetry shell

```
poetry shell
```

create .env file with the following values  
For DATABASE_URL you can use either a local instance of postgres or hosted solution such as [aiven.io](aiven.io)

```
DATABASE_URL=postgresql://DATABASE_NAME
TEST_ENV=true
SECRET_KEY=satunnainen_merkkijono
```

initialize database

```
python3 src/db_helper.py
```

run flask app

```
python3 src/index.py
```
