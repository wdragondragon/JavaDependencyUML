SRC_ROOT = r"C:\dev\ideaProject\hive\jdbc\src\java\org\apache\hive\jdbc"
OUTPUT_DOT = "java-deps.dot"

IGNORED_FIELD_CLASSES = {
    "STRING", "INTEGER", "BOOLEAN",
    "FLOAT", "DOUBLE", "OBJECT", "LONG"
}

IGNORE_CLASSES = {
    "java.util.List",
    "java.util.Map",
    "java.util.Set",
    "java.util.Optional",
    "org.slf4j.Logger",
}

# root 模式：
# - 精确类
# - 包前缀
ROOTS = {
    # "org.apache.hive.jdbc",                  # 包
    "org.apache.hive.jdbc.HiveStatement"     # 类
}