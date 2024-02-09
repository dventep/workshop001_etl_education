# workshop001_etl_education

Repository of workshop001 developed.

Link Power BI

https://app.powerbi.com/groups/me/reports/932696b5-e5f6-4c88-a969-1101609ebee8?pbi_source=desktop

### Step by step for execution

Following instructions are based on Windows 11 OS:

1. To have the required tools for the execution of the repository correctly, so it's necessary to have the following:

   - **Python** _(Optional: used version 3.10.3)_.
   - **Docker** or **Docker Desktop** _(Optional: used version 20.10.21)_.
   - **Git** _(Optional: used version 2.43.0)_.

   In this case, I use Docker to deploy PostgreSQL _(Port 5432)_ and PgAdmin _(Port 80)_ with host _localhost_.
2. Let's deploy docker's containers.

   1. Turn on **Docker** or **Docker Desktop**.
   2. To do this, from root folder we must go to the folder: _./code/script/_
   3. When we stay in that folder, we execute the code: `<code>`docker-compose up`</code>`

      > __[ ℹ️ ].__ If we want to eliminate the containers, from root folder execute the code _(For Windows)_: `<code>`/code/script/dockerdelete.ps1`</code>`.
      
   4. Return to the root folder.
3. Create virtual environment for Python:

   `<code>`python -m venv venv`</code>`
4. Choose venv as Kernel for .ipynb files in the folder **notebooks**.

   In each file in **notebooks**, there is a code to install required libraries if necessary.
5. Explorate the notebooks in the folder **notebooks**. I have two notebooks: _load_csv_file_ and _EDA_report_.

    - **load_csv_file:** Its objective is take the raw dataset in a csv file and load it in a PosgreSQL database within the **raw_applicant** table.
    - **eda_report:** Its objective is take data of **raw_applicant**, explore, transform, analyze and load it in the same database within **applicant** table.

    > __[ ℹ️ ].__ To execute in order, let's start with **load_csv_file** and later **eda_report**.

