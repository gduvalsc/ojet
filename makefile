deliver:
	cd ojet && python3 setup.py clean
	cd ojet && rm -fr dist ojet*info
	cd ojet && python3 setup.py sdist upload
	cd ojet && rm -fr dist ojet*info
