# README – ElastiCache Query Caching Project

## **Team Members**
- **Zeel Thakker (en7825)**
- **Aryan (dc9128)**

---

## **Overview**
High traffic causes database response times to increase dramatically (from ~50 ms to over 2 seconds).  
This project uses **Amazon ElastiCache (Redis)** to cache frequently accessed queries, reducing database load by **60–80%** and returning cached results in **under 10 ms**.

---

## **Problem**
E-commerce applications repeatedly query product catalog data, user sessions, and shopping cart details.  
These repeated requests overload the primary database, and traditional optimizations such as indexing and read replicas become insufficient as traffic scales.

---

## **Solution**
A **Redis cache-aside layer** with TTL expiration is implemented to improve performance:

- Sub-10 ms cached responses  
- 60–80% reduction in database load  
- Seamless integration with Amazon RDS  
- Scalable and fault-tolerant design using Amazon ElastiCache  

---


## **Technologies**
- **Amazon ElastiCache (Redis)**
- **Amazon RDS**
- **Amazon EC2**
- **AWS VPC**
- **AWS CLI v2 / CloudShell**

---

## **Setup**
1. Create an Amazon RDS instance and note the endpoint + credentials.  
2. Deploy an ElastiCache Redis cluster in private subnets.  
3. Configure your EC2 application with environment variables:  
   - `DB_HOST`, `DB_USER`, `DB_PASSWORD`  
   - `REDIS_HOST`, `REDIS_PORT`, `CACHE_TTL`  
4. Start the application using:  
   - `npm start`  
   - or `python app.py`

---

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




