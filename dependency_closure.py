def collect_dependencies(root_classes, edges):
    if not root_classes:
        return set(), set()

    visited = set()
    result_edges = set()

    refs = {}
    iface_impls = {}

    for a, b, t in edges:
        refs.setdefault(a, set()).add((b, t))
        if t in ("implements", "extends") and "Exception" not in b:
            iface_impls.setdefault(b, set()).add(a)

    def dfs(node):
        if node in visited:
            return
        visited.add(node)

        for b, t in refs.get(node, []):
            result_edges.add((node, b, t))
            dfs(b)

            if t == "field" and b in iface_impls:
                for impl in iface_impls[b]:
                    dfs(impl)

    for root in root_classes:
        dfs(root)

    return visited, result_edges
