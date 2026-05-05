from app.services.document_processor import DocumentProcessor

def test_document_processor_basic():
    processor = DocumentProcessor(chunk_size=10)

    sample_text = """
    This is a test document.
    It has multiple sentences.
    We want to verify processing works correctly.
    """

    result = processor.process(sample_text)

    # Structure checks
    assert "title" in result
    assert "clean_text" in result
    assert "metadata" in result
    assert "chunks" in result

    # Content checks
    assert result["metadata"]["word_count"] > 0
    assert len(result["chunks"]) > 0
    assert isinstance(result["chunks"], list)

def test_empty_input():
    processor = DocumentProcessor(chunk_size=10)

    result = processor.process("")

    assert result["metadata"]["word_count"] == 0