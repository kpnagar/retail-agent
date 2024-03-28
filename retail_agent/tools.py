from semantic_router.utils import llm


def chitchat(user_query: str) -> str:
    """
    Do simple chitchat with user respectfully and honestly.

    :param user_query: The query provided by the user.
    :type user_query: str
    :return: Respectful response of user's query in string format
    """
    return llm.llm(user_query)
