## proposed improvements
1. Use .env and the python dotenv package to pass the configurations files as environment vars
   1. I feel like it's better do remove the defaults from config.py and put them in the .env file. This way missing config will end up breaking the deployment instead sooner rather than later.
2. dockerize the app for more reproducible environment
3. use pipenv or poetry for reproducible python environment
4. Extra class for the duplicated code of counting objects in CountDetectedObjects and ListDetectedObjects
5. Use dependency injection for connecting the components in the config.py
6. Create e2e tests based on user stories, eg:
   1. When uploading two images the output includes the sum of the objects in both images
7. Inline the unittests, that is put them next to the units that they are testing
8. Separate unittests from e2e tests by marking them with pytest. Add makefile targets for running unittest and e2e tests and all tests
9. Most of the readme.md should be inside the makefile
