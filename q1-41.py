import spacy

# Load SciSpaCy models
nlp_scispacy = spacy.load("en_core_sci_sm")

def extract_entities_scispacy(text):
    doc = nlp_scispacy(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

entities_scispacy = extract_entities_scispacy(consolidated_text)

# Save SciSpaCy entities to a CSV file
with open('entities_scispacy.csv', 'w', newline='') as csvfile:
    fieldnames = ['entity', 'label']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(entities_scispacy)
