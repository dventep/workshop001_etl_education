# workshop001_etl_education

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

### Description
Repository of workshop001 developed.

Link Power BI

https://app.powerbi.com/groups/me/reports/932696b5-e5f6-4c88-a969-1101609ebee8?pbi_source=desktop

### Purpose - Reason to be

### Step by step for execution

Following instructions are based on Windows 11 OS:

1. To have the required tools for the execution of the repository correctly, so it's necessary to have the following:

   - <img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/pandas-icon.svg" alt="Pandas Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/numpy-icon.svg" alt="Numpy Python" width="21px" height="21px"> **Python** _(Optional: used version 3.10.3)_.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/git-icon.svg" alt="Git" width="21px" height="21px"> **Git** _(Optional: used version 2.43.0)_.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/postgresql-logo.svg" alt="PostgreSQL" width="21px" height="21px"> **Postgres** _(Optional: used version 16.1)_.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/postgresql.svg" alt="PgAdmin 4" width="21px" height="21px"> **PgAdmin 4** _(Optional: used version 7.8)_.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> **GitHub**.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/aws.svg" alt="AWS" width="21px" height="21px"> <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/aws-rds.svg" alt="AWS RDS" width="21px" height="21px"> **AWS RDS**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/looker-icon.svg" alt="Looker Studio" width="21px" height="21px"> **Looker Studio**.

   > [!NOTE]
   > In this case, I use Docker to deploy PostgreSQL _(Port 5432)_ with host _localhost_.

2. Create credentials file to connect local Postgres.

   The file must is locate from root folder in _./code/config/_ with name _credentials.ini_. Its structure must be such as the following in which between single quotation marks (') the whole content including the quotation marks must be replaced by the respective information:

   ```ini
   [postgresql]
   host='localhost (default)'
   database=etl_workshop_first
   user='postgres (default)'
   password=' (default)'
   port='5432 (default)'
   ```

   > [!NOTE]
   > If you notice, AWS RDS was mentioned and in the .gitignore file there is aws_credentials.ini filename. In the process as will be evidenced below, you will find the screenshots of part of the services and connections established in AWS to connect me from the execution of these notebooks to Looker Studio.
   >
   > The service at this moment is down for the elimination of unnecessary costs, if it's needed in a few adjustments it will be implemented.

3. Create virtual environment for Python:

   ```python
   python -m venv venv
   ```

4. Choose venv as Kernel for .ipynb files in the folder **notebooks**.

   In each file in **notebooks**, there is a code line to install required libraries if necessary with the title '_Install requirement libraries_'.

5. Explorate the notebooks in the folder **notebooks**. There are two notebooks: _load_csv_file_ and _EDA_report_.

   - **load_csv_file:** Its objective is take the raw dataset in a csv file and load it in a PosgreSQL database within the **raw_applicant** table.
   - **eda_report:** Its objective is take data of **raw_applicant**, explore, transform, analyze and load it in the same database within **applicant** table.

   > [!NOTE] 
   > To execute in order, let's start with **load_csv_file** and later **eda_report**.

### Execution example

### Evidence

### Support resources

   - Github: [Workshop 001 - ETL Education Repository]

   - Gist: [Workshop 001 - ETL Education Gist]

[Workshop 001 - ETL Education Repository]: (https://gist.github.com/dventep/579f1646c6d6011e4e8314fb85482eba)
[Workshop 001 - ETL Education Gist]: (https://gist.github.com/dventep/579f1646c6d6011e4e8314fb85482eba)
