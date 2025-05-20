+-----------------------------+
|         Contact            |
+-----------------------------+
| - name: str                |
| - email: str               |
+-----------------------------+
| + __init__(name: str,      |
|            email: str)     |
| + __repr__() -> str        |
+-----------------------------+

             ▲
             |
             |
+-----------------------------+
|       ContactLists          |
|  (inherits from list)       |
+-----------------------------+
|                             |
+-----------------------------+
| + search(name: str)         |
|      -> list[Contact]       |
+-----------------------------+

Notes:
- ContactLists kế thừa từ list[Contact], do đó không cần định nghĩa lại __init__, trừ khi bạn muốn thêm logic tùy chỉnh.
- Quan hệ 1-n: ContactLists chứa nhiều Contact objects.
