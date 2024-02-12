# Candidates - Job test

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

### Description

In this repository we have an ETL's process based in a CSV file with randomly generated data of candidates from February 22, 2020 until May 13, 2022 with 50.000 rows and 10 columns that after processing are now 16 columns.

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

The visualizations that I am expecting are:
   - Hires by technology (pie chart).
   - Hires by year (horizontal bar chart).
   - Hires by seniority (bar chart).
   - Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart) .

> <span style="color:#3c4e29; font-weight:bold">[Considerations]</span>
>
> <span style="color:#5b753f">This project is the first workshop of the ETL subject of Artificial Intelligence & Data Engineering at the Universidad Autónoma de Occidente under the teaching of [Javier Alejandro Vergara Zorilla](https://www.linkedin.com/in/javier-alejandro-vergara/).</span>

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
      In this, I use [ngrok](https://ngrok.com/download) to create a public tunnel with _TCP protocol_ to connect _Looker Studio_ with _Local PostgreSQL_ and get all data of **applicant** table.

      _AWS RDS_ give us a _Public Host_ to connect if the setting of _AWS VPC_ allows it.

   - **Consume block**:
      Here, we look the dashboard which users will see and can analyze. This dashboard is in _Looker Studio_, which gives us public access.

   - **Users representation**:
      Represents each of us.

#### Diagram: Local Flow.
   ![Local Flow - Data Arquitecture Diagram](https://gist.github.com/assets/92474551/c44df4de-c77a-4032-bc15-1a29bc57ed09)

#### Diagram: Cloud Flow.
   ![Cloud Flow - Data Arquitecture Diagram](https://gist.github.com/assets/92474551/c2517643-a25b-4065-b196-56c999ecfe3c)

---
### Step by step for execution

Following instructions are based on Windows 11 OS:

1. **Requirements**: To have the required tools for the execution of the repository correctly, so it's necessary to have the following:

   - <img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/pandas-icon.svg" alt="Pandas Python" width="21px" height="21px"> <img src="https://github.com/get-icon/geticon/raw/master/icons/numpy-icon.svg" alt="Numpy Python" width="21px" height="21px"> **[Python](https://www.python.org/downloads/)** _(Optional: used version 3.10.3)_.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/git-icon.svg" alt="Git" width="21px" height="21px"> **[Git](https://git-scm.com/downloads)** _(Optional: used version 2.43.0)_.
   - <img src="https://assets-global.website-files.com/63ed4bc7a4b189da942a6b8c/63ef8624e010d9861920be4e_ngrok-favicon.svg" alt="Git" width="21px" height="21px"> **[Ngrok](https://ngrok.com/download)** _(Optional: used version 3.6.0, this is only requirement if you want to connect Looker Studio to Local PostgreSQL)_.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/postgresql-logo.svg" alt="PostgreSQL" width="21px" height="21px"> **[Postgres](https://www.postgresql.org/download)** _(Optional: used version 16.1)_.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/postgresql.svg" alt="PgAdmin 4" width="21px" height="21px"> **[PgAdmin 4](https://www.pgadmin.org/download/)** _(Optional: used version 7.8, PosgreSQL's installation brings PgAdmin 4)_.
   - <img src="https://github.com/get-icon/geticon/raw/master/icons/aws.svg" alt="AWS" width="21px" height="21px"> <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/aws-rds.svg" alt="AWS RDS" width="21px" height="21px"> **[AWS RDS](https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiwkpv2pKSEAxWPuVoFHf2EAbwYABAAGgJ2dQ&ase=2&gclid=CjwKCAiA_aGuBhACEiwAly57MTL4U4hy14avuIvQqnyTW3qLO0oDvonHgfXrsmleQHE-rEK8zTKxlxoCHoMQAvD_BwE&ohost=www.google.com&cid=CAESVeD2Jr0_QQpQLU5ADLjI5Fz49bQCraF74sHyYXzpOCr12nkr91opntblv7p3tuhYFZXQE7r84QneeMHj3shjJg64CTJEDkXS3koCfOUcMVWMdTTk_b0&sig=AOD64_0-ZEYfY4AJ3dBJsNKYxvHHnBtuXw&q&nis=4&adurl&ved=2ahUKEwjcrZT2pKSEAxUpfjABHe_IApcQ0Qx6BAgIEAE)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> **[GitHub](https://github.com/)**.
   - <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/looker-icon.svg" alt="Looker Studio" width="21px" height="21px"> **[Looker Studio](https://lookerstudio.google.com/)**.

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

   > NOTE
   >
   > If you notice, AWS RDS was mentioned and in the .gitignore file there is aws_credentials.ini filename. In the process as will be evidenced below, you will find the screenshots of part of the services and connections established in AWS to connect me from the execution of these notebooks to Looker Studio.
   >
   > The service at this moment is down for the elimination of unnecessary costs, if it's needed in a few adjustments it will be implemented.
   >
3. Create virtual environment for Python:

   ```python
   python -m venv venv
   ```
4. Choose venv as Kernel for .ipynb files in the folder **notebooks**.
   ![Evidence selection of Venv](https://gist.github.com/assets/92474551/e8df45a4-15ef-47e5-8dde-d1f388cdfe40)

   In each file in **notebooks**, there is a code line to install required libraries if necessary with the title '_Install requirement libraries_'.

   As it's in the following screenshot:
  ![Evidence of section Install requirement libraries](https://gist.github.com/assets/92474551/178d3df4-ad5a-4f97-a7e3-f6d36b8a83eb)

5. Create the _TCP tunnel_ to connect _Local PostgreSQL_ to _Looker Studio_.

   After install _Ngrok_, we need to execute it and sign in with our accounts to get tokens, because to create the tunnel, Ngrok require a token.

   Finally, knowing our port on which PostgreSQL is running, we execute the following where 'port' is the port that we know:

   ```bash
   ngrok tcp port
   ```
   Such as:
   ![Evidence of Ngrok is running](https://gist.github.com/assets/92474551/9f59a0ca-a9cc-4ce8-bc29-323ace774b9f)
   According the example, our host is `4.tcp.ngrok.io` and our port `10297` to put in "*database authentication*" in PostgreSQL connector of _Looker Studio_.

6. Explorate the notebooks in the folder **notebooks**. There are two notebooks: _load_csv_file_ and _EDA_report_.

   - **load_csv_file:** Its objective is take the raw dataset in a csv file and load it in a PosgreSQL database within the **raw_applicant** table.
   - **eda_report:** Its objective is take data of **raw_applicant**, explore, transform, analyze and load it in the same database within **applicant** table.

   > NOTE
   >
   > To execute in order, let's start with **load_csv_file** and later **eda_report**.
   >

7. Then executed every notebook, we should verify the existence of the database.

   As the AWS RDS service will only be active on occasions that merit it, according to the project, it will have been performed on the local PostgreSQL; so openning PgAdmin 4 we will be able to verify the existence of the database and the records loaded.

8. Now, we go to Looker Studio to look the dashboard created with these data.

   **Link of the dashboard:** [Dashboard in Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).

   If we want, could update the data by editing the connection previously established with our credentials or create a new dashboard:

   1. Click on _Add data_ option:
      ![Click on Add data](https://gist.github.com/assets/92474551/026d1a08-6731-48c0-8f43-9a0ee781e6cd)

   2. Choose PosgreSQL Connector:
      ![To choose PostgreSQL Connector in Looker Studio](https://gist.github.com/assets/92474551/eff688be-029b-4457-b788-f80826862ac1)

   3. User our credentials to connect and choose _applicant_ table of the database.

      To use our credentials, we need according Ngrok gave us, our host and port:

      ```ini
      host = 4.tcp.ngrok.io
      port = 10297
      database = etl_workshop_first
      user = --------
      password = --------
      ```

      ![Config to connect Looker Studio with PostgreSQL](https://gist.github.com/assets/92474551/0ca9ed14-6365-4792-b845-9c1ca3b9e116)

      Now, we have the data sync with Looker Studio.

---
### Evidence

   1. Evidence of _etl_workshop_first_ creation.
   
      ![Evidence of _etl_workshop_first_ creation](https://gist.github.com/assets/92474551/0d79098a-8859-4e6b-af15-f29d04dfdee2)

   2. Loading of records in **raw_applicant** table done.

      Inside of **load_csv_file** file is the evidence of execution.

      ![raw applicant data](https://gist.github.com/assets/92474551/35a5912d-65dd-4680-aca3-d6b7e0b240f3)

   3. Loading of records in **applicant** table done.

      Inside of **eda_report** file is the evidence of execution.

      ![applicant_data](https://gist.github.com/assets/92474551/13086343-0d5b-4829-84c6-05d1c57d00b9)

   4. Creation account in AWS for later use of AWS RDS.
      ![Creation account in AWS for later use of AWS RDS](https://gist.github.com/assets/92474551/c4a84a2c-d8d9-4822-a1af-85cfe04485a0)

   5. Creation Database in AWS RDS and Stopping for now.
      ![Creation Database in AWS RDS and Stopping for now](https://gist.github.com/assets/92474551/c9cdeb78-b02c-4d80-8dd6-04950c75d4e3)

   6. After used to get data for Looker Studio, I delete it to override costs.
      ![After used to get data for Looker Studio, I delete it to override costs](https://gist.github.com/assets/92474551/82ab2ecf-060a-47ef-9f9d-df845433a579)

   7. Connection established between Looker Studio and AWS RDS with _etlworhshop_ database.
      ![Connection established between Looker Studio and AWS RDS with _etlworhshop_ database](https://gist.github.com/assets/92474551/0d18940d-f7c2-47de-9276-2f5507cf3578)

   8. Ngrok is running.
      ![Evidence of Ngrok is running](https://gist.github.com/assets/92474551/9f59a0ca-a9cc-4ce8-bc29-323ace774b9f)

   9. Connection with Local PostgreSQL.
      ![Config to connect Looker Studio with PostgreSQL](https://gist.github.com/assets/92474551/0ca9ed14-6365-4792-b845-9c1ca3b9e116)

   10. Using pre-commits.
      ![Using pre-commits](https://gist.github.com/assets/92474551/75f80c5f-381d-4bb1-9c04-00f94659f9ff)


---
### My support resources

- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Github: [Workshop 001 - ETL Education Repository](https://github.com/dventep/workshop001_etl_education/tree/develop)
- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Gist: [Workshop 001 - ETL Education Gist](https://gist.github.com/dventep/579f1646c6d6011e4e8314fb85482eba)
