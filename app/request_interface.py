import json
from app.notion_request import NotionRequest


def get_block(integration_token, block_id):
    """Request a Notion block."""
    request = NotionRequest(integration_token, "blocks", block_id, "GET")
    response = request.execute_request()
    if response.status_code < 200 or response.status_code >= 300:
        raise ValueError(f"Error {response.status_code}: {response.reason}")
    return response


def delete_block(integration_token: str, block_id: str):
    """Delete the target Notion block."""
    request = NotionRequest(integration_token, "blocks", block_id, "DELETE")
    response = request.execute_request()
    if response.status_code < 200 or response.status_code >= 300:
        raise ValueError(f"Error {response.status_code}: {response.reason}")
    return response


def append_paragraph(integration_token, parent_id, paragraph_text, paragraph_link=None):
    """Add a basic Notion paragraph block as a child to the parent block."""
    paragraph_content = {
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {"content": paragraph_text, "link": paragraph_link},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": paragraph_text,
                            "href": None,
                        }
                    ],
                    "color": "default",
                },
            }
        ]
    }
    request = NotionRequest(
        integration_token,
        "blocks",
        parent_id,
        "PATCH",
        data=json.dumps(paragraph_content),
        children=True,
    )
    response = request.execute_request()
    if response.status_code < 200 or response.status_code >= 300:
        raise ValueError(f"Error {response.status_code}: {response.reason}")
    return response


def update_paragraph(
    integration_token: str, parent_id: str, paragraph_text: str, paragraph_link=None
):
    """Update content of target Notion paragraph block."""
    paragraph_content = {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [
                {
                    "type": "text",
                    "text": {"content": paragraph_text, "link": paragraph_link},
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default",
                    },
                    "plain_text": paragraph_text,
                    "href": None,
                }
            ],
            "color": "default",
        },
    }
    request = NotionRequest(
        integration_token,
        "blocks",
        parent_id,
        "PATCH",
        data=json.dumps(paragraph_content),
        children=False,
    )
    response = request.execute_request()
    if response.status_code < 200 or response.status_code >= 300:
        raise ValueError(f"Error {response.status_code}: {response.reason}")
    return response
