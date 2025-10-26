import unittest
from markdown_blocks import (
    markdown_to_blocks,
    BlockType,
    block_to_blocktype,
)


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_paragraph(self):
        md = """
This is a paragraph block
"""
        blocktype = block_to_blocktype(md)
        self.assertEqual(BlockType.PARAGRAPH, blocktype)

    def test_block_to_blocktype_heading(self):
        md = """
# This is a heading with 1 hashtag

## This is a heading with 2 hashtags

### This is a heading with 3 hashtags

#### This is a heading with 4 hashtags

##### This is a heading with 5 hashtags

###### This is a heading with 6 hashtags
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        self.assertListEqual(
            [
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
                BlockType.HEADING,
            ],
            block_types,
        )

    def teste_block_to_blocktype_code(self):
        md = """
```This is a proper
code block```

```This is a wrong code block that opens but doesn't closes

This is a wrong code block that doesn't open but closes```
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        self.assertListEqual(
            block_types,
            [
                BlockType.CODE,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )

    def teste_block_to_blocktype_quote(self):
        md = """
>This is a proper
>quote block
>with 3 lines

>This should be
a paragraph block

This should also
>be a paragraph block
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        self.assertListEqual(
            block_types,
            [
                BlockType.QUOTE,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )

    def teste_block_to_blocktype_unordered_list(self):
        md = """
- This is a proper list block
- with 2 lines

-This is am improper list block because there is no space between the dash and the start of the item

- This should be a paragraph
because the second line doesn't start with '- '

Same as the previous test
- but the lines are swapped
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        self.assertListEqual(
            block_types,
            [
                BlockType.UNORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )

    def teste_block_to_blocktype_ordered_list(self):
        md = """
1. This is a proper ordered list block
2. with 2 lines

1.This is am improper list block because there is no space between the dot and the start of the item

1. This should be a paragraph
because the second line doesn't start with '2. '

This should be a paragraph
2. This should be a paragraph

2. This should be a paragraph

1. This should be a paragraph
- because of this
"""
        blocks = markdown_to_blocks(md)
        block_types = []
        for block in blocks:
            block_types.append(block_to_blocktype(block))
        self.assertListEqual(
            block_types,
            [
                BlockType.ORDERED_LIST,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
                BlockType.PARAGRAPH,
            ],
        )


if __name__ == "__main__":
    unittest.main()
