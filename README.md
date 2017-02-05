# Integration Tests for FullyStacked using Docker-Compose
E2E Tests using Docker-compose for Django app. 

## Run Tests
1. Build a recent docker image of fullystacked
2. `cd integration-tests`
3. `./test.sh`

If you encounter errors try:
1. `docker-compose kill`
2. `docker-compose rm`