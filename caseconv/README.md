# caseconv

A tiny, dependency-free helper to convert identifiers between
**snake_case**, **kebab-case**, **camelCase** and **PascalCase**. Acronym
boundaries (``XMLParser`` -> ``xml_parser``) and runs of separators (``_``,
``-``, whitespace) are handled.

## Usage

```python
from caseconv import to_camel, to_kebab, to_pascal, to_snake

assert to_snake("helloWorld") == "hello_world"
assert to_camel("hello_world") == "helloWorld"
assert to_pascal("hello-world") == "HelloWorld"
assert to_kebab("XMLParser") == "xml-parser"
```

## Tests

```bash
cd caseconv
pytest
```
