# README – ElastiCache Query Caching Project

## **Team Members**
- **Zeel Thakker (en7825)**
- **Aryan (dc9128)**

---

## **Overview**
High traffic causes database response times to increase dramatically (for example, from ~50 ms to over 2 seconds).  
This project implements **Amazon ElastiCache (Redis)** as a query caching layer to reduce repeated reads on the database.

By caching frequently accessed data, the system achieves:
- **60–80% reduction in database load**
- **Sub-10 ms response times** for cached queries
- **More stable performance during traffic spikes**

---

## **Problem**
E-commerce systems frequently fetch product catalog data, shopping cart details, and user session information.  
When thousands of users request the same data repeatedly:

- The relational database becomes a bottleneck  
- Latency spikes under load  
- Read replicas and indexes become insufficient  
- User experience degrades as APIs slow down  

A caching layer is required to eliminate redundant reads and increase scalability.

---

## **Solution**
We implemented a **Redis cache-aside architecture** using Amazon ElastiCache.

### Key Benefits
- Sub-10 ms cached responses  
- Automatic TTL expiration  
- Database queried only on cache misses  
- Seamless integration with Amazon RDS  
- Scales easily as traffic increases  

### Cache-Aside Workflow
1. Application checks Redis for the requested key.  
2. **Cache Hit →** Return result immediately.  
3. **Cache Miss →** Query RDS → Store result in Redis → Return response.  
4. TTL ensures outdated values refresh automatically.

---

## **Technologies Used**
- **Amazon ElastiCache (Redis)** — Cache layer  
- **Amazon RDS** — Primary database  
- **Amazon EC2** — Backend hosting  
- **AWS VPC** — Networking, routing, and security  
- **AWS CLI v2 / CloudShell** — Deployment and management  

---

## **Setup Instructions**

### 1. Create an Amazon RDS Instance
- Take note of DB endpoint & credentials  
- Ensure RDS is in private subnets (recommended)

### 2. Deploy an ElastiCache Redis Cluster
- Place Redis in private subnets  
- Allow incoming traffic only from EC2 Security Group  
- Default port: **6379**

### 3. Launch an EC2 Instance
Install dependencies and configure environment variables:



## **How It Works**
1. Application checks Redis for cached data.  
2. **Cache hit →** returns data in under 10 ms.  
3. **Cache miss →** queries the database, stores the result in Redis, then returns the response.

---

## **Performance Gains**
- Faster API response times  
- Significant reduction in database load  
- Improved scalability during high traffic surges  

---

## **Troubleshooting**
- Redis unreachable → verify VPC security group rules  
- High cache miss rate → extend TTL value  
- Redis evicting keys → upgrade Redis memory/node size  
- Slow DB queries → add proper indexing  

---

## **Estimated Cost**
Estimated AWS test environment cost: **$50–$100/month** using t3.micro instances.





