# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

import json

x = '{"name":"tharchen", "age":"12", "city":"bhutan"}'
# If you have a JSON string, you can parse it by using the json.loads() method.
y = json.loads(x)

print(y['city'])

tex = {
    "name": "tharchen",
    "age": int(61),
}
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
tex1 = json.dumps(tex)
# print(tex1["name"])
print(tex1)

# Convert Python objects into JSON strings, and print the values:


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


xtox = {
    "name": "tharchen",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# direct to json .dunps
print(json.dumps(xtox))

# Format the Result
# The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
# The json.dumps() method has parameters to make it easier to read the result:

# use four indents to make it easier to read the result:
print(json.dumps(xtox, indent=4))


# Use the separators parameter to change the default separator:
print(json.dumps(xtox, indent=4, separators=(" . "," = ")))

# Order the Result
# The json.dumps() method has parameters to order the keys in the result:

# sort the result alphabetically by keys:
print(json.dumps(xtox, indent=4, sort_keys=True))























































