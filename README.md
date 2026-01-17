**Project launch**

In order to launch the project, follow the steps below:

1) Find the file ".env.template" and remove ".template" from the name of the file
2) Inside this file set the environment variables
   - **POSTGRES_USER** - PostgreSQL user
   - **POSTGRES_PASSWORD** - PostgreSQL user's password
   - **POSTGRES_DB** - name of selected database
   - **POSTGRES_PORT** - PostgreSQL port
3) In terminal run the following commands:
   ```powershell
   docker compose build
   docker compose up
   ```
4) Open:
   ```http
   http://0.0.0.0:8011/docs
   ```
