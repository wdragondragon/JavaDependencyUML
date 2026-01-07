import javalang

def parse_tree(file):
    try:
        with open(file, encoding="utf-8") as f:
            return javalang.parse.parse(f.read())
    except Exception:
        return None


def build_import_map(tree):
    imports = {}
    for imp in tree.imports:
        if not imp.wildcard:
            short = imp.path.split(".")[-1]
            imports[short] = imp.path
    return imports
