run_postgres:
	docker rm -f test-postgres
	docker run --name test-postgres --rm --net host -e POSTGRES_USER=count_user -e POSTGRES_PASSWORD=notsosecretpassword -e POSTGRES_DB=count_db -d postgres


lock_pip: requirements.txt
	test -d venv || (echo "a virtual env needs to be installed in the venv directory before running this command; consider running 'python3 -m venv venv' " && exit 1);
	. venv/bin/activate; pip freeze | xargs --no-run-if-empty pip uninstall -y;
	pip install -r requirements.txt;


