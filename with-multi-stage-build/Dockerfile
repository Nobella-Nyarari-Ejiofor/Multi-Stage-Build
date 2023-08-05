FROM python:3-slim AS build-env

COPY . /app
# Install the Python dependencies (if you have any)

WORKDIR /app

FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
WORKDIR /app
CMD ["python3" , "rock_paper_scissors2.py"]