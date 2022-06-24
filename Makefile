lock_pip: requirements.txt
	test -d venv || echo "a virtual env needs to be installed in the venv directory before running this";
	. venv/bin/activate; pip freeze | xargs --no-run-if-empty pip uninstall -y;
	pip install -r requirements.txt;


