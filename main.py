from config import *
from graph_builder import collect_known_classes, build_dependency_graph
from dependency_closure import collect_dependencies
from dot_writer import write_dot
from root_resolver import resolve_roots
from graphviz_runner import generate_svg


def main():
    known_classes = collect_known_classes(SRC_ROOT)

    nodes, edges = build_dependency_graph(
        SRC_ROOT,
        known_classes,
        IGNORED_FIELD_CLASSES
    )

    root_classes = resolve_roots(ROOTS, known_classes)

    nodes, edges = collect_dependencies(root_classes, edges)

    write_dot(OUTPUT_DOT, nodes, edges, IGNORE_CLASSES)

    # ✅ 自动生成 svg
    generate_svg(OUTPUT_DOT)


if __name__ == "__main__":
    main()
