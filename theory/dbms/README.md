# Databases

`Weeks 11–13` of the prep plan.

| # | File | Topics |
|---|---|---|
| 01 | [Fundamentals & SQL](01-fundamentals-and-sql.md) | keys, joins, normalisation, ACID overview, SQL vs NoSQL |
| 02 | [Transactions & Concurrency](02-transactions-and-concurrency.md) | WAL, isolation levels, anomalies, 2PL, deadlock, MVCC, optimistic vs pessimistic |
| 03 | [Indexing & Performance](03-indexing-and-performance.md) | B+ trees, clustered indexes, leftmost prefix, query plans, denormalisation, CDC |
| 04 | [ER Modelling & Schema Design](04-er-modelling-and-schema-design.md) | ER diagrams, cardinality, ER→relational mapping, keys, NULL semantics, constraints, views/triggers |
| 05 | [Query Processing & NoSQL](05-query-processing-and-nosql.md) | optimiser, join algorithms, EXPLAIN, why indexes are ignored, partitioning, NoSQL modelling, quorum, backup/RPO/RTO |

## SQL practice

[LeetCode Top SQL 50](https://leetcode.com/studyplan/top-sql-50/) — work through it across Weeks 11–13. SQL rounds are common at product companies and are usually free marks if you've practised.

## The five that come up most

1. **Isolation levels** — the table, plus a concrete interleaving for each anomaly
2. **Indexing** — leftmost prefix rule, and why an index might be ignored
3. **Normalisation** — 2NF vs 3NF with an example violation of each
4. **MVCC** — readers don't block writers, and the `VACUUM` consequence
5. **Joins** — write "customers with no orders" without hesitating

## Connections

| DBMS concept | Where it reappears |
|---|---|
| WAL + `fsync` | [OS: page cache](../os/05-storage-io-and-linux.md) — why `write()` isn't durable |
| B+ tree vs LSM | [System Design: databases](../system-design/04-databases.md) |
| Deadlock + lock ordering | [OS: concurrency](../os/03-concurrency.md) — same four conditions |
| Optimistic concurrency | [System Design: coordination](../system-design/07-coordination-and-consistency.md) — the alternative to distributed locks |
| CDC | [System Design: messaging](../system-design/06-messaging-and-kafka.md) |
