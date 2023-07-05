build:
	sudo docker-compose build

up:
	sudo docker-compose up -d

down:
	sudo docker-compose down

restart:
	sudo docker-compose restart

stop:
	sudo docker-compose stop

clean:
	sudo docker-compose down -v --rmi all

.PHONY: build up down restart stop clean
