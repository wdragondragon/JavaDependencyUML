import javalang
from javalang.tree import BasicType
from file_scanner import walk_java_files
from ast_utils import parse_tree, build_import_map
from type_resolver import extract_type, find_class


def collect_known_classes(src_root):
    known = set()
    for file in walk_java_files(src_root):
        tree = parse_tree(file)
        if not tree:
            continue

        pkg = tree.package.name if tree.package else ""
        for _, c in tree.filter(javalang.tree.ClassDeclaration):
            known.add(f"{pkg}.{c.name}")
        for _, c in tree.filter(javalang.tree.AnnotationDeclaration):
            known.add(f"{pkg}.{c.name}")
    return known


def build_dependency_graph(src_root, known_classes, ignored_field_classes):
    nodes = set()
    edges = set()

    for file in walk_java_files(src_root):
        tree = parse_tree(file)
        if not tree:
            continue

        pkg = tree.package.name if tree.package else ""
        import_map = build_import_map(tree)

        for _, clazz in tree.filter(javalang.tree.ClassDeclaration):
            cls = f"{pkg}.{clazz.name}"
            nodes.add(cls)

            # extends
            if clazz.extends:
                edges.add((
                    cls,
                    find_class(import_map, pkg, clazz.extends, known_classes, pkg),
                    "extends"
                ))

            # implements
            for impl in clazz.implements or []:
                edges.add((
                    cls,
                    find_class(import_map, pkg, impl, known_classes, pkg),
                    "implements"
                ))

            # fields
            type_params = {tp.name for tp in clazz.type_parameters or []}

            for field in clazz.fields or []:
                if isinstance(field.type, BasicType):
                    continue

                for t in extract_type(field.type):
                    if t.name in type_params:
                        continue
                    if t.name.upper() in ignored_field_classes:
                        continue

                    edges.add((
                        cls,
                        find_class(import_map, pkg, t, known_classes, pkg),
                        "field"
                    ))

    return nodes, edges
