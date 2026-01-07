DOT_HEADER = """
    digraph JavaDeps {
      rankdir=LR;

      graph [
        nodesep=1.2,
        ranksep=2.0,
        splines=polyline,
        overlap=false,
        concentrate=false
      ];

      node [
        shape=box,
        fontsize=10,
        margin="0.25,0.18"
      ];

      edge [
        fontsize=10,
        arrowsize=0.7
      ];
"""


def write_dot(filename, nodes, edges, ignore_classes):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(DOT_HEADER)

        for n in nodes:
            if n not in ignore_classes:
                f.write(f'"{n}" [label="{n}"];\n')

        for a, b, t in edges:
            if b in ignore_classes:
                continue

            style = "solid"
            if t == "implements":
                style = "dashed"
            elif t == "extends":
                style = "bold"

            f.write(f'"{a}" -> "{b}" [label="{t}", style="{style}"];\n')

        f.write("}\n")
