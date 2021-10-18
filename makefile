build: clean
	# edit file "packaging/setup.cfg" and update version number
	pip3 install --upgrade build
	cd packaging && python3 -m build
	
test:
	pip3 install --upgrade twine
	cd packaging && python3 -m twine upload --repository testpypi dist/*
	pip3 install --upgrade -i https://test.pypi.org/simple/ --no-deps ojet

deliver:
	# edit file "packaging/setup.cfg" and update version number (remove suffix dev)
	cd packaging && python3 -m twine upload dist/*
	pip3 install --upgrade ojet

clean:
	rm -fr packaging/dist
