# Auto generated from cellmark_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-25T10:23:03
# Schema: cellmark-schema
#
# id: https://example.org/cellmark
# description: Schema for relating ontology classes to sets of markers via annotation properties
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE

metamodel_version = "1.7.0"
version = None

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MS = CurieNamespace('ms', 'https://example.org/marker-sets/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MS


# Types

# Class references
class MarkerId(URIorCURIE):
    pass


class MarkerSetId(URIorCURIE):
    pass


class Axiom(YAMLRoot):
    """
    An OWL axiom
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Axiom"]
    class_class_curie: ClassVar[str] = "owl:Axiom"
    class_name: ClassVar[str] = "Axiom"
    class_model_uri: ClassVar[URIRef] = MS.Axiom


class OntologyClass(YAMLRoot):
    """
    An ontology class that can be associated with marker sets
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL["Class"]
    class_class_curie: ClassVar[str] = "owl:Class"
    class_name: ClassVar[str] = "OntologyClass"
    class_model_uri: ClassVar[URIRef] = MS.OntologyClass


@dataclass(repr=False)
class Marker(YAMLRoot):
    """
    A specific marker that can be part of a marker set
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MS["Marker"]
    class_class_curie: ClassVar[str] = "ms:Marker"
    class_name: ClassVar[str] = "Marker"
    class_model_uri: ClassVar[URIRef] = MS.Marker

    id: Union[str, MarkerId] = None
    name: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkerId):
            self.id = MarkerId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MarkerSet(YAMLRoot):
    """
    A named set of markers associated with an ontology class
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = MS["MarkerSet"]
    class_class_curie: ClassVar[str] = "ms:MarkerSet"
    class_name: ClassVar[str] = "MarkerSet"
    class_model_uri: ClassVar[URIRef] = MS.MarkerSet

    id: Union[str, MarkerSetId] = None
    name: str = None
    description: Optional[str] = None
    has_part: Optional[Union[Union[str, MarkerId], list[Union[str, MarkerId]]]] = empty_list()
    confidence_score: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MarkerSetId):
            self.id = MarkerSetId(self.id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.has_part, list):
            self.has_part = [self.has_part] if self.has_part is not None else []
        self.has_part = [v if isinstance(v, MarkerId) else MarkerId(v) for v in self.has_part]

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if self.precision is not None and not isinstance(self.precision, float):
            self.precision = float(self.precision)

        if self.recall is not None and not isinstance(self.recall, float):
            self.recall = float(self.recall)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=MS.id, name="id", curie=MS.curie('id'),
                   model_uri=MS.id, domain=None, range=URIRef)

slots.name = Slot(uri=MS.name, name="name", curie=MS.curie('name'),
                   model_uri=MS.name, domain=None, range=str)

slots.description = Slot(uri=MS.description, name="description", curie=MS.curie('description'),
                   model_uri=MS.description, domain=None, range=Optional[str])

slots.has_marker_set = Slot(uri=MS.has_marker_set, name="has_marker_set", curie=MS.curie('has_marker_set'),
                   model_uri=MS.has_marker_set, domain=OntologyClass, range=Optional[Union[Union[str, MarkerSetId], list[Union[str, MarkerSetId]]]])

slots.has_part = Slot(uri=BFO['0000051'], name="has_part", curie=BFO.curie('0000051'),
                   model_uri=MS.has_part, domain=MarkerSet, range=Optional[Union[Union[str, MarkerId], list[Union[str, MarkerId]]]])

slots.confidence_score = Slot(uri=MS.confidence_score, name="confidence_score", curie=MS.curie('confidence_score'),
                   model_uri=MS.confidence_score, domain=None, range=Optional[float])

slots.precision = Slot(uri=MS.precision, name="precision", curie=MS.curie('precision'),
                   model_uri=MS.precision, domain=MarkerSet, range=Optional[float])

slots.recall = Slot(uri=MS.recall, name="recall", curie=MS.curie('recall'),
                   model_uri=MS.recall, domain=MarkerSet, range=Optional[float])

slots.annotation_confidence = Slot(uri=MS.annotation_confidence, name="annotation_confidence", curie=MS.curie('annotation_confidence'),
                   model_uri=MS.annotation_confidence, domain=Axiom, range=Optional[float])

slots.derived_from_markers = Slot(uri=MS.derived_from_markers, name="derived_from_markers", curie=MS.curie('derived_from_markers'),
                   model_uri=MS.derived_from_markers, domain=MarkerSet, range=Optional[Union[bool, Bool]])

slots.MarkerSet_name = Slot(uri=MS.name, name="MarkerSet_name", curie=MS.curie('name'),
                   model_uri=MS.MarkerSet_name, domain=MarkerSet, range=str)