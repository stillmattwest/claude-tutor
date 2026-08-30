# Mastertrack: Professional Python web development

# Current item: C1 Command-line Python (not started)

## Out of scope

- This track does not guarantee a job.
- It does not cover front-end JavaScript frameworks or mobile development.

## Item C1: Command-line Python
**Type:** curriculum
**Start point:** Can open a terminal; has never programmed.
**End goal:** Writes small, well-structured command-line programs with functions, modules, and tests.

### C1.1 Writing and running scripts
**Start point:** Can use a terminal.
**End goal:** Writes and runs a multi-function script.

### C1.2 Project structure and modules
**Start point:** Can write a single-file script.
**End goal:** Splits code across modules and runs it as a package.

### C1.3 Tests with pytest
**Start point:** Has a multi-module project.
**End goal:** Writes passing pytest tests for their functions.

## Item C2: Relational databases with PostgreSQL
**Type:** curriculum
**Start point:** Can write tested command-line Python.
**End goal:** Designs a normalized schema and queries it with SQL.

### C2.1 Tables, rows, and SELECT
**Start point:** No database experience.
**End goal:** Creates tables and runs SELECT queries with filters and joins.

### C2.2 Schema design
**Start point:** Can query a single table.
**End goal:** Designs a small normalized multi-table schema.

### C2.3 Talking to a database from Python
**Start point:** Can write SQL by hand.
**End goal:** Runs parameterized queries from a Python program.

## Item M1: Inventory CLI
**Type:** milestone
**Duration:** ~1 week
**Uses:** C1, C2
**Start point:** Can write tested Python and query PostgreSQL.
**End goal:** A command-line inventory tool backed by a PostgreSQL database, built from scratch.

### Steps
1. Design the schema.
2. Build the CLI commands.
3. Add tests for the core logic.

## Item C3: Web apps with Flask
**Type:** curriculum
**Start point:** Can build a tested CLI backed by a database.
**End goal:** Builds a server-rendered Flask app backed by PostgreSQL.

### C3.1 Routes and templates
**Start point:** No web experience.
**End goal:** Renders HTML from templates across several routes.

### C3.2 Forms and validation
**Start point:** Can render templates.
**End goal:** Handles and validates form submissions.

### C3.3 Connecting the database
**Start point:** Can handle forms.
**End goal:** Reads and writes the PostgreSQL database from routes.

## Item Capstone: Team task tracker
**Type:** capstone
**Duration:** ~2–3 weeks
**Uses:** C1, C2, C3
**Start point:** Can build a database-backed Flask app.
**End goal:** A deployed, tested task-tracking web app that other people can sign up for and use.

### Steps
1. Model the domain and schema.
2. Build the web app.
3. Test and deploy it.
