**Project launch**

In order to launch the project, follow the steps below:

1) Find the file ".env.template" and remove ".template" from the name of the file
2) Inside this file set the environment variables
   - **POSTGRES_USER** - PostgreSQL user
   - **POSTGRES_PASSWORD** - PostgreSQL user's password
   - **POSTGRES_DB** - name of selected database
   - **POSTGRES_EXT_PORT** - PostgreSQL external port
3) In terminal run the following commands:
   ```powershell
   docker compose build
   docker compose up
   ```
4) Open:
   ```http
   http://127.0.0.1:8011/docs
   ```

**Launch tests**  

In order to launch tests, after setting environment variables above, type in terminal (we need to create environment and install all dependencies):

```powershell
python -m venv venv
python venv\Scripts\activate
pip install -r requirements.txt
pytest -v --disable-pytest-warnings
```
