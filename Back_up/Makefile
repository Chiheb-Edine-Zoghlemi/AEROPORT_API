app_name = routes-api
build:
	@docker-compose build 
run:
	@docker-compose up -d 
kill:
	@echo 'Killing container...'
	@docker ps | grep $(app_name) | awk '{print $$1}' | xargs docker stop
