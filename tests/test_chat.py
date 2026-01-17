from app.schemas.schemas import Chat, Message, FullChat

# Test №1: Create chat
def test_create_chat(client, create_chat):
    response = client.post("/chats", json=create_chat())

    assert response.status_code == 200

    chat = Chat(**response.json())

    assert chat.title == "House chat"


# Test №2: Create messages
def test_create_messages(client, create_chat, create_message):
    response = client.post("/chats", json=create_chat())

    assert response.status_code == 200

    chat = Chat(**response.json())

    response_message = client.post(f"/chats/{chat.id}/messages", json=create_message())

    assert response_message.status_code == 200

    message = Message(**response_message.json())

    assert message.text == "Hello everyone!"


# Test №3: Get chat and last N messages
def test_get_chat_messages(client, create_chat, create_message):
    response = client.post("/chats", json=create_chat())

    assert response.status_code == 200

    chat = Chat(**response.json())

    for message in create_message(single=False):
        response_message = client.post(f"/chats/{chat.id}/messages", json=message)

        assert response_message.status_code == 200

    get_chat_messages = client.get(f"/chats/{chat.id}?limit=3")

    assert get_chat_messages.status_code == 200

    chat_data = FullChat(**get_chat_messages.json())

    assert chat_data.chat.title == "House chat"

    assert len(chat_data.messages) == 3

    assert chat_data.messages[0].created_at > chat_data.messages[1].created_at > chat_data.messages[2].created_at


# Test №4: Delete chat and messages
def test_delete_chat(client, create_chat, create_message):
    response = client.post("/chats", json=create_chat())

    assert response.status_code == 200

    chat = Chat(**response.json())

    for message in create_message(single=False):
        response_message = client.post(f"/chats/{chat.id}/messages", json=message)

        assert response_message.status_code == 200

    delete_response = client.delete(f"/chats/{chat.id}")

    assert delete_response.status_code == 204


# Test №5: Create chat with empty title
def test_create_empty_title_chat(client):
    response = client.post("/chats", json={"title": "              "})

    assert response.status_code == 422


# Test №6: Create message in nonexistent chat
def test_create_message_in_nonexistent_chat(client, create_message):
    response_message = client.post(f"/chats/{100}/messages", json=create_message())
    
    assert response_message.status_code == 404


# Test №7: Get a nonexistent chat
def get_noneexistent_chat(client):
    response = client.get(f"/chats/{100}")

    assert response.status_code == 404
