


class DocumentProcessor():
    def __init__(self, chunk_size):
        self.chunk_size = chunk_size
        pass


    def process(self, text):
        clean_text = self.clean_text(text)

        return {
            "title": self.extract_title(text),
            "clean_text": clean_text,
            "metadata": self.get_metadata(text),
            "chunks": self.chunk_text(clean_text)
        }


    
    def clean_text(self, text):
        text = text.replace("\n", " ")
        text = " ".join(text.split())
        return text.strip()
    
    def extract_title(self, text):
        lines = text.split("\n")
        title = None
        for line in lines:
            if line.strip():
                title = line
                break
        if title:
            return title.strip()
        else:
            return "Untitled Document"
    
    def get_metadata(self, text):
        return {
            "word_count": len(text.split()),
            "char_count": len(text),
            "line_count": len(text.split("\n"))
        }
    
    def chunk_text(self, text):
        words = text.split()
        chunks = []

        for i in range(0, len(words), self.chunk_size):
            chunk = "".join(words[i:i+self.chunk_size])
            chunks.append(chunk)
        return chunks




