import subprocess
import os


def generate_svg(dot_file, svg_file=None):
    """
    使用 graphviz dot 生成 svg
    """
    if svg_file is None:
        svg_file = os.path.splitext(dot_file)[0] + ".svg"

    cmd = [
        "dot",
        "-Tsvg",
        dot_file,
        "-o",
        svg_file
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"SVG generated: {svg_file}")
    except FileNotFoundError:
        raise RuntimeError(
            "Graphviz not found. Please install graphviz and ensure 'dot' is in PATH."
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"dot command failed: {e}")
