import requests


class NotionRequest:
    """
    Generate a Notion request object.
    Wraps Notion API endpoints for accessibility.
    """

    def __init__(
        self, integration_token, resource_type, resource_id, action_type, **kwargs
    ):
        """Instantiate NotionRequest object."""
        RESOURCE_TYPES = ["blocks", "databases", "pages", "users"]

        self.integration_token = integration_token
        if resource_type not in RESOURCE_TYPES:
            raise ValueError(
                f"Specified resource type must be one of: {RESOURCE_TYPES} received: {resource_type}."
            )
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.action_type = action_type
        for key, value in kwargs.items():
            setattr(self, key, value)

    def build_url(self):
        """Append parameters to build endpoint URL."""
        BASE_URL = "https://api.notion.com/v1"
        self.url = f"{BASE_URL}/{self.resource_type}/{self.resource_id}"
        if hasattr(self, "children") and self.children:
            self.url = f"{self.url}/children"
        return self.url

    def build_headers(self):
        """Create endpoint headers, applying user's integration token"""
        return {
            "Authorization": f"Bearer {self.integration_token}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-02-22",
        }

    def build_request_params(self):
        """Aggregate method calls for endpoint parameters into single method"""
        url = self.build_url()
        headers = self.build_headers()
        return url, headers

    def execute_request(self):
        """Make endpoint request based on request options."""
        url, headers = self.build_request_params()
        if self.action_type == "GET":
            self.request = requests.get(url, headers=headers)
            return self.request
        if self.action_type == "PATCH":
            self.request = requests.patch(url, self.data, headers=headers)
            return self.request
        if self.action_type == "DELETE":
            self.request = requests.delete(url, headers=headers)
            return self.request
