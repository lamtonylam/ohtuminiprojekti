# ohtuminiprojekti
[![codecov](https://codecov.io/gh/lamtonylam/ohtuminiprojekti/graph/badge.svg?token=N62JBV2CMT)](https://codecov.io/gh/lamtonylam/ohtuminiprojekti)  
![CI](https://github.com/lamtonylam/ohtuminiprojekti/actions/workflows/ci.yaml/badge.svg?branch=main)
### [Product backlog](https://github.com/users/lamtonylam/projects/4)

### [Sprint backlog](https://helsinkifi-my.sharepoint.com/:x:/g/personal/bbsebast_ad_helsinki_fi/Ee2nabIYHuRJuohTCCOQPcYBBL0G3sMeIiiRyvB-SzPxGQ?e=jA78dm)

## Definition of Done
- Each user story has at least one test and it has been run successfully
- The feature has been integrated, and documented extensively
- The code has been reviewed by team
- The code style is consistent
- The requirements have been validated
- The acceptance criteria has been met


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
DATABASE_URL=postgresql:///DATABASE_NAME
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


