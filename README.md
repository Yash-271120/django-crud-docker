# NOTE: DO NOT FORK THIS REPOSITORY. CLONE AND SETUP A STANDALONE REPOSITORY.

# TO run Locally
1. Clone this repository
2. create a `.env` file with content - ADBREW_CODEBASE_PATH="{path_to_repository}/test/src" OR  run `export ADBREW_CODEBASE_PATH="{path_to_repository}/test/src"`
3. run `docker compose up -d` OR run `docker compose up --watch` to run in development mode
4. frontend will be live at `http://localhost:3000` and backend will be live at `http://localhost:8000`


# Structure
In side the main app folder(rest) there is a todo package that will handle all the business logic required for the todo app. If required we can add further package that will encapsulate their own business logic.
