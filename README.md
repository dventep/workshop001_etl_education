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

The visualizations that I am expecting are:
   - Hires by technology (pie chart).
   - Hires by year (horizontal bar chart).
   - Hires by seniority (bar chart).
   - Hires by country over years (USA, Brazil, Colombia, and Ecuador only)(multiline chart) .

>[!NOTE]
> <span style="color:#5b753f">This project is the first workshop of the ETL subject of Artificial Intelligence & Data Engineering at the Universidad Autónoma de Occidente under the teaching of [Javier Alejandro Vergara Zorilla](https://www.linkedin.com/in/javier-alejandro-vergara/).</span>

---
### Dashboard

1. Home - Dashboard.
   ![Home - Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/304759256-77482a38-61ca-4431-84e0-bc502570016c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T145653Z&X-Amz-Expires=300&X-Amz-Signature=d124dcfe2e19373405224d49ba0de232d40f8fd646e5a2a40275512b76712612&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)
   
3. Technology Category - Dashboard.
   ![Technology Category - Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/304129419-dd9a5f2e-c3d3-4c17-9c78-0f41368a599a.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T150644Z&X-Amz-Expires=300&X-Amz-Signature=43e990c5a7195c1641d4a0cb99cc32ccec7cb972c988e9fd41f5b62a7a433ff5&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

4. Year & Seniority - Dashboard.
   ![Year & Seniority - Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/304128943-192fd030-4d25-4bcb-b73c-f0a260efa9cd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T150714Z&X-Amz-Expires=300&X-Amz-Signature=6d620e4a5292522e429dc4a05f2a9b23c304ca67de7bc3e0588af4f3447a3ef2&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

5. Country over years - Dashboard.
   ![Country over years - Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/304762241-d712f601-1080-4da5-8bac-42a25938a4cb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T150947Z&X-Amz-Expires=300&X-Amz-Signature=b2e5e8b7cd7becc9a6f394fa3f96809fbad39182f993065c94d3eecdc40311dc&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

6.  Table of candidates hired - Dashboard.
   ![Table of candidates hired - Dashboard](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/304759513-b346a96c-608a-40a3-bb0d-8bf3f77b0a08.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T150918Z&X-Amz-Expires=300&X-Amz-Signature=5df025f955d90eff3473bb620adef06889aad69b9c411e3811bb324f18588c64&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   **Link of the interactive dashboard:** [Dashboard in Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).

   **Look PDF:** [Dashboard in PDF](https://docs.google.com/viewer?srcid=16Hq1Zg4BD6EV23qcGTasjwCc6axVRyhn&pid=explorer&efh=false&a=v&chrome=false&embedded=true).

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
   ![Local Flow - Data Arquitecture Diagram](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303946145-c44df4de-c77a-4032-bc15-1a29bc57ed09.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240214%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240214T225021Z&X-Amz-Expires=300&X-Amz-Signature=4b2d44749e21f2c2685dea15f681e4011599c0ab5e1c90a7f2a1101b9db42b50&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

#### Diagram: Cloud Flow.
   ![Cloud Flow - Data Arquitecture Diagram](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303948466-c2517643-a25b-4065-b196-56c999ecfe3c.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025348Z&X-Amz-Expires=300&X-Amz-Signature=3343e5682100c6193db7d02e39277c1e30c24586608edb7e6a7510a67a1bab06&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

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

>[!NOTE]
> If you notice, AWS RDS was mentioned and in the .gitignore file there is aws_credentials.ini filename. In the process as will be evidenced below, you will find the screenshots of part of the services and connections established in AWS to connect me from the execution of these notebooks to Looker Studio.
>
> The service at this moment is down for the elimination of unnecessary costs, if it's needed in a few adjustments it will be implemented.

3. Create virtual environment for Python:

   ```python
   python -m venv venv
   ```
4. Choose venv as Kernel for .ipynb files in the folder **notebooks**.
   ![Evidence selection of Venv](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303951049-e8df45a4-15ef-47e5-8dde-d1f388cdfe40.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025333Z&X-Amz-Expires=300&X-Amz-Signature=315b93903d3908b84692dd199e851519c9654ffc36046ce4a1744d24669d6620&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   In each file in **notebooks**, there is a code line to install required libraries if necessary with the title '_Install requirement libraries_'.

   As it's in the following screenshot:
  ![Evidence of section Install requirement libraries](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303951226-178d3df4-ad5a-4f97-a7e3-f6d36b8a83eb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025326Z&X-Amz-Expires=300&X-Amz-Signature=27f1f47d7eca5e587b81179010ebcef75eccab7dbd034053208427010621b0e1&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

5. Create the _TCP tunnel_ to connect _Local PostgreSQL_ to _Looker Studio_.

   After install _Ngrok_, we need to execute it and sign in with our accounts to get tokens, because to create the tunnel, Ngrok require a token.

   Finally, knowing our port on which PostgreSQL is running, we execute the following where 'port' is the port that we know:

   ```bash
   ngrok tcp port
   ```
   Such as:
   ![Evidence of Ngrok is running](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303951549-9f59a0ca-a9cc-4ce8-bc29-323ace774b9f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025318Z&X-Amz-Expires=300&X-Amz-Signature=4a9fcc8d19fd4a9296cbc886c1707ed40a20feee87e616264437d0714568a780&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)
   According the example, our host is `4.tcp.ngrok.io` and our port `10297` to put in "*database authentication*" in PostgreSQL connector of _Looker Studio_.

6. Explorate the notebooks in the folder **notebooks**. There are two notebooks: _load_csv_file_ and _EDA_report_.

   - **load_csv_file:** Its objective is take the raw dataset in a csv file and load it in a PosgreSQL database within the **raw_applicant** table.
   - **eda_report:** Its objective is take data of **raw_applicant**, explore, transform, analyze and load it in the same database within **applicant** table.

>[!NOTE]
> To execute in order, let's start with **load_csv_file** and later **eda_report**.

7. Then executed every notebook, we should verify the existence of the database.

   As the AWS RDS service will only be active on occasions that merit it, according to the project, it will have been performed on the local PostgreSQL; so openning PgAdmin 4 we will be able to verify the existence of the database and the records loaded.

8. Now, we go to Looker Studio to look the dashboard created with these data.

   **Link of the dashboard:** [Dashboard in Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).

   If we want, could update the data by editing the connection previously established with our credentials or create a new dashboard:

   1. Click on _Add data_ option:
      ![Click on Add data](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303954175-026d1a08-6731-48c0-8f43-9a0ee781e6cd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025255Z&X-Amz-Expires=300&X-Amz-Signature=8e6d81456e80a8b810ca91281db98f1dd048fa2eeb513eb7385c777ba2537bec&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   2. Choose PosgreSQL Connector:
      ![To choose PostgreSQL Connector in Looker Studio](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303954251-eff688be-029b-4457-b788-f80826862ac1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025247Z&X-Amz-Expires=300&X-Amz-Signature=51aa5b7e9d289ed07917c93bec7cb87ff8d0afd976670137b904a6cc3c46c1ac&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   3. User our credentials to connect and choose _applicant_ table of the database.

      To use our credentials, we need according Ngrok gave us, our host and port:

      ```ini
      host = 4.tcp.ngrok.io
      port = 10297
      database = etl_workshop_first
      user = --------
      password = --------
      ```

      ![Config to connect Looker Studio with PostgreSQL](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303954422-0ca9ed14-6365-4792-b845-9c1ca3b9e116.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025240Z&X-Amz-Expires=300&X-Amz-Signature=191d11604cdcee3a9ea162ee64208e24387d790d16d1cbef22b7c5e70cd1266f&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

      Now, we have the data sync with Looker Studio.

---
### Evidence

   1. Evidence of _etl_workshop_first_ creation.

      ![Evidence of _etl_workshop_first_ creation](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303954840-0d79098a-8859-4e6b-af15-f29d04dfdee2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025216Z&X-Amz-Expires=300&X-Amz-Signature=0dcda14550cd153e2872f6f8b567e548e00be31891e31e72946c717c0f02e5b6&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   2. Loading of records in **raw_applicant** table done.

      Inside of **load_csv_file** file is the evidence of execution.

      ![raw applicant data](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303897209-35a5912d-65dd-4680-aca3-d6b7e0b240f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025205Z&X-Amz-Expires=300&X-Amz-Signature=2a3ba515440a57d4b477df61516f2b0b0ef5e913c65999c7e03954dae7b329a2&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   3. Loading of records in **applicant** table done.

      Inside of **eda_report** file is the evidence of execution.

      ![applicant_data](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303897290-13086343-0d5b-4829-84c6-05d1c57d00b9.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025157Z&X-Amz-Expires=300&X-Amz-Signature=7a609c654ef0c4df694487ce1ad6a8f9fab489270f0ba2c267e929c4d8f08ca5&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   4. Creation account in AWS for later use of AWS RDS.
      ![Creation account in AWS for later use of AWS RDS](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303956012-c4a84a2c-d8d9-4822-a1af-85cfe04485a0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025143Z&X-Amz-Expires=300&X-Amz-Signature=dfb7374b81a7fdd4dcb9fb4dacf94b2227071fc5070e26f37cae2d7b76f4682d&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   5. Creation Database in AWS RDS and Stopping for now.
      ![Creation Database in AWS RDS and Stopping for now](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303956109-c9cdeb78-b02c-4d80-8dd6-04950c75d4e3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025134Z&X-Amz-Expires=300&X-Amz-Signature=81422e8412c2a9c27ae2556ddfad3182f4ae3f64792f405a422c19dcee44300f&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   6. After used to get data for Looker Studio, I delete it to override costs.
      ![After used to get data for Looker Studio, I delete it to override costs](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303956391-82ab2ecf-060a-47ef-9f9d-df845433a579.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025123Z&X-Amz-Expires=300&X-Amz-Signature=50db1c2114861291214cb7292069f7b5e4aa670e423a744e935a2720a2543559&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   7. Connection established between Looker Studio and AWS RDS with _etlworhshop_ database.
      ![Connection established between Looker Studio and AWS RDS with _etlworhshop_ database](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303961735-0d18940d-f7c2-47de-9276-2f5507cf3578.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025113Z&X-Amz-Expires=300&X-Amz-Signature=e54b85b9302ab7cdcf6a3c833ff6df074a300304d894a276151469f240e9625a&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   8. Ngrok is running.
      ![Evidence of Ngrok is running](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303951549-9f59a0ca-a9cc-4ce8-bc29-323ace774b9f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025056Z&X-Amz-Expires=300&X-Amz-Signature=c47891e041b5ba5c2e637319da001aa378a304cbaaeb31c256531277d347bf08&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   9. Connection with Local PostgreSQL.
      ![Config to connect Looker Studio with PostgreSQL](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303954422-0ca9ed14-6365-4792-b845-9c1ca3b9e116.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025048Z&X-Amz-Expires=300&X-Amz-Signature=5383c84d7063ce04cb5454423dbf4277ad23a1414400543a4c2a6d7c70d82127&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

   10. Using pre-commits.
      ![Using pre-commits](https://github-production-user-asset-6210df.s3.amazonaws.com/92474551/303961952-75f80c5f-381d-4bb1-9c04-00f94659f9ff.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20240212%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240212T025037Z&X-Amz-Expires=300&X-Amz-Signature=9d74de65bf0275b66ae5bbdc6cec360f51be0519072384319dc887d18fc2ed1a&X-Amz-SignedHeaders=host&actor_id=0&key_id=0&repo_id=0)

---
### My support resources

- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Github: [Workshop 001 - ETL Education Repository](https://github.com/dventep/workshop001_etl_education/tree/develop).
- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/github-icon.svg" alt="GitHub" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Gist: [Workshop 001 - ETL Education Gist](https://gist.github.com/dventep/579f1646c6d6011e4e8314fb85482eba).
- <img src="https://raw.githubusercontent.com/get-icon/geticon/fc0f660daee147afb4a56c64e12bde6486b73e39/icons/looker-icon.svg" alt="Looker Studio" width="21px" height="21px"> <img src="https://avatars.githubusercontent.com/u/92474551" alt="Me" width="21px" height="21px" style="border-radius: 50%"> Looker Studio: [Dashboard - Looker Studio](https://lookerstudio.google.com/reporting/7c98a50e-d58f-4e4e-a8e8-17a09b233513).
