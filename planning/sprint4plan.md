**Sprint 4 goals:**

1. **ACID Transactions:**
   - **Ensures atomicity:**
     - **Goal:** Implement transaction management to ensure atomicity by batching queries into transactions that execute entirely or not at all.
     - **Evaluation Criteria:** Successful execution of transactions with rollback capabilities in case of failures, verified by test cases.
   - **Enforces consistency:**
     - **Goal:** Maintain database consistency using check constraints and assertions to prevent invalid data entry.
     - **Evaluation Criteria:** Implementation of check constraints and assertions to ensure data integrity.
   - **Isolates transactions:**
     - **Goal:** Analyze transactions to determine and set appropriate isolation levels to prevent concurrency issues.
     - **Evaluation Criteria:** Identification and application of suitable isolation levels for various transactions, with testing to confirm the absence of concurrency-related issues.
   - **Preserves durability:**
     - **Goal:** Ensure data durability by implementing manual recovery of a database from a log file.
     - **Evaluation Criteria:** Successful recovery of the database from a log file during testing scenarios simulating data loss.
       
2. **Advanced SQL:**
   - **Simplify Queries:**
     - **Goal:** Simplify a complex query by converting a sub-query into an outer join.
     - **Evaluation Criteria:** Successful simplification of complex queries, verified through testing and performance analysis.
   - **Use Triggers:**
     - **Goal:** Enforce consistency by adding triggers to queries.
     - **Evaluation Criteria:** Implementation of triggers that maintain data integrity and consistency, verified through testing.
   - **Embrace Ternary Logic:**
     - **Goal:** Incorporate NULLs into queries with ternary predicate logic.
     - **Evaluation Criteria:** Successful incorporation of NULLs and ternary logic into queries, verified through testing and ensuring correct query results.


---
