import javalang
from javalang.tree import BasicType


def sub_type_class(t, full_name):
    if t:
        return sub_type_class(t.sub_type, f"{full_name}.{t.name}")
    return full_name


def find_class(imports, pkg, t, known_classes, default_pkg=""):
    name = t.name

    if t.sub_type:
        return sub_type_class(t.sub_type, name)

    if name in imports:
        return imports[name]

    if f"{pkg}.{name}" in known_classes:
        return f"{pkg}.{name}"

    if default_pkg:
        return f"{default_pkg}.{name}"

    return name


def extract_type(t):
    """
    递归提取 ReferenceType（包含泛型）
    """
    types = set()

    if t is None or isinstance(t, BasicType):
        return types

    if isinstance(t, javalang.tree.ReferenceType):
        types.add(t)
        for arg in t.arguments or []:
            if isinstance(arg, javalang.tree.TypeArgument) and arg.type:
                types |= extract_type(arg.type)
            else:
                types |= extract_type(arg)

    return types
