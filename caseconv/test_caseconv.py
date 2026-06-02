from caseconv import to_camel, to_kebab, to_pascal, to_snake


def test_from_camel():
    assert to_snake("helloWorld") == "hello_world"
    assert to_kebab("helloWorld") == "hello-world"
    assert to_pascal("helloWorld") == "HelloWorld"
    assert to_camel("helloWorld") == "helloWorld"


def test_from_pascal():
    assert to_snake("HelloWorld") == "hello_world"
    assert to_camel("HelloWorld") == "helloWorld"


def test_from_snake():
    assert to_camel("hello_world") == "helloWorld"
    assert to_pascal("hello_world") == "HelloWorld"
    assert to_kebab("hello_world") == "hello-world"


def test_from_kebab():
    assert to_snake("hello-world") == "hello_world"
    assert to_camel("hello-world") == "helloWorld"


def test_acronym_boundary():
    assert to_snake("XMLParser") == "xml_parser"
    assert to_camel("XMLParser") == "xmlParser"


def test_with_numbers():
    assert to_snake("version2Number") == "version2_number"


def test_whitespace_input():
    assert to_snake("  Hello   World  ") == "hello_world"


def test_empty():
    assert to_snake("") == ""
    assert to_camel("") == ""
    assert to_pascal("") == ""
    assert to_kebab("") == ""
