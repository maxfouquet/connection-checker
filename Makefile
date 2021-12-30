build:
	docker build -t connection-checker .

run:
    docker run -p 5001:5000 -d connection-checker