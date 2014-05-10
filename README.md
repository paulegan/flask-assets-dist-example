To run:

	python manage.py runserver
	curl http://127.0.0.1:5000/

To build distribution:

	python setup.py bdist
	tar -tf dist/*.tar.gz

Test dist app:

	python setup.py install --root dist/root
	APP_CONFIG=$PWD/dist/root/etc/myapp/prod.cfg PYTHONPATH=`find dist -name site-packages` dist/root/usr/bin/myapp-manage runserver
