import pytest
from app.notion_request import NotionRequest

# This could be more succint by generating the test data programmatically
request_data = [
    (
        "integrationabc123",
        "blocks",
        "resourcedef456",
        "GET",
        False,
        "",
        "https://api.notion.com/v1/blocks/resourcedef456",
    ),
    (
        "integrationabc123",
        "databases",
        "resourceghi789",
        "POST",
        False,
        "",
        "https://api.notion.com/v1/databases/resourceghi789",
    ),
    (
        "integrationabc123",
        "pages",
        "resourcejkl012",
        "PATCH",
        False,
        "",
        "https://api.notion.com/v1/pages/resourcejkl012",
    ),
    (
        "integrationabc123",
        "pages",
        "resourcejkl012",
        "PUT",
        False,
        "",
        "https://api.notion.com/v1/pages/resourcejkl012",
    ),
]


@pytest.mark.parametrize(
    "integration_token, resource_type , resource_id, action_type, children, data, expected_url",
    request_data,
)
def test_build_url(
    integration_token,
    resource_type,
    resource_id,
    action_type,
    children,
    data,
    expected_url,
):
    request = NotionRequest(
        integration_token,
        resource_type,
        resource_id,
        action_type,
        children=children,
        data=data,
    )
    assert request.build_url() == expected_url
