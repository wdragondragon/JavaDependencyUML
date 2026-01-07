def resolve_roots(roots, all_classes):
    """
    roots: 用户配置的 root（类 or 包）
    all_classes: 项目中所有已知类 FQN
    """
    resolved = set()

    for r in roots:
        if r in all_classes:
            # 精确类
            resolved.add(r)
        else:
            # 当作包前缀
            prefix = r + "."
            matched = {c for c in all_classes if c.startswith(prefix)}
            resolved |= matched

    return resolved
