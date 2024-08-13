from abc import ABC, abstractmethod
from test_PartType import PartType


class GenericDocument(ABC):
    def __init__(self):
        self._document_parts = []

    def __getitem__(self, index):
        return self._document_parts[index]

    def __len__(self):
        return len(self._document_parts)

    def add_heading1(self, text: str):
        self._document_parts.append((PartType.HEADING1, text))
        return self

    def add_heading2(self, text: str):
        self._document_parts.append((PartType.HEADING2, text))
        return self

    def add_heading3(self, text: str):
        self._document_parts.append((PartType.HEADING3, text))
        return self

    def add_paragraph(self, text: str):
        self._document_parts.append((PartType.PARAGRAPH, text))
        return self

    def add_codeblock(self, text: str):
        self._document_parts.append((PartType.CODEBLOCK, text))
        return self

    def merge_indices(self, dst_index: int, *src_indices, sep="\n"):
        if dst_index in src_indices:
            raise ValueError("Destination index cannot be in source indices.")

        src_indices = sorted(set(src_indices))
        dst_part_type, dst_text = self._document_parts[dst_index]

        for src_index in reversed(src_indices):
            src_part_type, src_text = self._document_parts[src_index]
            dst_text += sep + src_text
            del self._document_parts[src_index]

        self._document_parts[dst_index] = (dst_part_type, dst_text)
        return self

    def merge_consecutive(self, part_type: PartType, sep="\n"):
        i = 0
        while i < len(self._document_parts) - 1:
            if (
                self._document_parts[i][0] == part_type
                and self._document_parts[i + 1][0] == part_type
            ):
                self._document_parts[i] = (
                    part_type,
                    self._document_parts[i][1] + sep + self._document_parts[i + 1][1],
                )
                del self._document_parts[i + 1]
            else:
                i += 1
        return self

    @abstractmethod
    def render_paragraph(self, text: str) -> str:
        pass

    def render(self) -> str:
        result = ""
        for part_type, text in self._document_parts:
            if part_type == PartType.HEADING1 and hasattr(self, "render_heading1"):
                part_result = getattr(self, "render_heading1")(text)
            elif part_type == PartType.HEADING2 and hasattr(self, "render_heading2"):
                part_result = getattr(self, "render_heading2")(text)
            elif part_type == PartType.HEADING3 and hasattr(self, "render_heading3"):
                part_result = getattr(self, "render_heading3")(text)
            elif part_type == PartType.CODEBLOCK and hasattr(self, "render_codeblock"):
                part_result = getattr(self, "render_codeblock")(text)
            else:
                part_result = self.render_paragraph(text)
            result += part_result
        return result
