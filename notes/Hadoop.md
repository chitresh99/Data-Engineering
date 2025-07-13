## Hadoop and Big Data Ecosystem Notes

Hadoop is a powerful distributed framework designed for large-scale data processing. It enables scalable, reliable, and fault-tolerant storage and computation across clusters of machines.

### Hadoop Design Philosophy

* **Architectural Thinking**: Designing a Hadoop cluster involves planning storage layout, node responsibilities, data replication, and fault tolerance.
* **Inspired by Google**:

  * **HDFS** is derived from **GFS (Google File System)**.
  * **MapReduce** is derived from **Google MapReduce (GMR)**.

### 1. What is a File System?

A file system is a method used by an operating system or platform to store, organize, and retrieve data.

**Examples**:

* Local: NTFS, EXT4
* Distributed: HDFS, S3, CephFS

### 2. What is a Block?

A block is the smallest unit of data storage in a file system. Large files are split into blocks for efficient storage and access.

**Block Size Examples**:

* NTFS: 16 KB
* EXT: 512 KB
* HDFS: Configurable (typically 64 MB / 128 MB / 256 MB)

### 3. Client and Server

* **Client**: Sends a request.
* **Server**: Responds to the request.

This model is fundamental to web applications, APIs, databases, and distributed systems.

### 4. Types of File Systems

* **Standalone File Systems**: Used on a single machine (e.g., NTFS, EXT4)
* **Distributed File Systems**: Data is stored across multiple machines (e.g., HDFS, Amazon S3, CephFS)

### 5. Types of Distributed Systems

* **Master-Slave Architecture**:

  * A single master coordinates multiple slave nodes.
  * Example: Hadoop (HDFS)

* **Peer-to-Peer (P2P)**:

  * All nodes are equal and can communicate directly.
  * Example: Cassandra

### 6. What is a Process?

A process is a program in execution. It includes the program code and its current activity (registers, stack, heap, etc.).

### 7. What is a Daemon Process?

A daemon is a background process that runs continuously to handle system-level tasks.

**Examples**: sshd, httpd, cron

### 8. Cluster vs Node

* **Node**: An individual physical or virtual machine in a network.
* **Cluster**: A collection of nodes working together as a single system.

### 9. What is a Client API?

A Client API (Application Programming Interface) is a set of functions and tools that allow developers to interact with a system or service.

**Example**: Accessing HDFS using the Hadoop Java Client API.

## Overview of the Hadoop Ecosystem

* **HDFS**: Hadoop Distributed File System. Stores large data files across multiple nodes. Inspired by GFS.
* **MapReduce**: Programming model for distributed processing. Based on Google’s MapReduce paper.
* **Hive**: SQL-like query engine for Hadoop. Developed by Facebook. Converts SQL to Java MapReduce jobs.
* **Pig**: Data flow scripting platform using Pig Latin. Suitable for procedural transformations.
* **Sqoop**: Tool to import/export data between Hadoop and relational databases (developed by Yahoo).
* **Flume**: Distributed service for collecting, aggregating, and transporting large volumes of log data in real-time.
* **Oozie**: Workflow scheduler system to manage Hadoop jobs. Like cron but for Hadoop (developed by Yahoo).
* **HBase**: Columnar NoSQL database that runs on top of HDFS. Used for real-time read/write access.
* **Mahout**: Machine learning library for Hadoop. Includes algorithms for clustering, classification, and collaborative filtering.

### Integration Principles

* Hadoop ecosystem components are **loosely coupled**.
* This allows seamless integration of tools, services, and external systems.
* **Storage Layer**: HDFS, HBase
* **Processing Layer**: MapReduce, Pig, Hive
* **Ingestion Layer**: Sqoop, Flume
* **Scheduling**: Oozie
* **Analytics/ML**: Mahout

### Development Tip: Single-Node Hadoop Cluster

For learning and development:

* Start with a **single-node Hadoop cluster** setup.
* Avoid multi-node installation unless you're simulating real-world deployments or working on advanced use cases.

### Parallel Data Distribution

* GFS (and by extension HDFS) distributes data **before writing** to disk.
* Enables **parallel processing**, a key advantage of Hadoop-based systems.
