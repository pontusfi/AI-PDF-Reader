class LLMService:
    "MOCK LLM so far"

    def __init__(self):
        pass

    def summarize_document(self, document: dict) -> dict:
        text = document["clean_text"]

        # simple heuristic "fake LLM"
        words = text.split()

        summary = " ".join(words[:50]) + "..."

        key_points = [
            "Document contains structured content",
            "Text has been preprocessed and chunked",
            "Ready for LLM analysis pipeline"
        ]

        return {
            "title": document.get("title"),
            "summary": summary,
            "key_points": key_points
        }