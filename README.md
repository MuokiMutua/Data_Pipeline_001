# Simple Data Pipeline with Python, NiFi, PostgreSQL & Docker  
<img width="1117" height="625" alt="image" src="https://github.com/user-attachments/assets/8dce5ca4-a57e-46b6-87c1-33d8d816c146" />


## 📌 Project Overview  
This project demonstrates a **simple end-to-end data pipeline** that simulates real-world data ingestion, transformation, and storage — all orchestrated inside **Docker containers** for easy setup and portability.  

---

## 🔹 1. Data Generation (Python + Faker)  
- A Python script generates synthetic data using the **Faker library** with the following fields:  
  - `name`  
  - `email`  
  - `product_name`  
  - `price`  
  - `product_date`  
- New CSV files are created every **5 seconds** and saved in the `input` directory.  
- File creation runs continuously until the script is **manually stopped**.  

---

## 🔹 2. Apache NiFi Pipeline  
- **First Flow**  
  - **GetFile Processor** → Reads CSVs from the `input` directory.  
  - **PutFile Processor** → Moves them into the `output` directory.  

- **Second Flow**  
  - **GetFile Processor** → Reads CSVs from the `output` directory.  
  - **PutDatabaseRecord Processor** → Inserts records into a **PostgreSQL database**.  

---

## 🔹 3. Containerized Services (Docker Compose)  
All components run in containers defined in `docker-compose.yml`:  

- **PostgreSQL** – Relational database for storing ingested records.  
- **pgAdmin4** – GUI for managing PostgreSQL.  
- **Apache NiFi** – Data pipeline orchestration & processing.  
- **Elasticsearch** – Indexing and searching pipeline logs/data.  
- **Kibana** – Visualization and monitoring of Elasticsearch data.  



### ScreenShoots
<img width="1448" height="382" alt="image" src="https://github.com/user-attachments/assets/5b244e5a-94c6-4002-92b4-38e66d90f048" />
<img width="1234" height="610" alt="image" src="https://github.com/user-attachments/assets/3c5bcbac-fdde-4c63-b1ee-4479010e8a1d" />
<img width="1908" height="855" alt="image" src="https://github.com/user-attachments/assets/230df5c4-e0f2-4235-93ec-68f2d0e25132" />




