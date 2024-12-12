import re
import json
import config


with open(config.HTML_FILENAME, "r") as f:
    content = f.read()

start_pattern = "events: "
start_index = content.find(start_pattern) + len(start_pattern)
end_pattern = "],"
end_index = content.find(end_pattern, start_index) + 1

calendar_content = content[start_index:end_index]
calendar_content = re.sub("(?P<Key>(title)|(Nama)|(Jam)|(start)|(url)): ", "\"\g<Key>\": ", calendar_content)
calendar_content = calendar_content.replace("'", "\"")

calendar = json.loads(calendar_content)
# Remove unnecessary rows
def row_is_necessary(row):
    return (not "url" in row) and (row["title"] != "LIBUR")

calendar = list(filter(row_is_necessary, calendar))
with open(config.JSON_FILENAME, "w") as f:
    f.write(json.dumps(calendar))