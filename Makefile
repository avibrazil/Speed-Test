changelog:
	f1=`mktemp`; \
	f2=`mktemp`; \
	git tag --sort=-committerdate | tee "$$f1" | sed -e 1d > "$$f2"; \
	paste "$$f1" "$$f2" | sed -e 's|	|...|g' | while read range; do echo; echo "## $$range"; git log '--pretty=format:* %s' "$$range"; done; \
	rm "$$f1" "$$f2"

tgz:
	cd ..; \
	tar --exclude-vcs --exclude=.ipynb_checkpoints -czvf openspeedtest-1.5.tar.gz openspeedtest

rpm: tgz
	# RPM will be generated in ~/rpmbuild/RPMS/noarch
	mv ../openspeedtest-1.5.tar.gz ${HOME}/rpmbuild/SOURCES/; \
	rpmbuild -ba --build-in-place openspeedtest.spec
