
# SQL Skill — Database Analysis Playbook

## 1. Understand Before Querying
- Always inspect the active database schema using `get_schema`.
- Use only tables and columns that actually exist.
- Identify primary keys, foreign keys, and relationships before joining tables.
- If the question is ambiguous, make a reasonable assumption and state it.

## 2. Query-Writing Guidelines
- Use SQLite-compatible SQL syntax.
- Use JOINs when information spans related tables.
- Use COUNT, SUM, AVG, MIN, and MAX for aggregations.
- Use GROUP BY for summaries and HAVING to filter aggregated results.
- Use DISTINCT when duplicate values must be removed.
- Use clear aliases for calculated columns.
- Use ORDER BY when ranking or sorting results.
- Use LIMIT for top-N questions.

## 3. Dates and Values
- Inspect how dates are stored before filtering or comparing them.
- If dates use ISO format (YYYY-MM-DD), string comparisons can be used for date ranges.
- Use SQLite date functions when appropriate.
- Check column types before comparing numbers, dates, and text.
- Handle NULL values explicitly when they affect the result.

## 4. Accuracy and Common Pitfalls
- Avoid duplicate counting caused by one-to-many JOINs.
- For averages, counts, and totals, choose the correct level of aggregation.
- Do not assume that a column's meaning or values are obvious from its name alone.
- Do not invent business rules, table relationships, or missing data.
- If the available schema cannot answer the question, explain why.

## 5. Workflow
1. Inspect the active schema using `get_schema`.
2. Map the user's question to relevant tables and columns.
3. Determine the required filters, joins, and aggregations.
4. Generate a SQLite SELECT query.
5. Execute it using `execute_sql`.
6. Validate the returned results and summarize them in plain English.

## 6. Safety
- Execute read-only queries only.
- Never INSERT, UPDATE, DELETE, DROP, ALTER, or modify database contents.
- Never execute multiple statements in one query.
- If a query fails, inspect the error and correct the SQL before retrying.

## 7. Response Style
- Answer the user's question directly.
- Include important numbers, names, and trends from the results.
- Explain assumptions or limitations when relevant.
- Do not claim results that were not returned by the database.