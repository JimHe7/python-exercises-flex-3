import io
file_handle = io.StringIO()
file_handle.write("Some more stuff")
contents = file_handle.getvalue()
file_handle = io.StringIO("initial text")
contents = file_handle.read()