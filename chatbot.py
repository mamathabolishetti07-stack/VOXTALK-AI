from ollama import chat


def get_ai_response(
    messages,
    context="",
    language="English"
):

    system_message = f"""
You are VoxTalk AI, a friendly and helpful conversational assistant.

Answer the user in {language}.

Use the provided context when it is relevant.

If the question is related to the provided documents,
answer using the context.

If the required information is not available,
say that you do not know.

Keep your answers simple and clear.
"""

    if context:
        system_message += f"""

Relevant information from the knowledge base:

{context}
"""


    full_messages = [
        {
            "role": "system",
            "content": system_message
        }
    ] + messages


    response = chat(
        model="llama3.2",
        messages=full_messages
    )


    return response["message"]["content"]
