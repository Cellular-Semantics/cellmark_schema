-- # Class: "Axiom" Description: "An OWL axiom"
--     * Slot: id Description: 
-- # Class: "OntologyClass" Description: "An ontology class that can be associated with marker sets"
--     * Slot: id Description: 
-- # Class: "Marker" Description: "A specific marker that can be part of a marker set"
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: description Description: 
-- # Class: "MarkerSet" Description: "A named set of markers associated with an ontology class"
--     * Slot: id Description: 
--     * Slot: name Description: Name of the marker set, often derived from component marker names (e.g., "CD3+CD4+CD8+ T cell markers")
--     * Slot: description Description: 
--     * Slot: confidence_score Description: Confidence score for the marker set or annotation
--     * Slot: precision Description: Precision metric for the marker set
--     * Slot: recall Description: Recall metric for the marker set
-- # Class: "MarkerSet_has_part" Description: ""
--     * Slot: MarkerSet_id Description: Autocreated FK slot
--     * Slot: has_part_id Description: Relates a marker set to its component markers

CREATE TABLE "Axiom" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "OntologyClass" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Marker" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MarkerSet" (
	id TEXT NOT NULL, 
	name TEXT NOT NULL, 
	description TEXT, 
	confidence_score FLOAT, 
	precision FLOAT, 
	recall FLOAT, 
	PRIMARY KEY (id)
);
CREATE TABLE "MarkerSet_has_part" (
	"MarkerSet_id" TEXT, 
	has_part_id TEXT, 
	PRIMARY KEY ("MarkerSet_id", has_part_id), 
	FOREIGN KEY("MarkerSet_id") REFERENCES "MarkerSet" (id), 
	FOREIGN KEY(has_part_id) REFERENCES "Marker" (id)
);