**Sprint 3 goals:**

1. **Basic Security:**
   - **Manages access:**
     - **Goal:** Implement an access control system to manage data access with users, ensuring privileges are appropriately set and can be revoked.
     - **Evaluation Criteria:** Successful creation and testing of user roles with appropriate privileges, with tests confirming that unauthorized access is prevented.
   - **Creates views:**
     - **Goal:** Create and manage database views that restrict data visibility and allow for controlled data manipulation. Prehaps a View specific for end users.
     - **Evaluation Criteria:** Successful creation of views with specific privileges and verification through testing that views can insert or delete data from the base tables without compromising security.

2. **ACID Transactions:**
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

3. **Advanced Conceptual Design:**
   - **Uses inheritance notions:**
     - **Goal:** Incorporate inheritance and weak entity sets into the database design to model real-world relationships more accurately.
     - **Evaluation Criteria:** Design and implementation of an ERD that effectively uses inheritance and weak entity sets, validated by testing.
   - **Evaluates quality:**
     - **Goal:** Evaluate an ERD concerning a canonical set of design principles to ensure a high-quality design.
     - **Evaluation Criteria:** Peer review and critique of the ERD based on established design principles, followed by necessary revisions to meet quality standards.

4. **Advanced Relational Design:**
   - **Connects conceptual-logical:**
     - **Goal:** Translate functional dependencies (FDs) from an ERD and reverse engineer the relations back into an ERD.
     - **Evaluation Criteria:** Successful translation and reverse engineering of FDs, with verification through comparison with the original ERD.
   - **Simplifies FD's:**
     - **Goal:** Calculate a minimal basis for a set of FDs to ensure a simple and efficient database design.
     - **Evaluation Criteria:** Identification and implementation of a minimal basis for FDs, confirmed through testing and peer review.
   - **Preserves FD's:**
     - **Goal:** Check if a decomposition preserves FDs and decompose relations into third normal form (3NF) when appropriate.
     - **Evaluation Criteria:** Successful decomposition into 3NF with verification that FDs are preserved, confirmed by testing and peer review.
   - **Preserves MVD's:**
     - **Goal:** Check if a decomposition preserves multi-value dependencies (MVDs) and decompose relations into fourth normal form (4NF) when appropriate.
     - **Evaluation Criteria:** Successful decomposition into 4NF with verification that MVDs are preserved, confirmed by testing and peer review.

---


