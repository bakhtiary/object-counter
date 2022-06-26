## proposed improvements
1. Most of the readme.md should be inside the makefile. One target start_local_server should start everything (the dbs)
2. Use .env and the python dotenv package to pass the configurations files as environment vars
   1. I feel like it's better do remove the defaults from config.py and put them in the .env file. This way missing config will end up breaking the deployment instead sooner rather than later.
3. Use docker compose for a more declarative approach to launching the docker containers
4. use pyenv to install a specific base python. Currently the build breaks if we use python 3.10
5. use pipenv or poetry for reproducible python environment
6. dockerize the app for more reproducible environment
7. Extra class for the duplicated code of counting objects in CountDetectedObjects and ListDetectedObjects
8. Use dependency injection for connecting the components in the config.py
9. Create e2e tests based on user stories, eg:
   1. When uploading two images the output includes the sum of the objects in both images
10. Inline the unittests, that is put them next to the units that they are testing
11. Separate unittests from e2e tests by marking them with pytest. Add makefile targets for running unittest and e2e tests and all tests
12. The way we select between PROD and DEV environments seems brittle. Maybe if a wrong environment is entered we get a wierd message which is hard to debug

