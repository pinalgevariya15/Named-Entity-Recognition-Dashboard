from pathlib import Path
from ner_processor import extract_entities
import pandas as pd

# Location of our article folder
data_folder = Path("data")

all_entities =[]
 # read all data files
for file in data_folder.glob("*.txt"):
    print(f"processing:{file.name}")
    # Read article
    text = file.read_text(encoding="utf-8")
    #extract entities
    entities = extract_entities(text)
    #add article name to each entity
    for entity in entities:
        entity["article"]= file.name
        all_entities.append(entity)
#display all entities
print("\n========== ALL ENTITIES ==========")
for entity in all_entities:
    print(entity)
# Convert extracted entities into a DataFrame
df = pd.DataFrame(all_entities)

print("\n========== RAW DATAFRAME ==========")
print(df)
df["entity_normalized"] = (
    df["entity"]
    .str.strip()
    .str.lower()
)
display_names = (
    df.groupby(["entity_normalized", "type"])["entity"]
    .first()
    .reset_index()
)
# Aggregate entities and count frequency
frequency_df = (
    df.groupby(["entity_normalized", "type"])
    .size()
    .reset_index(name="frequency")
)

frequency_df = frequency_df.merge(
    display_names,
    on=["entity_normalized", "type"]
)

frequency_df = frequency_df[
    ["entity", "type", "frequency"]
]
# Sort by frequency
frequency_df = frequency_df.sort_values(
    "frequency",
    ascending=False
)

print("\n========== ENTITY FREQUENCY ==========")
print(frequency_df)