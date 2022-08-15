class HealthCheck:
    def get(self) -> dict[str, str]:
        return {"message": "Hello World"}
