HUGO?=hugo
MSG?='rebuilding site $(date)'


help:
	@echo 'Makefile for hugo Web site	                                             '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make hugo                           (re)generate the web site          '
	@echo '   make publish                        generate using production settings '
	@echo '   make server [PORT=1313]             serve site at http://localhost:1313'
	@echo '                                                                          '

hugo:
	@echo -e '\e[1;34mBCompiling Hugo!!! $<\e[0m'
	$(HUGO)

server:
	$(HUGO) server

publish: hugo
	@echo 'Deploying updates to GitHub...'
	git add .
	git commit -m $(MSG)
	git push origin master
