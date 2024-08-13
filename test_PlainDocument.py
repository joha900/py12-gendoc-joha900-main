from test_GenericDocument import GenericDocument
from test_PartType import PartType


class PlainDocument(GenericDocument):
    def create_part(self, part_type, content):
        if part_type == PartType.HEADING1:
            return f"{content}\n{'=' * len(content)}"
        elif part_type == PartType.HEADING2:
            return f"{content}\n{'-' * len(content)}"
        elif part_type == PartType.HEADING3:
            return f"{content}\n{'~' * len(content)}"
        elif part_type == PartType.PARAGRAPH:
            return content
        elif part_type == PartType.CODEBLOCK:
            return f"{content}\n{'-' * len(content)}"
        else:
            raise ValueError(f"Unsupported part type: {part_type}")
