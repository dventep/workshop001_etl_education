# Candidates - Job test

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)


### Description

In this repository we have an ETL's process based in a CSV file with randomly generated data of candidates from February 22, 2020 until May 13, 2022 with 50.000 rows and 10 columns that after processing are now 16 columns to create a dashboard of hired candidates.

The process start with the CSV file that is read by an Jupyter Notebook to transfer the data to PostgreSQL. Then this data is read by another Jupyter Notebook that applies ETL methodologies to know, organize, calculate and modify it; and same data with additions are loaded again to PostgreSQL. Finally, a dashboard retrieves it to communicate its raison d'être.

The tools used are:

   - <img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/pandas-icon.svg" alt="Pandas Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/numpy-icon.svg" alt="Numpy Python" width="21px" height="21px"> **[Python](https://www.python.org)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/git-icon.svg" alt="Git" width="21px" height="21px"> **[Git](https://git-scm.com/about)**.
   - <img src="https://assets-global.website-files.com/63ed4bc7a4b189da942a6b8c/63ef8624e010d9861920be4e_ngrok-favicon.svg" alt="Git" width="21px" height="21px"> **[Ngrok](https://ngrok.com)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/postgresql-logo.svg" alt="PostgreSQL" width="21px" height="21px"> **[Postgres](https://www.postgresql.org/)**.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/postgresql.svg" alt="PgAdmin 4" width="21px" height="21px"> **[PgAdmin 4](https://www.pgadmin.org/)**.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/aws.svg" alt="AWS" width="21px" height="21px"> <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/aws-rds.svg" alt="AWS RDS" width="21px" height="21px"> **[AWS RDS](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiwkpv2pKSEAxWPuVoFHf2EAbwYABAAGgJ2dQ&ase=2&gclid=CjwKCAiA_aGuBhACEiwAly57MTL4U4hy14avuIvQqnyTW3qLO0oDvonHgfXrsmleQHE-rEK8zTKxlxoCHoMQAvD_BwE&ohost=www.google.com&cid=CAESVeD2Jr0_QQpQLU5ADLjI5Fz49bQCraF74sHyYXzpOCr12nkr91opntblv7p3tuhYFZXQE7r84QneeMHj3shjJg64CTJEDkXS3koCfOUcMVWMdTTk_b0&sig=AOD64_0-ZEYfY4AJ3dBJsNKYxvHHnBtuXw&q&nis=4&adurl&ved=2ahUKEwjcrZT2pKSEAxUpfjABHe_IApcQ0Qx6BAgIEAE)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> **[GitHub](https://github.com/)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/looker-icon.svg" alt="Looker Studio" width="21px" height="21px"> **[Looker Studio](https://lookerstudio.google.com/)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/visual-studio-code.svg" alt="Looker Studio" width="21px" height="21px"> **[Visual Studio Code](https://code.visualstudio.com/)**.

---
### Purpose - Raison d'être

The project is oriented to present in a general way the candidates that are hired under the requirements provided by a job test and to perfom it in a visual way by means of sampling specific data to comply with it.

The visualizations that we am expecting are:
   - Hires by technology (pie chart).
   - Hires by year (horizontal bar chart).
   - Hires by seniority (bar chart).
   - Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart) .

>[!NOTE]
> <span style="color:#5b753f">This project is the first workshop of the ETL subject of Artificial Intelligence & Data Engineering at the Universidad Autónoma de Occidente under the teaching of [Javier Alejandro Vergara Zorilla](https://www.linkedin.com/in/javier-alejandro-vergara/).</span>

---
### Dashboard

1. Home - Dashboard.
   ![Home - Dashboard](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/home_dashboard.png)
   
3. Technology Category - Dashboard.
   ![Technology Category - Dashboard](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/technology_category_dashboard.png)

4. Year & Seniority - Dashboard.
   ![Year & Seniority - Dashboard](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/year_and_seniority_dashboard.png)

5. Country over years - Dashboard.
   ![Country over years - Dashboard](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/012b5915c054d81db4c6892a2899bf98f955d0fd/country_over_years_dashboard.png)

6.  Table of candidates hired - Dashboard.
   ![Table of candidates hired - Dashboard](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/a84fb47e5accb0fa3188f526bfc91b73c3af4029/table_of_candidates_hired_dashboard.png)

   **Link of the interactive dashboard:** [Dashboard in Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).

   **Look PDF:** [Dashboard in PDF](files/Candidates%20-%20ETL%20Workshop%20001.pdf).

---
### Data arquitecture diagram

   Let's see the flow of data in this project. Below there are two diagrams, these will allow to have a more visual knowledge of the process that is carried out in the notebooks that are in this repository.

- **Metadata of diagrams:**
  In this part, there are a few explaining of every block and his properties that you will look in the diagrams.

   - **Data source block**:
      There is a CSV file with 50.000 rows of candidates data for this job test. This starting point file is called _candidates.csv_.

   - **Data pipeline block**:
      In this section, there are two jupyter notebooks, which are:

      - **load_csv_file**.
         The process of reading the CSV file and loading of data to **raw_applicant** table in a PostgreSQL Database called **etl_workshop_first**.

      - **eda_report**.
         The process of data collection of **raw_applicant** table in **etl_workshop_first** database to explorate, transform and clean it. Then load data to **applicant** tabe in the database.

   - **Server block**:
      There are two options, load to the local server or to the AWS RDS server. On either server, the **etl_workshop_first** database will be used which will have two tables, **raw_applicant** and **applicant**.

      If the database doesn't exist, **load_csv_file** notebook will create it and its structure.

   - **Connection tunnel block**:
      In this, we use [ngrok](https://ngrok.com/download) to create a public tunnel with _TCP protocol_ to connect _Looker Studio_ with _Local PostgreSQL_ and get all data of **applicant** table.

      _AWS RDS_ give us a _Public Host_ to connect if the setting of _AWS VPC_ allows it.

   - **Consume block**:
      Here, we look the dashboard which users will see and can analyze. This dashboard is in _Looker Studio_, which gives us public access.

   - **Users representation**:
      Represents each of us.

#### Diagram: Local Flow.
   ![Local Flow - Data Arquitecture Diagram](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/local_flow_diagram_data_arquitecture_diagram.png)

#### Diagram: Cloud Flow.
   ![Cloud Flow - Data Arquitecture Diagram](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/Cloud_Flow_Data_Arquitecture_Diagram.png)
   
---
### Installing guide

Read [installing_README.md](installing_README.md) for details on step by step to install the requirements to deploy this repository.

---
### Project organization

```
   ├── code
   │   ├── config
   │   │   ├── .pre-commit-config.yaml          <- Configuration for pre-commit hooks.
   │   │   └── requirements.txt                 <- Python package dependencies for project.
   │   ├── database_models
   │   │   └── sql_classes.py                   <- SQL classes for database tables.
   │   └── connect_database.py                  <- Code to establish and manage PostgreSQL database connection module.
   ├── data
   │   └── candidates.csv                       <- Candidates data in CSV format.
   ├── files
   │   └── Candidates - ETL Workshop 001.pdf    <- Dashboard with graphical results of candidates hired.
   ├── notebooks
   │   ├── eda_report.ipynb                     <- Exploratory Data Analysis (EDA) Report: PostgreSQL data preprocessing, insights.
   │   └── load_csv_file.ipynb                  <- CSV file loaded to PostgreSQL.
   ├── installing_README.md                     <- Installation instructions for required tools and process.
   ├── README.md                                <- The README to start the ETL process dashboard with Python and randomly generated candidate data.
   └── .gitignore                               <- All files to avoid being read.
```

---
### Evidence

   1. Evidence of _etl_workshop_first_ creation.

      ![Evidence of _etl_workshop_first_ creation](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/evidence_of_etl_workshop_first_creation.png)

   2. Loading of records in **raw_applicant** table done.

      Inside of **load_csv_file** file is the evidence of execution.

      ![raw applicant data](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/creation_account_in_aws.png)

   3. Loading of records in **applicant** table done.

      Inside of **eda_report** file is the evidence of execution.

      ![applicant_data](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/records_in_applicant_table.png)

   4. Creation account in AWS for later use of AWS RDS.
      ![Creation account in AWS for later use of AWS RDS](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/creation_account_in_aws.png)

   5. Creation Database in AWS RDS and Stopping for now.
      ![Creation Database in AWS RDS and Stopping for now](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/creation_database_in_aws_rds.png)

   6. After used to get data for Looker Studio, we delete it to override costs.
      ![After used to get data for Looker Studio, we delete it to override costs](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/after_used_to_get_data_for_looker_studio.png)

   7. Connection established between Looker Studio and AWS RDS with _etlworhshop_ database.
      ![Connection established between Looker Studio and AWS RDS with _etlworhshop_ database](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/connection_established_between_looker_studio.png)

   8. Ngrok is running.
      ![Evidence of Ngrok is running](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/evidence_of_ngrok_is_running.png)

   9. Connection with Local PostgreSQL.
      ![Config to connect Looker Studio with PostgreSQL](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/config_to_connect_looker_studio_with_postgresql.png)

   10. Using pre-commits.
      ![Using pre-commits](https://gist.githubusercontent.com/dventep/579f1646c6d6011e4e8314fb85482eba/raw/79d0afa23cb3a60b23821531b35c07fea0cb1790/using_pre_commits.png)

---
### My support resources

- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Github: [Workshop 001 - ETL Education Repository](https://github.com/dventep/workshop001_etl_education/tree/develop).
- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Gist: [Workshop 001 - ETL Education Gist](https://gist.github.com/dventep/579f1646c6d6011e4e8314fb85482eba).
- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/looker-icon.svg" alt="Looker Studio" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Looker Studio: [Dashboard - Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).
